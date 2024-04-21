# Segmenting with PCA

In this activity, you will use your knowledge of principal component analysis (PCA) to reduce the dimensionality of a customer base dataset. The data has already been segmented based on all of the factors. Use PCA to determine if reducing the dimensionality will improve the results compared to the original DataFrame, then determine which features have the strongest influence on the principal components.

## Instructions

1. Reduce the dimensionality of the original `customers_transformed_df` DataFrame to two principal components using the following steps:

    * Import the PCA module from `scikit-learn`.

    * Instantiate the instance of the PCA model by declaring the number of principal components as two.

    * Using the `fit_transform` function from PCA, fit the PCA model to the `customers_transformed_df` DataFrame. Review the first five rows of list data.

2. Using the `explained_variance_ratio_` function from PCA, calculate the percentage of the total variance that is captured by the two PCA variables and answer the following question:

    * What is the explained variance ratio captured by the two PCA variables?

3. Using the `customer_pca` data, create a pandas DataFrame called `customers_pca_df`. The columns of the DataFrame should be called "PCA1" and "PCA2".

4. Using the `customers_pca_df` DataFrame, apply the elbow method to determine the optimal value of k.

5. Segment the `customers_pca_df` DataFrame using the K-means algorithm and the optimal value for k defined in Step 2, and create a scatter plot of components and customer segments.

6. Segment the original `customers_transformed_df` DataFrame with all factors by using the K-means algorithm, and create a scatter plot of any two features and customer segments.

7. Determine which features have the strongest or weakest influence on each principal component.

8. Create a scatter plot of the most influential features for each component and customer segments.

9. What is the difference between the segmentation results of the PCA DataFrame and the most influential features for each component?

## Reference

The original data is from *Kaggle*. 2023. Available [https://www.kaggle.com/](https://www.kaggle.com/)([CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/legalcode)). Note that this dataset has been modified for the purpose of this activity.

---

© 2023 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
