# Augmenting One Image

## Introduction

You will use the ImageDataGenerator to create modified clones of a single image.

## Instructions

Use the Jupyter notebook in the `Unsolved` folder to complete the following steps:

1. Resize the image to 250 by 250.

2. Convert the pixel values to floating point and normalize them by dividing by 255.

3. View the shape of the array.

4. Add the batch dimension. Note that for a grayscale image, we would also need to add the channel dimension. Since this image is RGB, it already has the channel dimension as is evidenced by the 3 in the image shape.

5. Create an ImageDataGenerator with whatever settings you'd like.

6. Create a new image based on the original image.

7. View the shape of the new image.

8. Using matplotlib, display the new image. Note that because this image is RGB, we can simply multiply the image by 255 to undo the normalization and pass the entire result to the `imshow` function from matplotlib. Be sure to convert the array to `uint8` before plotting.

9. Plot the original image for comparison. Since we added a batch dimension, plot using only the first item of the first dimension, then all the values from the other three dimensions using this syntax: [0, :, :, :]. Make sure to multiply by 255 and convert to `uint8` before plotting.

## Reference

Hajati, F. 2021. *DeFungi* [Dataset]. UCI Machine Learning Repository. Available: https://archive.ics.uci.edu/dataset/773/defungi [2023, December 5]. ([CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/legalcode))

---

&copy; 2024 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
