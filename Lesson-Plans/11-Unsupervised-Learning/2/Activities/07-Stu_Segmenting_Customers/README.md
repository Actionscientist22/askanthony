# Segmenting Customer Data

In this activity, you will use BIRCH, agglomerative clustering, and the K-means algorithm to segment a dataset on 5,000 credit card customers. You'll determine the optimal number of clusters for the balance limit and age of the customer. This will be your first attempt at comparing one machine learning algorithm over another.


## Instructions

1. Load the raw data into a pandas DataFrame.

2. Preprocess the data by completing the following steps:

    * Transform the "education" column with the `get_dummies` function.
    * Combine the `education_dummies` DataFrame with the `ccinfo_df` DataFrame.
    * Drop the original "education" column.
    * Transform the "marriage" column with the `encode_marriage()` function provided.
    * Scale the data by using the  `StandardScaler` and the `fit_transform` function on the "limit_bal", "bill_amt", and "pay_amt" columns from the DataFrame.
    * Replace the original numeric data from the "limit_bal", "bill_amt", and "pay_amt" columns with its scaled counterparts.

3. Use the elbow method to determine the optimal number of clusters.

4. Segment the data with K-means using the optimal number of clusters.

5. Cluster the data by using agglomerative clustering and BIRCH.

    * Using the optimal number of clusters found in Step 3, estimate clusters by using both `AgglomerativeClustering` and `BIRCH`. Save each of these models and their results for comparison.

6. Compare the cluster results from using K-means, agglomerative clustering, and BIRCH.  Make sure to do the following:

    * Create a DataFrame that is a copy of the original `customers_df` data.

    * Add all of the predicted labels (`kmeans_predictions`, `agglo_predictions`, and `birch_predictions`) as columns to this DataFrame.

    * For each algorithm, plot the clusters by using the "limit_bal" and "age" columns.

### Bonus

Loop through each clustering algorithm using an alternative metric to determine the optimal number of clusters. To do so, follow these steps:

1. Create three lists, or a dictionary or DataFrame, to contain the metrics to measure optimal clusters.

2. Using a `for` loop, cycle through a list of cluster counts, fitting each of the three clustering algorithms.

3. When fitting the clustering algorithms in the loop, estimate the [variance ratio criterion (Calinski-Harabasz index)`](https://scikit-learn.org/stable/modules/clustering.html#calinski-harabasz-index) and save that metric to your metrics lists in Step 1.

    > **Hint:** Code samples for these and other metrics can be found in scikit-learn documentation on [clustering performance evaluation](https://scikit-learn.org/stable/modules/clustering.html#clustering-performance-evaluation).

4. Output each of the three lists. If larger metric values indicate a better number of clusters, what cluster count is best? Does it vary by the algorithm selected?

## Reference

UCI Machine Learning. 2016. *Default of credit card clients dataset*. Kaggle. Available: https://www.kaggle.com/datasets/uciml/default-of-credit-card-clients-dataset [2023, September 25] ([CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/legalcode)). Note that this dataset has been modified for the purpose of this activity. You can access the modified data in the CSV file provided.

---

© 2023 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
