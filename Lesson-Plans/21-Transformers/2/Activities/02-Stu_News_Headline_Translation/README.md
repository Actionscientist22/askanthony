# News Headline Translation

In this activity, you will use a Hugging Face Transformer pre-trained model to translate text into one or more languages.

## Instructions

### Use Transformers `AutoTokenizer` and `TFAutoModelForSeq2SeqLM` to Translate Each News Headline.

1. Import the `Autotokenizer` and `TFAutoModelForSeq2SeqLM` classes from the `transformers` module.

2. Create an instance of the `Autotokenizer` class using the `t5-base` model and `model_max_length=256`.

3. Create a list to hold the input IDs for the news headlines.

4. Using the `create_input_ids` function, pass in each headline from the list of news headlines and retrieve the translation input IDs from each headline by doing the following:
    * Create a translate prompt for each headline using the `Autotokenizer` object to get the input IDs.
    * Append each input ID to the list you created in Step 3 and have the function return the list.

5. Using a `for` loop, pass each headline to the `create_input_ids` function and then print out the headline input IDs array to make sure you get the correct format.

6. Create an instance of the `TFAutoModelForSeq2SeqLM` class using the `t5-base` model.

7. Create a list to hold the translated headline.

8. Using the `decode` function, pass in each input ID from the list of headline input IDs to generate the output IDs from the model by doing the following:
    * Create the output id from the input id using the `generate` function.
    * Append each decoded output ID, i.e., translation to the translated headline list and have the function return the list.

9. Using a `for` loop, pass each input ID to the `decode` function.

10. Print out each translated headline.

### Use the Transformer Pipeline to Translate Each Headline.

1. Import the `pipeline` class from the `transformers` module, and initialize the `pipeline` to translate using the `t5-base` model.

2. Create a list to hold the translated headline.

3. Using the `translate` function to translate each English headline into French by doing the following:
    * Set the translate prompt to a variable
    * Pass the translated variable to the translator method.
    * Append the translated text to the translated headline list and have the function return the list.

4. Using a `for` loop, pass each headline to the `translate` function.

5. Print out each translated headline

---

© 2023 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
