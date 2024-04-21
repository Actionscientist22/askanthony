# Feature Selection With P-Values

## Introduction

In this activity, you will use apartment rent data to predict the price of a rental. You will use p-values from the OLS model in the statsmodels library to choose only the most relevant columns in a model's training, and you will compare the adjusted r-squared value to that of a model trained with all columns.

## Instructions

Use the starter code in the Jupyter notebook in the unsolved folder to complete the following steps:

1. Use the statsmodels package to create and fit a linear regression.

2. Create a variable to hold the p-values of all columns sorted in ascending order.

3. Use loc to filter to columns with p-values below 0.05, and show the index of the results.

4. Create an X variable with all features and another with only features that meet the 0.05 threshold.

    * Use the index from the previous cell to select columns.

5. Split the data into training and testing sets.

6. Create and fit two models using the different X variables.

7. Using the provided r2_adj function, compare the adjusted r-squared of the two models.

    * Which model performed better according to adjusted r-squared?

## Reference

UC Irvine Machine Learning Repository. 2019. *Apartment for rent classified* [Dataset]. Available: https://archive.ics.uci.edu/dataset/555/apartment+for+rent+classified [2023, August 24]. ([CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/legalcode))

---

© 2023 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
