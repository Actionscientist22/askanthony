# Word and Bigram Corpus Counter

In this activity, you will create two DataFrames, one that has the top 10 most common words and another that has the top 10 most common bigrams from Reuters articles on grain.

First, you will write a function that will combine all the articles on grain from the Reuters library and preprocess the combined articles with the `process_text` function. After the articles have been processed, the top 10 most common words will be added to a DataFrame.

Then, you will write a function that will combine all the articles on grain from the Reuters library and preprocess the combined articles with the `process_text` function. After the articles have been processed, the top 10 most common bigrams will be added to a DataFrame.


## Instructions

* Create a function called `word_counter` that takes in a combined list of documents and outputs a DataFrame that contains the top 10 most frequent words in the list of documents. The combined list of documents should be processed by the `process_text` function before you create the DataFrame.

* Create a `bigram_counter` function that takes in a combined list of documents and outputs a DataFrame that contains the top 10 most frequent bigrams in the list of documents. The combined list of documents should be processed by the `process_text` function before you create the DataFrame.

**Hint:** Creating a DataFrame from a dictionary where the keys are not column names can be tricky. One way of doing so involves using the `items()` function of the dictionary. Use Google to your advantage if you're having trouble implementing this part!

## Reference

Lewis, D. 1997. Reuters-21578 Text Categorization Collection. *UCI Machine Learning Repository*. Available https://archive.ics.uci.edu/dataset/137/reuters+21578+text+categorization+collection [2023, October 25]. ([CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/legalcode)).

---

© 2023 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
