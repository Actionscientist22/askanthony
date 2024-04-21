# Q&A Testing

In this activity, you will work with a partner to create a question and answering system using a pre-trained Hugging Face Transformer model.

## Instructions

1. Import the `pipeline` class from the `transformers` module, and initialize the `pipeline` with the "question-answering" task and the `distilbert-base-cased-distilled-squad` model.

2. Provide text for the question and answering system.

3. Generate a list of questions.

4. Check the output from one question by passing one question and text to the `question_answerer` object.

5. Use the `question_answer` function to generate the answers from the questions, and populate a DataFrame with the question, answer, the probability score, and the starting and ending indices of where the answer is located in the text.

6. Call the `question_answer` function by passing each question and the text into the function.

7. Answer the following question:

    * Based on the probability score, how accurate were the answers to your questions?


## Reference

*History of video games*. 2023. Wikipedia. Available: https://en.wikipedia.org/wiki/History_of_video_games [2023, December 14].

---

© 2023 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
