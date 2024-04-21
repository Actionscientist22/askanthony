# Tokenizing Reuters

In this activity, you will practice both sentence and word tokenization on some articles from the Reuters Corpus.

## Instructions

1. Search the Reuters Corpus for articles under the category "income."

2. Get all "fileids" associated with income.

3. Using list comprehensions, get all raw stories and the ids in separate lists. Remove the "test/" from the ids so only the id number is retained.

4. Get the sentence tokens for each story using a list comprehension.

5. Use the following steps to get the word tokens:
    * Initialize an empty list named `word_tokenized` to store the tokenized words.
    * Implement a nested `for` loop to iterate through each story within the tokenized sentences list created in step 4.
    * Inside the `for`loop do the following:
       * Create an empty list named `words` to store the tokenized words for each story.
       * Implement a second `for` loop to iterate through each sentence within the current story.
       * Use the `word_tokenize` function to tokenize the words from each sentence.
       * Concatenate the tokenized words to the `words` list (i.e., do not use `append`).
   * Finally, append all `words` list to the `word_tokenized` list.

6. Place the raw articles, the tokenized sentence from the articles, and the tokenized words from the articles in a DataFrame with appropriate column headers.
    * Each row in the "sentence_tokenized" column should contain a list of sentences, and each row in the "word_tokenized" column should contain a list of words.
    * The index of the DataFrame are the ids from step 3.

**Hint:** Use a nested `for` loop to apply the word tokenizer to each sentence. You can combine several lists into a DataFrame, and include column headers, using dictionary syntax with the `pandas.DataFrame` function.

## Reference

Lewis, D. 1997. Reuters-21578 Text Categorization Collection. *UCI Machine Learning Repository*. Available https://archive.ics.uci.edu/dataset/137/reuters+21578+text+categorization+collection [2023, October 25]. ([CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/legalcode)).

---

© 2023 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
