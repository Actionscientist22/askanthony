# Second Model

## Introduction

In this activity,you will re-attempt to fit a Random Forest model using the bank marketing data, but this time you will use balanced accuracy as a metric, test the model for overfitting, and attempt to tune the max_depth parameter in the logistic regression model to prevent over- and underfitting.

## Instructions

Use the Jupyter notebook in the `Unsolved` folder to complete the following steps:

1. Import and clean the data using the provided code.

2. Create a Random Forest model and train it with the X_train and y_train data.

3. Check the model's balanced accuracy on the testing data.

4. Check the model's balanced accuracy on the training data. Is the model overfit?

5. Using the provided values, create a loop to test several values of the max_depth parameter in a Random Forest model.

6. Create a DataFrame from the models dictionary using "max_depth" as the index.
6. Create a DataFrame from the models dictionary using "max_depth" as the index.

7. Plot the results. Does any particular max_depth value show a resistance to overfitting?
7. Plot the results. Does any particular max_depth value show a resistance to overfitting?

8. With any time remaining, attempt to create a better model. You can attempt to tune other parameters, you can use models other than Random Forest, and you can attempt any preprocessing steps you'd like. Remember, improvement is measured only with a balanced accuracy score!

## References

Moro, S., Rita, P. & Cortez, P. 2012. *Bank marketing* [Dataset]. UCI Machine Learning Repository. Available: https://archive.ics.uci.edu/dataset/222/bank+marketing [2023, October 17]. *Note that this data set has been modified/cleaned/shortened for the purpose of this activity. You can access the modified data in the CSV file provided.* ([CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/legalcode))

---

© 2023 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
