# Predicting Malware with Logistic Regression

## Introduction

Nefarious actors constantly try to steal private information by infiltrating electronic devices through malware apps. Try logistic regression on this real-world problem and find out how it fares at identifying malware.

## Instructions

Use the Jupyter notebook in the `Unsolved` folder to complete the steps for this activity, which are divided into the following stages:

1. Prepare the data.

2. Split the data into training and testing sets.

3. Model and fit the data to a logistic regression.

4. Predict the testing labels.

5. Calculate the performance metrics.

#### Prepare the Data

1. Load the [app-data.csv](https://static.bc-edx.com/ai/ail-v-1-0/m13/lesson_1/datasets/app-data.csv) file into a Pandas DataFrame.

2. Note that you want to predict the `Result` variable. Answer the following question: Using `value_counts`, how many malware apps exist in this dataset?

#### Split the Data into Training and Testing Sets

1. Using the `app_data` DataFrame, separate the data into training and testing data. Start by defining the `y` (target) and `X` (features) of the data (all the columns except “Result”).

2. Split the features and target data into `X_train`, `X_test`, `y_train`, and `y_test` datasets by using the `train_test_split` function.

#### Model and Fit the Data to a Logistic Regression

1. Declare a `LogisticRegression` model.

2. Fit the training data to the model, and save the model.

3. Validate the model.

#### Predict the Testing Labels

1. Make predictions about malware by using the testing dataset, and save those predictions.

#### Calculate the Performance Metrics

1. Calculate the accuracy score by evaluating `y_test` vs. `testing_predictions`.

2. Answer the following question: For this dataset, how well did the model predict actual malware?

## Resources

[Logistic regression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html)

[train_test_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html)

[Accuracy score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html)

## Reference

Mathur, A. 2022. *NATICUSdroid (Android permissions) dataset* [Dataset]. UCI Machine Learning Repository. Available: https://archive.ics.uci.edu/dataset/722/naticusdroid+android+permissions+dataset [2023, April 28]. ([CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/legalcode))

---

© 2023 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
