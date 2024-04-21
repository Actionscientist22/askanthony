# Describing America

In this activity, you will determine if stopwords can affect the ability of a linear SVC model to predict the classification of a movie review.

## Instructions

1. Import the dependencies and load the `imdb_reviews.csv` dataset into a DataFrame.

2. Check the data for missing values and drop any null values.

3. Determine how many positive and negative reviews there are.

#### Split the data into training and testing data sets.

1. Set the features variable, `X`, to the "review" column.

2. Set the target variable, `y`, to the "label" column.

3. Split the data into training and testing and use `test_size = 30%`.

4. Build a pipeline using `TfidfVectorizer()` and `LinearSVC()`. Do not use `stopwords`.

5. Fit the data to the model.

6. Validate the model by checking the model's training and testing accuracy.

#### Run predictions and analyze the results.

1. Retrieve the first 30 predictions from the model.

2. Print the confusion matrix, the classification report, and overall accuracy of the model.

3. Create or find a movie review of your choice and pass it into the model's `predict()` method, and print out the review's classification.

#### Rebuild the Pipeline using `stopwords`.

1. Use `stopwords='english` in the `TfidfVectorizer` class.

2. Fit the data to the model.

3. Validate the model by checking the model's training and testing accuracy.

4. Retrieve the first 30 predictions from the model.

5. Print the confusion matrix, the classification report, and overall accuracy of the model.

6. Use the same review as before and pass it in the model's `predict()` method, and print out the review's classification.

7. Answer the following questions.
    * Did the review change?
    * If so why do you think it changed?

#### Rebuild the Pipeline using custom `stopwords`.

1. Using the following custom `stopwords` in the `TfidfVectorizer` class.

    ```text
    custom_stopwords = ['a', 'about', 'an', 'and', 'are', 'as', 'at', 'be', 'been', 'but', 'by', 'can', \
             'even', 'ever', 'for', 'from', 'get', 'had', 'has', 'have', 'he', 'her', 'hers', 'his', \
             'how', 'i', 'if', 'in', 'into', 'is', 'it', 'its', 'just', 'me', 'my', 'of', 'on', 'or', \
             'see', 'seen', 'she', 'so', 'than', 'that', 'the', 'their', 'there', 'they', 'this', \
             'to', 'was', 'we', 'were', 'what', 'when', 'which', 'who', 'will', 'with', 'you']
    ```

2. Fit the data to the model.

3. Validate the model by checking the model's training and testing accuracy.

4. Retrieve the first 30 predictions from the model.

5. Print the confusion matrix, the classification report, and overall accuracy of the model.

6. Use the same review as before and pass it in the model's `predict()` method, and print out the review's classification.

7. Answer the following questions.
    * Did the review change?
    * If so why do you think it changed?


## Reference

Dimitrios, K. 2015. Sentiment Labelled Sentences. *UCI Machine Learning Repository*. Available https://archive.ics.uci.edu/dataset/331/sentiment+labelled+sentences [2023, October 25]. ([CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/legalcode)).

---

© 2023 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
