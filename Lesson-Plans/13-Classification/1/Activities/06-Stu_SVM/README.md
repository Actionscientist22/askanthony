# Predicting Malware with SVM

## Introduction

You've trained a logistic regression model with malware data. Now it's time to see if a Support Vector Machine (SVM) model can improve the accuracy.

## Instructions

Use the Jupyter notebook in the `Unsolved` folder to complete the steps for this activity, which are divided into the following stages:

1. Prepare the data.

2. Model and fit the data to an SVM.

3. Predict the testing labels and calculate the performance metrics.

#### Prepare the Data

1. Load the [app-data.csv](https://static.bc-edx.com/ai/ail-v-1-0/m13/lesson_1/datasets/app-data.csv) file into a Pandas DataFrame.

2. Note that you want to predict the `Result` variable.

3. Using the `app_data` DataFrame, separate the data into training and testing data. Start by defining the `y` (target) and `X` (features) of the data (all the columns except “Result”).

4. Split the features and target data into `X_train`, `X_test`, `y_train`, and `y_test` datasets by using the `train_test_split` function.

#### Model and Fit the Data to a Support Vector Machine

1. Declare a `SVC` model with a `kernel` value of `linear`.

2. Fit the training data to the model, and save the model.

3. Validate the model.

#### Predict the Testing Labels and Calculate the Performance Metrics

1. Make predictions about malware by using the testing dataset, and save those predictions.

2. Calculate the accuracy score by evaluating `y_test` vs. `testing_predictions`.

3. Answer the following question: For this dataset, how well did the model predict actual malware? Is the accuracy improved on the logistic regression model?

## Reference

Mathur, A. 2022. *NATICUSdroid (Android permissions) dataset* [Dataset]. UCI Machine Learning Repository. Available: https://archive.ics.uci.edu/dataset/722/naticusdroid+android+permissions+dataset [2023, April 28]. ([CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/legalcode))

---

© 2023 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
