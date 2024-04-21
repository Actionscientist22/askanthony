# Build a CNN

## Introduction

You will use Keras to create and train a simple CNN.

## Instructions

Use the Jupyter notebook in the `Unsolved` folder to complete the following steps:

1. Use the provided code to import the X and y data, encode the y data, convert the X data to a NumPy array, and split the data into training and testing sets.

2. Build the CNN model using the sequential constructor from Keras along with `Conv2D` and `MaxPooling2D` layers. Use one of each to start, and make sure to set the "input_shape" correctly on the first `Conv2D` layer. Check the preprocessing activity from lesson 1 if you can't remember the dimensions of the images.

3. Compile the model using the `adam` optimizer, `sparse_categorical_crossentropy` for loss, and `accuracy` as the metric.

4. Use a batch size of 32 for 10 epochs to fit the model. Make sure to specify the validation data. If you receive an error, try to troubleshoot to see what needs fixed.

5. Examine the output; how did your model perform?

## Reference

Hajati, F. 2021. *DeFungi* [Dataset]. UCI Machine Learning Repository. Available: https://archive.ics.uci.edu/dataset/773/defungi [2023, December 5]. ([CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/legalcode))

---

&copy; 2024 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
