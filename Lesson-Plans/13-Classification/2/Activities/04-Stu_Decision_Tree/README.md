# Predicting Malware with Decision Trees

## Introduction

You've trained logistic regression, SVM, and KNN models with malware data. Now it's time to see how a decision tree model performs with the data.

## Instructions

Use the Jupyter notebook in the `Unsolved` folder to complete the steps for this activity. The code for loading and splitting the data has been prepared for you.

1. Declare a `tree.DecisionTreeClassifier()` model.

2. Fit the scaled training data to the model, and save the model.

3. Evaluate the model by making predictions with the scaled testing data to get the accuracy score.

4. Visualize the decision tree with a `max_depth` of `5`.

   * **Note:** If you were unable to install `pydotplus` locally, you should perform this task in Google Colab.

5. Save the decision tree visualization as PDF and PNG.

## Exporting Images from Google Colab

If you’re using Colab, you can open up the “Files” menu (the icon that looks like a folder located to the left of your notebook, identified as step 1 in the following image) and find the image file(s) there. To download the images locally, hover your mouse cursor over the filename and click the three dots menu (identified as step 2 in the following image).

![A screenshot of the Files menu in Google Colab indicates the three dots menu for an individual file.](https://static.bc-edx.com/ai/ail-v-1-0/m13/lesson_2/img/colab-files-menu.png)

From the menu that opens, click the “Download” option.

![A screenshot of the Download option for a file in Google Colab.](https://static.bc-edx.com/ai/ail-v-1-0/m13/lesson_2/img/colab-files-download.png)

## Resources

[DecisionTreeClassifier()](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html)

[export_graphviz()](https://scikit-learn.org/stable/modules/generated/sklearn.tree.export_graphviz.html)

## Reference

Mathur, A. 2022. *NATICUSdroid (Android permissions) dataset* [Dataset]. UCI Machine Learning Repository. Available: https://archive.ics.uci.edu/dataset/722/naticusdroid+android+permissions+dataset [2023, April 28]. ([CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/legalcode))

---

© 2023 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
