# Spending Beyond Our K-Means

In this activity, you’ll cluster the data into two different customer shopping segments and determine which segment reveals any relevant differences in customer shopping habits.


## Instructions

Use the Jupyter notebook in the `Unsolved` folder to complete the following steps:

1. Read in the `customer-shopping-scaled.csv` file from the Resources folder and create the DataFrame. Review the resulting DataFrame. Additionally, check for null values and the data types associated with the DataFrame.

2. Use the `encodeMethod` function that sets the `purchase` variable to 1 for "HotelRestCafe" (hotel/restaurant/cafe) purchases, and 2 for "retail" purchases.

3. Edit the "Method" column in the DataFrame by applying the `encodeMethod` function, then review the DataFrame. Confirm that the "Method" column consists of 1s and 2s.

4. Using this encoded DataFrame, initialize two K-means models: one with two clusters and another with three. For each model, follow these steps to identify the clusters and assign them to the data:

    * Initialize the `KMeans` model instance.
    * Fit the model.
    * Predict the model segments (clusters).

5. Once the models have been run, create a copy of the original DataFrame and name it `customer_predictions`. Next, add each of the customer segments to the `customer_predictions` DataFrame as new columns.

6. Using pandas’ `plot`, create scatter plots for the two customer segments.

7. Do you note any relevant differences between the two K-Means models?



## Reference

Cardoso, M. 2014. *Wholesale customers*. UCI Machine Learning Repository. Available:  https://archive.ics.uci.edu/dataset/292/wholesale+customers [2023, September 25] ([CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/legalcode)).

---

© 2023 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
