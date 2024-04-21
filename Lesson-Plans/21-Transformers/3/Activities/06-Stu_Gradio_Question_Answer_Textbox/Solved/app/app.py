# %%
# Uncomment these lines if you are using Google Colab.
# ! pip install transformers
# ! pip install gradio

# %%
# Import transformers pipeline
from transformers import pipeline
# Import Gradio
import gradio as gr

# %%
# Initialize the pipeline to generate questions and answers using the distilbert-base-cased-distilled-squad model. 
question_answerer = pipeline("question-answering", model='distilbert-base-cased-distilled-squad')

# %%
# Create a function called `question_answer` that takes two parameters, the text to search and a question.
# The function should return the question, answer, probability score, and the starting and ending index of the answer.
def question_answer(text, question):
    result = question_answerer(question=question, context=text)
    return question, result['answer'], result['score'], result['start'], result['end']

# %%
# Create the app with two Textbox components. 
# The first textbox will take the text to search the second will take the question.
# The output should show the question, answer, probability score, and the starting and ending index of the answer.

app = gr.Interface(
    fn=question_answer,
    inputs = [
        gr.Textbox(label="Paste the text to search."), 
        gr.Textbox(label="Ask a question.")],
    outputs=gr.Textbox(lines=10, label="Answer to question, probability score, and location.", show_copy_button=True))
    
# Launch the app.
app.launch(show_error=True)

# %% [markdown]
# **The text to paste:**
# 
# A transformer is a deep learning model that adopts the mechanism of self-attention, differentially weighting the significance of each part of the input data. It is used primarily in the fields of natural language processing (NLP)[1] and computer vision (CV).[2]
# 
# Like recurrent neural networks (RNNs), transformers are designed to process sequential input data, such as natural language, with applications towards tasks such as translation and text summarization. However, unlike RNNs, transformers process the entire input all at once. The attention mechanism provides context for any position in the input sequence. For example, if the input data is a natural language sentence, the transformer does not have to process one word at a time. This allows for more parallelization than RNNs and therefore reduces training times.[1]
# 
# Transformers were introduced in 2017 by a team at Google Brain[1] and are increasingly becoming the model of choice for NLP problems,[3] replacing RNN models such as long short-term memory (LSTM). The additional training parallelization allows training on larger datasets. This led to the development of pretrained systems such as BERT (Bidirectional Encoder Representations from Transformers) and GPT (Generative Pre-trained Transformer), which were trained with large language datasets, such as the Wikipedia Corpus and Common Crawl, and can be fine-tuned for specific tasks.[4][5]

# %% [markdown]
# **Questions to ask.**
# 1. Who introduced transformers?
# 2. Why is parallelization important?
# 3. What pretrained systems were developed from parallelization?

# %%



