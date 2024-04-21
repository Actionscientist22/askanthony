import streamlit as st
from langchain.chains import ConversationalRetrievalChain
from langchain_community.chat_models import ChatOpenAI
from langchain_community.vectorstores import Qdrant
from langchain_openai import OpenAIEmbeddings
import qdrant_client
import os
from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate

st.set_page_config(page_title=None, page_icon=None, layout="centered", initial_sidebar_state="auto", menu_items=None)

def get_vector_store():
    client = qdrant_client.QdrantClient(
        st.secrets["QDRANT_HOST"], 
        api_key=st.secrets["QDRANT_API_KEY"]
    )
    embeddings = OpenAIEmbeddings()
    vector_store = Qdrant(
        client=client,
        collection_name=st.secrets["QDRANT_COLLECTION_NAME"],
        embeddings=embeddings,
    )
    return vector_store

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
    # Set the model name for our LLMs.
    OPENAI_MODEL = "gpt-3.5-turbo"

    # Store the API key in a variable.
    OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]

    st.title('Chat with your AI bootcamp!')
    st.header("Ask about a topic from class 💬")

    # create vector store
    vector_store = get_vector_store()

    # create crc llm
    llm = ChatOpenAI(model='gpt-3.5-turbo', temperature=1)
    retriever = vector_store.as_retriever()
    crc = ConversationalRetrievalChain.from_llm(llm, retriever)
    st.session_state.crc = crc

    st.success('Activities, slides, and transcripts are loaded')

    # question
    question = st.text_input('Input your question')
    if question:
        if 'crc' in st.session_state:
            crc = st.session_state.crc
            if 'history' not in st.session_state:
                st.session_state['history'] = []
            response = crc.run({'question': question, 'chat_history': st.session_state['history']})
            st.session_state['history'].append((question, response))
            st.write(response)

            # Find the most relevant source document
            relevant_document = find_relevant_document(response, vector_store)
            if relevant_document:
                st.write("Most relevant source document:", relevant_document)
            else:
                st.write("No relevant source document found.")

if __name__ == '__main__':
    main()