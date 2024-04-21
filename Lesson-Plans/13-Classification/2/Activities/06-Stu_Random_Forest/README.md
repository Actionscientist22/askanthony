# Predicting Malware with Random Forest

## Introduction

You've trained logistic regression, SVM, KNN, and decision tree models with malware data. Now it's time to see how a random forest model performs with the data.

## Instructions

Use the Jupyter notebook in the `Unsolved` folder to complete the steps for this activity. The code for loading and splitting the data has been prepared for you.

1. Declare a `RandomForestClassifier()` model. Use the following settings: `n_estimators=128` and `random_state=78`

2. Fit the training data to the model, and save the model.

3. Evaluate the model by making predictions with the testing data to get the accuracy score.

4. Get the model's feature importances and list the top ten most important features.

5. Answer the following questions:

   * Would you trust this model to detect malware?

   * Out of the following models, which one had the highest accuracy score: logistic regression, SVM, KNN, decision tree, or random forest?

## Resources

[RandomForestClassifier()](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html)

## Reference

Mathur, A. 2022. *NATICUSdroid (Android permissions) dataset* [Dataset]. UCI Machine Learning Repository. Available: https://archive.ics.uci.edu/dataset/722/naticusdroid+android+permissions+dataset [2023, April 28]. ([CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/legalcode))

---

© 2023 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
