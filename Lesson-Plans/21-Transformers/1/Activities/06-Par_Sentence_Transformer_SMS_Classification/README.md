# SMS Text Classification

In this activity, you will use a pre-trained sentence-transformer LLM to determine the classification of SMS text messages. First, while working in pairs, use the 'all-MiniLM-L6-v2' model from SentenceTransformer to encode both labeled SMS text messages and unclassified SMS texts. Then, implement a cosine similarity calculation to identify the top 5 similar classified SMS text messages for each unclassified SMS text message.

## Instructions

1. Import the dependencies and use the `SentenceTransformer('all-MiniLM-L6-v2')` model.

2. Read the `SMS_Ham_Spam.csv` file into a DataFrame and check the data for null values.

3. Read the `unclassified_text_messages.csv` file into a DataFrame and check the data for null values.

### Pre-process the Data and Get Vector Embeddings.

1. For each DataFrame, convert the "text_message" column to a list.

2. Convert each text message list to vector embeddings.

### Get the Top Five Cosine Similarities For Each Unclassified Text Message

1. Create two lists. The first list, `unclassified_similarities`, will store tuples consisting of the unclassified message and the top five similarity scores. The second list, `classified_similarities`, will store tuples consisting of the classified text message and their similarity scores.

2. Create a nested `for` loop. The first `for` loop will iterate through each unclassified message and unclassified embedding created in the pre-process steps.

3. For each iteration, the second `for` loop:

    * Iterate through each classified message and classified embedding created in the pre-process steps.

    * Calculate the cosine similarity between each unclassified embedding and every classified embedding generated from the classified text messages.

        * **Note:** The code is provided for you.

    * Append the classified text message and the cosine similarity score to the `classified_similarities` list.

4. Sort the list of tuples in the `classified_similarities` list on the similarity score in descending order.

    * **Note:** The code is provided for you.

5. Use list slicing to get the top five similarity scores from the `classified_similarities` list.

6. Append the unclassified text message and the top five similarity scores to the `unclassified_similarities` list.

### Determine the Classification of Each Unclassified Text Message.

1. Create a nested `for` loop. The first `for` loop will iterate through the `unclassified_similarities` list and print the unclassified text message.

2. For each iteration, the second `for` loop:

    * Iterate through the top five similarities list and get the classified text message and the similarity score.

    * Using the classified text message string for each iteration, retrieve the classified text message label (ham or spam) from the DataFrame.

    * Print the rank, label, classified text message, and similarity score.

### Answer the following questions.

1. Did the similarity scores for the "unclassified" text messages agree with the label given in the CSV file? Why or why not?

2. What other method would you use to confirm the classification of the text messages?


## Reference

Tiago, A., & Hidalgo, J. 2012. SMS spam collection. *UCI Machine Learning Repository*. Available https://archive.ics.uci.edu/dataset/228/sms+spam+collection [2023, October 25]. ([CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/legalcode)).


---

© 2023 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
