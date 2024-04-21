# Crude Oil Stopwords

In this activity, you will practice creating a function that performs the preprocessing steps on a news article about crude oil.

## Instructions

1. After importing the necessary dependencies and downloading the `nltk` corpora libraries, retrieve the second article from the crude oil categories of the Reuters library, and print out the article.

2. Complete the function called `clean_text` that processes an article and returns a unique list of words after you have done the following:
    * Use a regular expression to substitute everything that is not a letter with an empty string.
    * Tokenize the words.
    * Clean the words to retrieve only the words that aren't in the "stopwords" list.

3. Inspect the results of this function and keep track of the words within the results that are uninformative. Use some of these words to customize the stopwords in step 4.

4. Complete the function `clean_text_again` that process an article and returns a unique list of words after you have done the following:
    * Create a dictionary of additional stopwords.
    * Use a regular expression to substitute everything that is not a letter with an empty string.
    * Tokenize the words.
    * Clean the words to retrieve only the words that aren't in the "stopwords" list.

**Hint:** Use the `union` method to add your customized stopwords to the nltk stopwords.

## Reference

Lewis, D. 1997. Reuters-21578 Text Categorization Collection. *UCI Machine Learning Repository*. Available https://archive.ics.uci.edu/dataset/137/reuters+21578+text+categorization+collection [2023, October 25]. ([CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/legalcode)).

---

© 2023 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
