import streamlit as st
from langchain.chains import ConversationalRetrievalChain, LLMChain
from langchain_community.chat_models import ChatOpenAI
from langchain_community.vectorstores import Qdrant
from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate
from langchain_openai import OpenAIEmbeddings
import qdrant_client

st.set_page_config(page_title=None,
                   page_icon=None,
                   layout="centered",
                   initial_sidebar_state="auto",
                   menu_items=None)

def get_vector_store():
    client = qdrant_client.QdrantClient(st.secrets["QDRANT_HOST"], api_key=st.secrets["QDRANT_API_KEY"])
    embeddings = OpenAIEmbeddings()
    vector_store = Qdrant(client, collection_name=st.secrets["QDRANT_COLLECTION_NAME"], embeddings=embeddings)
    return vector_store

def create_crc_llm(vector_store):
    llm = ChatOpenAI(model='gpt-3.5-turbo', temperature=1)
    retriever = vector_store.as_retriever()
    crc = ConversationalRetrievalChain.from_llm(llm, retriever)
    st.session_state.crc = crc
    st.success('Activies, slides and transcipts are loaded')
    return crc

def add_flair(crc_response):
    llm = ChatOpenAI(model='gpt-3.5-turbo', temperature=1)
    prefix = """
    Here are examples between a human and AI. The human provides a word, and
    the AI provides a single sentence with easy to read words that mostly rhyme
    with the word the human provided. The sentence does not have to include the 
    original word. For example:
    """
    examples = [
        {"query": "rat", "answer": "The cat sat next to the bat."},
        {"query": "frog", "answer": "A dog hops a log in the bog."},
        {"query": "ten", "answer": "Ben sent ten hens to the glen."}
    ]
    example_format = """Human: {query}\nAI: {answer}"""
    example_template = PromptTemplate(input_variables=["query", "answer"], template=example_format)
    suffix = """\n\nHuman: {query}\nAI:"""
    prompt_template = FewShotPromptTemplate(examples=examples, example_prompt=example_template, input_variables=["query"],
                                            prefix=prefix, suffix=suffix, example_separator="\n")
    chain = LLMChain(llm=llm, prompt=prompt_template, verbose=False)
    query = {"query": crc_response}
    result = chain.invoke(query)
    return result["text"]

def main():
    OPENAI_MODEL = "gpt-3.5-turbo"
    OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
    
    st.title('Chat with your AI bootcamp!')
    st.header("Ask about an topic from class 💬")

    vector_store = get_vector_store()
    crc = create_crc_llm(vector_store)

    question = st.text_input('Input your question')

    if question:
        if 'crc' in st.session_state:
            crc = st.session_state.crc
            if 'history' not in st.session_state:
                st.session_state['history'] = []
                
            crc_response = crc.run({'question': question,'chat_history': st.session_state['history']})
            final_response = add_flair(crc_response)
            st.session_state['history'].append((question,crc_response))
            
            st.write(final_response)

if __name__ == '__main__':
    main()