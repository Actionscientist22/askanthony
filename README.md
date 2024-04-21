# Chat with Anthony

Welcome to the "Chat with Anthony" project! This interactive application, powered by Streamlit and OpenAI, simulates a conversation with Anthony Taylor, a virtual AI instructor. Anthony can discuss topics such as data, Python, machine learning, artificial intelligence, neural networks, and more, adding personality and context to the conversations.

## Features

- AI-driven conversational interface.
- Context-aware responses with personality and flair, emulating an excitable and encouraging teacher.
- Uses the latest GPT-3.5 Turbo model for generating responses.
- Integration with a vector store for efficient document retrieval.

## Technologies Used

- **Streamlit**: For creating the web interface.
- **OpenAI's GPT-3.5 Turbo**: For natural language understanding and response generation.
- **LangChain**: For orchestrating AI models and vector stores.
- **Qdrant**: For efficient vector-based retrieval of documents.

## Getting Started

### Prerequisites

Ensure you have Python 3.8 or later installed on your machine. You will also need access to OpenAI APIs with the necessary API keys.

### Installation

To set up the project on your local machine:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/lordegraves/final_project_bootcamp.git

2. **Navigate to the repository folder:**
   ```bash
   cd final_project_bootcamp

3. **Install the required dependencies::**
   ```bash
   pip install streamlit
   pip install openai
   pip install langchain
   pip install qdrant-client
   pip install numpy


## Usage

To run the application:

1. Open a terminal in the project directory.
2. Start the program by executing:
   ```bash
   streamlit run chat_with_anthony
