# Predict Liters Per 100km Using Multiple Linear Regression Demo

## Introduction

In this activity, you will view charts to make observations about the relationship between the features and target variable in a dataset, then select the features that have the best linear relationships to train your linear regression model.

## Instructions

Use the Jupyter notebook in the `Unsolved` folder to complete the following steps:

1. Load and visualize the car data.

2. Assign the two features that appear to have the most linear relationship with liters per 100km to the variable `X`. Assign the target column `L/100km` to the variable `y`.

    > **Note:** Scikit-learn requires a two-dimensional array of values so we use `reshape()` to create this.

3. Use the scikit-learn `train_test_split()` function to split the data into training and testing data.

4. Create the linear regression model.

5. Fit the model to the training data.

6. Use the `predict` method to create predicted values on the testing data.

7. Use the predicted values to evaluate the model's MSE and R<sup>2</sup> metrics with the `mean_squared_error` and `r2_score` functions.

8. Use the `score()` function to check the R<sup>2</sup>.

## Reference

Quinlan, R. 1993. *Auto MPG* [Dataset]. UCI Machine Learning Repository. Available: https://archive.ics.uci.edu/dataset/9/auto+mpg [2023, May 5]. ([CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/legalcode))

> **Note:** This dataset was converted into metric measurements.

---

© 2023 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
