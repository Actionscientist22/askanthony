# Text Generation Playground

In this activity, you will test three different pre-trained Hugging Face Transformer models to generate text and compare the outputs from the models.

## Instructions

1. Import the `pipeline` class from the `transformers` module.

2. Set the `prompt` variable equal to the text of your choosing for the text generation task.

3. Using the `text_generator` function, pass the model and the prompt to the function and have the function do the following:

    * Initialize the `pipeline` class with the 'text-generation' task and the pre-trained transformer model.
    * Pass the prompt, and the `max_length`, and `pad_token_id` parameters with the appropriate values to the initialized `pipeline` class object.
    * Have the function return the generated text.

4. Call the `text_generator` function with the "EleutherAI/gpt-neo-125m" pre-trained model and the prompt, and display the generated text.

5. Call the `text_generator` function with the "EleutherAI/gpt-neo-1.3B" pre-trained model and the prompt, and display the generated text.

6. Call the `text_generator` function with the "EleutherAI/gpt-neo-2.7B" pre-trained model and the prompt, and display the generated text.

7. Answer the following question:

    * What was the best model? Why?

---

© 2023 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
