# Energize Your Stock Clustering

In this activity, the students will use the K-means algorithm and clustering optimization techniques to cluster stocks to determine a portfolio investment strategy.

## Instructions

1. Run the code that creates a DataFrame from the `stock_data.csv` file.

2. Run the code that scales the `df_stocks` DataFrame and creates a new DataFrame that contains both the scaled and encoded data.

3. Initialize the K-means model with three clusters and then fit the `df_stocks_scaled` DataFrame to the model.

4. Predict the clusters and then create a new DataFrame with the predicted clusters.

5. Create a scatter plot to visualize the "StockCluster" using "MeanOpen" as the x-variable and "MeanPercentReturn" as the y-variable.

6. Now, reduce the number of features to two principal components on the `df_stocks_scaled` DataFrame, and calculate the explained variance ratio that results from the principal component analysis (PCA) data.

7. Use the calculated PCA DataFrame from Step 6 to create a new DataFrame called `df_stocks_pca`, and then add an additional column to the `df_stocks_pca` DataFrame that contains the tickers from the original `df_stocks` DataFrame.

8. Rerun the K-means algorithm on the `df_stocks_pca` DataFrame and create a scatter plot using the "StockCluster" and the two principal components for the x- and y-axes, then answer the following question.

    * After visually analyzing the cluster analysis results, what is the impact of using fewer features to cluster the data using K-Means?


9. Determine which features have the strongest or weakest influence on each principal component, and provide your answer.

10. Create a scatter plot of the most influential features for each principal component and stock cluster.

11. Answer the following question:

    * What is the difference between the segmentation results of the PCA DataFrame and most influential features for each component?


## Reference

Brown, M. 2014. *Dow Jones Index*. UCI Machine Learning Repository. Available:  https://archive.ics.uci.edu/dataset/312/dow+jones+index [2023, September 25] ([CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/legalcode)).

—--

© 2023 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
