# The Case of the Vanishing Gradient

In this activity, you will clean and tokenize a Sherlock Holmes short story, "A Case of Identity", then create and train a LSTM using the tokenized text. After the model has been trained the students will provide the model with 25 words from the short novel as a seed text, then the model will return the next 25 words from the short story.


## Instructions

1. Import the dependencies and load spaCy's large english model.

2. Use the `read_file` function to read in the `A_Case_Of_Identity.txt` file.

### Tokenize and Clean the Text

1. Use the `separate_punc`function to tokenize the text using spaCy and then clean the text.

2. Look over the tokens to make sure the majority of the punctuation has been removed.

### Create Sequences of Tokens

1. Write a `for` loop that iterates through the `tokens` and creates sequences consisting of 26 tokens and add each sequence to a list.

2. Confirm that the length of the text sequences is 26 less than the total tokens.

### Perform Tokenization with Keras

1. Initialize the Keras `Tokenizer` class.

2. Use the `Tokenizer` class to map each word with an index.

3. Check the size of the vocabulary that is created with the `Tokenizer` class.

4. Encode each word in the text sequences to their indices.

### Convert the List of Sequences to Arrays.

1. Use `numpy` to convert all the sequences of indices to arrays.

2. Confirm that the length of the array is the same as the length of text sequences.

### Create Input Sequences and One-Hot Encode the Target Variable

1. Set the input variable `X` to the first 25 numbers of each array.

2. Set target variable `y` to the last number of each array.

3. Check the shape of each variable, and set the `seq_len` equal to the length of each array.

4. One-hot encode the target variable to transform each index to a binary value. Make sure to set the `num_classes` parameter equal to the length of the vocabulary plus "1."

### Create a LSTM Model and Train the Model

1. Use the `create_model` function to create and compile an LSTM-based sequential model for text generation.

2. Define the model and pass in the with the vocabulary size plus "1" and the `seq_len`.

3. Fit the model with the input and target variables, `epochs` equal to 290&ndash;300, and a `batch_size` equal to 128.

    * **Note:** This model may take 45&ndash;50 minutes to run depending on your machine.

4. After the model has run save the model weights and tokenizer if the percent accuracy is greater than 90%.


### Generate Text

1. Use the `generate_text` function to generate text using a trained language model.

2. Choose a 26-word piece of text from the short story "A Case of Identity."

3. Tokenize and clean the 26-word text you chose, join the tokens, and set the equal to the `seed_text` variable.

4. Call the `generate_text` function by passing in the rained model weights a tokenizer, `seq_len`, `seed_text` and `num_gen_words=25`.

### Analyze the Generated Text

* Use the "A Case of Identity" text file to determine the accuracy of your model.

## Reference

Doyle, A.C. 1891. A Case of Identity. *Project Gutenberg Literary Archive Foundation*. Available https://www.gutenberg.org/ [2023, October 25]. [2023, October 25]. ([CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/)).

---

© 2023 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
