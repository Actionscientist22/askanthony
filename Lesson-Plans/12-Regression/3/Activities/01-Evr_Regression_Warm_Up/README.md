# Everyone Do

## Introduction

In this activity you'll warm up your regression skills by applying adjusted r-squared using linear regression on rent pricing data.

## Instructions

Use the starter code in the Jupyter notebook in the `Unsolved` folder to complete the following steps:

1. Import the data and drop rows with missing values.

2. Create two X variables, one with all columns besides price and another with only the columns specified in the provided `select_features` variable.

3. Create the y variable from the price column.

4. Split the data into training and testing sets.

5. Create two models, and train them using the two X variables.

6. Make predictions using both models, then score them both using Mean Squared Error and R-Squared.

7. Using the provided r2_adj function, calculate the adjusted r-squared of both models.

8. Using the model with the highest adjusted r-squared value, calculate the mean and standard deviation of the output of the cross_val_score function.

## Reference

UC Irvine Machine Learning Repository. 2019. *Apartment for rent classified* [Dataset]. Available: https://archive.ics.uci.edu/dataset/555/apartment+for+rent+classified [2023, August 24]. ([CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/legalcode))

---

© 2023 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
