# Building a CNN From Scratch

## Introduction

Using Pillow, NumPy, and Keras, you will code the entire process of building a CNN. This includes importing images and metadata, preprocessing the images, labeling the data, augmenting the data, and creating the CNN model. 

## Instructions

Use the Jupyter notebook in the `Unsolved` folder to complete the following steps, which are broken into five parts:

### Part 1: Importing Data

1. Use the provided code to import all the images.

2. Print a random image from the list to ensure the import was successful.

### Part 2: Preprocessing

1. Check the size of the second image.

2. Get all the sizes into a list, then convert to a set.

3. Use a `for` loop to resize all images to 64 by 60.

4. Verify the resizing of all images by getting all the sizes into a list, then convert to a set.

5. Convert all images to floating point.

6. Normalize the images by dividing by 255.

### Part 3: Labels

1. Print the first few image file names; for this activity, focus on predicting the `userid` of each image.

2. Remove the .png file extension, then split into four new columns.

3. Create a new variable X to hold the normalized images and a new variable y to hold the `userid` column.

4. Convert the y variable to a NumPy array.

5. Split the data into training and testing sets.

### Part 4: Augmentation

1. Create an ImageDataGenerator. Make sure to select the transformations that are appropriate for the images in the dataset.

2. Create lists to hold the X and y training data.

3. Loop through all the images. For each image, perform steps 4 through 10.

4. Select the image.

5. Select the label of the image.

6. Add the channel dimension.

7. Add the batch dimension.

8. Add five images for every original image.

9. Append each new image to the X list created earlier.

10. For each appended image, also append the original label to the y list.

11. After the loop, print the lengths of each list to ensure they match.

12. Reshape the testing data to prepare for training by looping through the testing data and adding the channel dimension to every image.

13. Ensure the X testing data is stored as a NumPy array.

### Part 5: Creating the Model

1. One-hot-encode the y data. Ensure that `sparse_ouput` is set to “False” and `handle_unknown` is set to "ignore."

2. Confirm that all training and testing variables are converted to NumPy arrays.

3. Split the training data into training and validation datasets. This will leave an additional testing dataset for evaluation after the model is fully trained.

4. Check the shape of the one-hot-encoded y data to confirm how many neurons the output layer will need.

5. Define the CNN model. It should have three `Conv2D` layers, two `MaxPooling2D` layers, a flatten layer, a dense layer, and another dense output layer.

6. Compile the model.

7. Train the model.

8. Evaluate the model using the testing data.

## Reference

Mitchel, T. 1999. *CMU face images* [Dataset]. UCI Machine Learning Repository. Available: https://archive.ics.uci.edu/dataset/124/cmu+face+images [2023, December 5]. ([CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/legalcode))

---

&copy; 2024 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
