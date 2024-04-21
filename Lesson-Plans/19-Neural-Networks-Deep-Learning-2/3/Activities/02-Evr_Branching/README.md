# Branching

## Introduction

You will use Keras to build a non-sequential model with multiple branched outputs.

## Instructions

Use the Jupyter notebook in the `Unsolved` folder to complete the following steps:

1. Import the data.

2. Create a OneHotEncoder for the quality column and transform it.

3. Create a label encoder for the color column and transform it.

4. Create a processed version of the DataFrame with the newly created `y` variables and drop the original quality and color columns.

5. Split the data into an `X` variable and two separate `y` variables.

6. Split all three variables into training and testing sets.

7. Create an input layer and two shared dense layers, making sure to name each layer and specify the preceding layer.

8. Create an output layer for the quality columns as a branch off the final shared dense layer. Make sure to use the correct number of neurons and the sigmoid activation function. Name the layer and specify the preceding layer.

9. Create an output layer for the color column as a branch off the final shared dense layer. Make sure to use the correct number of neurons and the sigmoid activation function. Name the layer and specify the preceding layer.

10. Build the model using the `Model` function.

11. Compile the model, specifying the loss and metric function for each output layer with dictionaries that specify the name of the layer as the key and the function as the key.

12. Fit the model. Use a dictionary to specify which `y` variable is associated with each output layer.

13. Evaluate the model using the testing data.

14. Print the accuracy of both the quality and color layers.

## Reference

Hajati, F. 2021. *DeFungi* [Dataset]. UCI Machine Learning Repository. Available: https://archive.ics.uci.edu/dataset/773/defungi [2023, December 5]. ([CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/legalcode))

---

&copy; 2024 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
