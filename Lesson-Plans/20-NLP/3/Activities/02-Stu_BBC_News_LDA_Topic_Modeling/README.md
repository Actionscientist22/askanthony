# BBC News Topic Modeling with LDA

In this activity, you will use LDA to determine the topic for BBC News summaries. After you have determined the label for each topic you'll add two new columns to the original DataFrame that assigns each news summary a topic number and topic label.

## Instructions

1. Import the dependencies and load the `bbc_news_articles.csv` dataset into a DataFrame.

#### Preprocessing

1. Check the data for missing values and drop any null values.

2. Remove any numbers and non-alphabetic characters from the "news_summary" column.

#### Process the Text to Tokens and Counts.

1. Create an instance of the `CountVectorizer()` class and set the `max_df` and `min_df` parameters to 0.95 and 5, respectively, and use `stopwords="english"`.

2. Transform each row from the "news_summary" column to a document term matrix (DTM) and get the shape of the DTM.

3. Create an instance of the `LatentDirichletAllocation()` class with five topics.

4. Fit the instance of our model with our DTM data, and check the length of the vocabulary.

#### Get the Top 15 Words Per Topic

1. Print out the top 15 words associated with each topic.

2. Determine the label for each topic.

    * The labels are: Business, Entertainment, Politics, Sports, and Technology.


#### Assign the Topics and Labels to the News Summaries

1. Transform our DTM so we get an array that consists of our documents and number of topics.

2. Read the `bbc_news_articles.csv` file into a DataFrame.

3. Use the `add_topic_labels` function to add the topic and topic label to each news summary.

    * Complete the `topic_labels` dictionary by adding the label for each topic.

    * Get the dominant topic for each news summary and add the label to a new column.

    * Use the `map` function to add the topic label to the news summary based on the topic number.

    * Pass the DataFrame, the topic numbers (i.e, `topic_results`), and `topic_labels` dictionary to the function.

4. Display the first and last 20 rows of the updated DataFrame.

5. Answer the following question:
    * Did LDA do a good job at assigning the appropriate topic to the news summaries?


## Reference

Pariza, S. 2017. BBC News Summary. *Kaggle*. Available https://www.kaggle.com/datasets/pariza/bbc-news-summary [2023, October 25]. ([CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/)).

---

© 2023 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
