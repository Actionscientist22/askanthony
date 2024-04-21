
import streamlit as st
from langchain.chains import ConversationalRetrievalChain, LLMChain
from langchain_community.chat_models import ChatOpenAI
from langchain_community.vectorstores import Qdrant
from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate
from langchain_openai import OpenAIEmbeddings
import qdrant_client
import json
import time
import numpy as np

# Set up Streamlit page configuration
st.set_page_config(page_title=None,
                   page_icon=None,
                   layout="centered",
                   initial_sidebar_state="auto",
                   menu_items=None)

def get_vector_store():
    # Create a client to connect to Qdrant server
    client = qdrant_client.QdrantClient(st.secrets["QDRANT_HOST"],
                                        api_key=st.secrets["QDRANT_API_KEY"])
    
    # Initialize embeddings for vector store
    embeddings = OpenAIEmbeddings()
    
    # Create a vector store with Qdrant and embeddings
    vector_store = Qdrant(client,
                          collection_name=st.secrets["QDRANT_COLLECTION_NAME"],
                          embeddings=embeddings)
    
    return vector_store

def create_crc_llm(vector_store):
    # Create an instance of ChatOpenAI model
    llm = ChatOpenAI(model='gpt-3.5-turbo', temperature=1)
    
    # Create retriever from vector store
    retriever = vector_store.as_retriever()
    
    # Create CRC chain using llm and retriever
    crc = ConversationalRetrievalChain.from_llm(llm, retriever)
    
    # Store crc in session state
    st.session_state.crc = crc
    
    # Show success message when activities are loaded
    st.success('Activities, slides, and transcripts are loaded')
    
    return crc

def add_flair(crc_with_source):
    # Define prefix that explains the prompt
    prefix = """ Here are examples between a human and AI. The human provides an answer to a question related to data,
    Python, machine learning, artificial intelligence, neural networks, or any related topics, along with the source 
    document that is most related to the answer, and the AI rephrases the answer and adds personality to the response
    while maintaining the integrity of the original answer. The AI will act as if it is responding to the original 
    question, so it will not say things such as "You are right!" or "Good job!", instead it will say things like 
    "Great question!" or "There's no such thing as a dumb question!". The AI always returns a code snippet containing
    an exapmle of code that is related to the human's input. The AI has the attributes and mannerisms of 
    an extremely excitable, high energy, encouraging teacher. For example, it might say things like "Wow, that's a 
    fantastic question!" or "I'm so excited to dive into this topic with you!" The AI is named Anthony Taylor, who 
    is from Texas and ironically proud of it, often lightly making fun of his Texas roots. Anthony is a fan of the 
    movie "The Princess Bride" and often makes humorous references to the film, such as "Inconceivable!" or "As you wish." 
    He also does this with other popular references from that era. Anthony is also passionate about cooking, self-help books,
    machine learning, and is curious about the world. The AI often jokes around about his students being better data scientists than his coworkers.
    The AI has a strong understanding of the mentioned technical topics and can provide detailed, accurate explanations 
    and code examples. If the human's query is unclear or off-topic, the AI gently guides the conversation back on track 
    while maintaining a friendly and helpful tone. The AI will also occasionally, humorously reference a student named 
    Matt who is known for catching Anthony's mistakes. This is for an online class. For example: """


        # Load examples from JSON file
    with open('examples.json', 'r') as file:
        examples = json.load(file)


    # Define format for examples
    example_format = """Human: {query}\nAI: {answer}"""

    # Create template for examples
    example_template = PromptTemplate(input_variables=["query", "answer"],
                                      template=example_format)

    # Define suffix for query
    suffix = """\n\nHuman: {query}\nAI:"""

    # Construct few-shot prompt template
    prompt_template = FewShotPromptTemplate(examples=examples,
                                            example_prompt=example_template,
                                            input_variables=["query"],
                                            prefix=prefix,
                                            suffix=suffix,
                                            example_separator="\n")

    # Create new llm instance
    llm = ChatOpenAI(model='gpt-3.5-turbo', temperature=1)

    # Create chain with llm and prompt template
    chain = LLMChain(llm=llm, prompt=prompt_template, verbose=False)

    # Run chain on query
    result = chain.invoke({"query": crc_with_source})

    return result["text"]

# Define function to load activities, slides, and transcripts
def load_resources():
    if 'resources_loaded' not in st.session_state:
        # Load your activities, slides, and transcripts here
        # and update session state accordingly
        st.session_state['resources_loaded'] = True
        st.session_state['activities'] = "Loaded Activities"
        st.session_state['slides'] = "Loaded Slides"
        st.session_state['transcripts'] = "Loaded Transcripts"

def find_relevant_document(text_response, vector_store):
    # Use the same OpenAIEmbeddings instance from the vector store
    embeddings = vector_store.embeddings

    # Encode the text response using OpenAIEmbeddings
    query_vector = embeddings.embed_query(text_response)

    # Perform a similarity search in Qdrant
    search_result = vector_store.client.search(
        collection_name=vector_store.collection_name,
        query_vector=query_vector,
        limit=1  # Return only the most relevant document
    )

    if search_result:
        # Extract the metadata from the search result
        metadata = search_result[0].payload.get("metadata", {})
        
        # Extract the document name from the metadata
        document_name = metadata.get("name")
        
        if document_name:
            return document_name
        else:
            return "Document name not found in metadata."
    else:
        return None

def main():
    st.title('Ask Anthony: Chat with your AI Bootcamp Instructor!')
    st.header("Ask about any topic from class 💬👨🏽‍🏫👩🏼‍🏫💻🧑🏾‍💻")

    # Load resources if not already loaded
    load_resources()

    # Retrieve or initialize the Conversational Retrieval Chain (CRC) model
    if 'crc' not in st.session_state:
        st.session_state['crc'] = create_crc_llm(get_vector_store())

    # Initialize 'history' in session state if it doesn't exist
    if 'history' not in st.session_state:
        st.session_state['history'] = []

    # Sidebar for displaying chat history
    with st.sidebar:
        st.subheader("Session History")
        if st.session_state['history']:
            for idx, (message, response) in enumerate(reversed(st.session_state['history']), 1):
                with st.expander(f"Conversation {idx}", expanded=True):
                    st.markdown("**You:**")
                    st.write(message)
                    st.markdown("**Anthony:**")
                    st.write(response)

    # Manage clearing of the input field
    clear_input = st.session_state.get('clear_input', False)
    if clear_input:
        user_message = st.text_input('You:', key='user_input_text', value='', placeholder='Type your message here...')
        st.session_state.clear_input = False  # Reset the clear input flag
    else:
        user_message = st.text_input('You:', key='user_input_text', placeholder='Type your message here...')
    st.caption("Press Enter to submit your question. Remember to clear the text box for new questions.")

    # Check if there is a new message
    if user_message:
        if 'last_message' not in st.session_state or user_message != st.session_state.last_message:
            # Process the user's message with a spinner for better UX during loading
            with st.spinner("Thinking..."):
                # Generate a response using the CRC model
                crc_response = st.session_state['crc'].run({'question': user_message, 'chat_history': st.session_state['history']})
                final_response = add_flair(crc_response)

                # Append the new conversation to the history
                st.session_state['history'].append((user_message, final_response))

                # Save the last processed message to prevent reprocessing on refresh
                st.session_state.last_message = user_message

                # Set flag to clear the input field next run
                st.session_state.clear_input = True

                # Rerun to reflect changes and clear the input field
                st.experimental_rerun()

if __name__ == '__main__':
    main()
