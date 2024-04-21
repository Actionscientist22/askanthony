# Predicting Article Objectivity

## Introduction

In this activity, you'll train a deep learning model to predict the objectivity of sports articles. The goal is to create a model that improves the accuracy when compared to supervised learning models.

## Instructions

* Upload the starter notebook to Google Colab and run the code to do the following:

  * Import the dependencies and load the dataset.

  * Separate the objectivity **Label** target from the other features in the dataset.

  * Split the features and target into training and test datasets.

  * Preprocess the input data accordingly:

    * Use Scikit-learn's **LabelEncoder** module to preprocess categorical data for the target variable.

    * Use Scikit-learn's **StandardScaler** module to preprocess numerical data.

* Define a deep learning model with the following features:

  * A first Dense layer with five neurons and the "tanh" activation function

  * A second Dense layer with at least three neurons and the "tanh" activation function

  * A third Dense layer with at least nine neurons and the "tanh" activation function

  * A fourth Dense layer with at least three neurons and the "ReLU" activation function

  * An output layer with one neuron and the "sigmoid" activation function

* Compile and train the model across no more than 100 epochs.

* Evaluate the performance of the deep learning model by calculating the test loss and predictive accuracy.

* Make predictions with the model and prepare a classification report with Scikit-learn's **classification_report** function.

* Compare the accuracy score and classification report results with those provided in `compare_results/objectivity_supervised_learning_results.ipynb` for trained supervised learning models.

  * Does the neural network perform better? If not, try to adjust the neurons in your Dense layers to improve the results.

* Save the model.

* Load the saved model.

* Evaluate the loaded model.

## Reference

Rizk,Y. & Awad, M. 2018. *Sports articles for objectivity analysis* [Dataset]. UCI Machine Learning Repository. Available: https://archive.ics.uci.edu/dataset/450/sports+articles+for+objectivity+analysis [2023, September 27]. ([CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/legalcode))

---

© 2023 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
