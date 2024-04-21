# Branching Faces

## Introduction

You will use Keras to build a model to predict all of the classes in the faces dataset.

## Instructions

Use the Jupyter notebook in the `Unsolved` folder to complete the following steps, which are broken into these parts:

### Part 1: Import the Data

1. Use the provided code to import the preprocessed data and split it into individual variables.

### Part 2: Build the Model

#### Shared Layers (Common Across All Tasks)

1. First, we build the input layer using layers.Input.

2. The second layer should be a `Conv2D` layer. Build it off the input layer using the parenthetical syntax.

3. The third layer should be a `MaxPooling2D` layer built off the second layer.

4. The fourth layer should be a `Conv2D` layer built off the third layer.

5. The fifth layer should be a `MaxPooling2D` layer built off the fourth layer.

6. The sixth layer should be a `Conv2D` layer built off the fifth layer.

7. The seventh layer should be a `Flatten` layer built off the sixth layer.

8. Lastly, build one `dense` layer before branching to the different `y` branches.

#### Branched Output Layers

For each of the `y` variables, perform the following steps.

1. Create a standard dense layer connected to the last layer in the shared section.

2. Create an output dense layer. Make sure to give it the appropriate number of neurons and the appropriate activation function.

#### Train the Model

1. Assemble the model with the `Model` function. Make sure to name each output layer in a list passed to the outputs parameter.

2. Compile the model. Make sure to pass the name of each output layer in a dictionary to the loss and metrics parameter. Use either categorical or binary crossentropy for the losses, and use accuracy for the metrics.

3. Fit the model. Make sure to pass a dictionary naming each output layer and the `y` training data associated with it.

#### Evaluate the Results

1. Use the provided code to evaluate the model with the testing data and print the results.

2. Discuss the results with your class: Which results match what you expected? Which were surprising? How would this model perform on pictures that were not a part of this dataset? Would some of the output layers perform better than others? What could we do to improve the model?

## Reference

Mitchel, T. 1999. *CMU face images* [Dataset]. UCI Machine Learning Repository. Available: https://archive.ics.uci.edu/dataset/124/cmu+face+images [2023, December 5]. ([CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/legalcode))

---

&copy; 2024 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
