import streamlit as st
from langchain.chains import ConversationalRetrievalChain
from langchain_community.chat_models import ChatOpenAI
from langchain_community.vectorstores import Qdrant
from langchain_openai import OpenAIEmbeddings
import qdrant_client
import os
from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate

st.set_page_config(page_title=None,
                   page_icon=None,
                   layout="centered",
                   initial_sidebar_state="auto",
                   menu_items=None)

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

def main():
    # Set the model name for our LLMs.
    OPENAI_MODEL = "gpt-3.5-turbo"
    # Store the API key in a variable.
    OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
    
    st.title('Chat with your AI bootcamp!')
    
    # st.set_page_config(page_title="Ask Qdrant")
    st.header("Ask about an topic from class 💬")
    
    # create vector store
    vector_store = get_vector_store()
        
    # create crc llm
    llm = ChatOpenAI(model='gpt-3.5-turbo', temperature=1)
    
    retriever=vector_store.as_retriever()
    
    # chain
    crc = ConversationalRetrievalChain.from_llm(llm,retriever)
    st.session_state.crc = crc
    st.success('Activies, slides and transcipts are loaded')

    # question
    question = st.text_input('Input your question')

    if question:
        if 'crc' in st.session_state:
            crc = st.session_state.crc
            if 'history' not in st.session_state:
                st.session_state['history'] = []

            response = crc({'question':question,'chat_history':st.session_state['history']})

            st.session_state['history'].append((question,response))
            
            st.write(response)

            # #st.write(st.session_state['history'])
            # for prompts in st.session_state['history']:
            #     st.write("Question: " + prompts[0])
            #     st.write("Answer: " + prompts[1])    
                
if __name__ == '__main__':
    main()


