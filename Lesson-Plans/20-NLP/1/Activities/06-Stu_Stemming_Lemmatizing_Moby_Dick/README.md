# Stemming and Lemmatization of Moby Dick

In this activity, you will write a function that performs the preprocessing steps of stopword removal, regular expressions to remove non-letter characters, word tokenizing, stemming and lemmatization on the American classic novel _Moby Dick_, written by Herman Melville.

## Instructions

1. Import the dependencies, instantiate the `WordNetLemmatizer` and `SnowballStemmer`.

2. Read in the `melville-moby_dick.txt` from the `gutenberg` library and use the regular expression code to return all the text after Chapter 1.

3. Complete the function called `process_text_stemming` that processes the `melville-moby_dick.txt` and returns a list of words after you have done the following:
    * Use a regular expression to substitute everything that is not a letter with an empty string.
    * Tokenize the words.
    * Apply the `SnowballStemmer` to get the stem of the words.
    * Clean the words to retrieve only the words that aren't in the "stopwords" list.

4. Complete the function called `process_text_lemmatizaton` that processes the `melville-moby_dick.txt` and returns a list of words after you have done the following:
    * Use a regular expression to substitute everything that is not a letter with an empty string.
    * Tokenize the words.
    * Apply the `lemmatizer` to get the root of the words.
    * Clean the words to retrieve only the words that aren't in the "stopwords" list.

5. When you're done, try different `pos` arguments for the lemmatization portion and compare the results.

## Reference

Project Gutenberg Literary Archive Foundation. Available [https://www.gutenberg.org/](https://www.gutenberg.org/) [2023, October 25].

---

© 2023 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
