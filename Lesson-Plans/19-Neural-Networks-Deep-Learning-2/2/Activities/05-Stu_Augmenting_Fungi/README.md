# Augmenting Fungi

## Introduction

Using Pillow, NumPy, and Keras, you will apply the augmentation process to the entire fungi training dataset.

## Instructions

Use the Jupyter notebook in the `Unsolved` folder to complete the following steps:

1. Import the preprocessed data and split into training and testing sets using the provided code.

2. Create the ImageDataGenerator. Make sure to choose transformations that are appropriate for the data!

3. Create empty lists for both X and y augmentations.

4. Loop through all the images in the training data. Inside the loop, perform steps 5 through 8.

5. Select the original image and its y label.

6. Ensure that the input data has the correct shape; for these RGB images, you only need to add the batch dimension, not the channel dimension.

7. For every image, create five new images using the ImageDataGenerator.

8. Append each image and the label (from the original image) to the appropriate list.

9. After the loop, print the length of the lists containing the augmented images and labels to ensure they are the same length.

10. Lastly, use the provided code to export the split and augmented data to a pickle file inside a dictionary. You may have to modify the variable names to match the ones you chose in the previous steps.

## Reference

Hajati, F. 2021. *DeFungi* [Dataset]. UCI Machine Learning Repository. Available: https://archive.ics.uci.edu/dataset/773/defungi [2023, December 5]. ([CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/legalcode))

---

&copy; 2024 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
