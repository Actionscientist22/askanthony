# Similarity Search Engine

In this activity, you will use a pre-trained sentence-transformer LLM to determine the category of a random news headline by using similarity measures on the vector embeddings of a random news headline and the embeddings of known headlines.

## Instructions

1. Import the dependencies and use the `SentenceTransformer('all-MiniLM-L6-v2')` model.

2. Read the `news_headlines.csv` file into a DataFrame.

3. Convert the "headline" column to a list.

4. Convert each headline list to vector embeddings.

5. Convert the provided news headline, "Top 10 Hacks for Traveling Like a Pro." to vector embeddings.

6. Create a list to store tuples consisting of the news headline and similarity score.

7. Create a `for` loop that will do the following:

    * Iterate through the headline embeddings.

    * Calculate the cosine similarity score between each headline embedding and the new headline embedding.

        * **Note:** The code is provided for you.

    * Append the news headline and similarity score to the list.

8. Sort the list on the similarity score in descending order.

    * **Note:** The code is provided for you.

9. Create a `for` loop that will do the following:

    * Iterate through the similarities list

    * Get the category of the news headline from the DataFrame.

        * **Note:** The code is provided for you.

    * Print the rank, category, the news headline, and similarity score.


10. Answer the following questions.

    * **Question 1:** What category is the new headline?

    * **Question 2:** Why did you choose this category?

---

© 2023 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
