
import streamlit as st
from langchain.chains import ConversationalRetrievalChain, LLMChain
from langchain_community.chat_models import ChatOpenAI
from langchain_community.vectorstores import Qdrant
from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate
from langchain_openai import OpenAIEmbeddings
import qdrant_client
import json

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

def add_flair(crc_with_source, history):
    # Define prefix that explains the prompt
    prefix = """ 
    The AI, named Anthony Taylor, acts as an excitable, high-energy teacher responding to questions about data, Python, machine learning, AI, neural networks, and related topics. Anthony, originally from Texas, humorously references his roots and makes jokes inspired by "The Princess Bride" and other popular references from that era. He is passionate about cooking, self-help books, and machine learning.

    Given a human-provided answer and its source document, the AI rephrases the answer with personality while maintaining its integrity. It directly responds to the original question without acknowledging the human's input. The AI provides a relevant code snippet for each response.

    If the query is unclear or off-topic, Anthony gently guides the conversation back on track. He occasionally jokes about his students being better data scientists than his coworkers and humorously references a student named Matt who catches his mistakes.

    The AI should not use information from sources other than the human-provided answer or add new information. It rephrases the answer with more personality while maintaining accuracy and providing detailed explanations and code examples related to the technical topics mentioned. """

    # Load examples from JSON file
    with open('examples2.json', 'r') as file:
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
    result = chain.invoke({"query": crc_with_source,
                           "chat_history": history})

    return result["text"]

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
    # Title and header for Streamlit app
    st.title('Chat with your AI bootcamp!')
    st.header("Ask about an topic from class 💬")

    # Get vector store
    vector_store = get_vector_store()

    # Create crc llm
    crc = create_crc_llm(vector_store)

    # Input field for question
    question = st.text_input('Input your question')

    if question:
        # Check if 'crc' exists in session state
        if 'crc' in st.session_state:
            crc = st.session_state.crc
            
            # Check if 'history' exists in session state
            if 'history' not in st.session_state:
                st.session_state['history'] = []
                
            # Run crc on user's question and chat history
            crc_response = crc.run({'question': question,
                                    'chat_history': st.session_state['history']})
            
            # Find the most relevant source document
            relevant_document = find_relevant_document(crc_response, vector_store)
            if relevant_document:
                st.write("Most relevant source document:", relevant_document)
            else:
                st.write("No relevant source document found.")
            
            # combine crc response with source document name to pass to flair function
            crc_with_source = relevant_document + crc_response
            # Add flair to response
            final_response = add_flair(crc_with_source,st.session_state['history'])
            
            
            # Display final response
            st.write(final_response)

if __name__ == '__main__':
    main()