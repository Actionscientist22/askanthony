# Text Summarization

In this activity, you will use a pre-trained Hugging Face Transformer model to summarize text of your choosing.

## Instructions

1. Import the `pipeline` class from the `transformers` module, and initialize the `pipeline` with the "summarization" task and the `facebook/bart-large-cnn` model.

2. Provide text of your choosing to summarize.

3. Get the most likely summary of the article using "False" for the `do_sample` parameter, and pass in the values for the `min_length` and `max_length`.

4. Get the most diverse summary of the article using "True" for the `do_sample` parameter, and pass in the values for the `min_length` and `max_length`.

5. Answer the following question:

    * How different were the most likely and diverse summaries of the text?

---

© 2023 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
