# Preprocessing Fungi

## Introduction

You will import a pickle file containing all 250 fungi images. After confirming that the images were loaded, you will resize, convert to float, and normalize all images in the set.

## Instructions

Use the Jupyter notebook in the `Unsolved` folder to complete the following steps:

1. Use the provided code to import the pickle file. Note that this pickle file is imported via url, and a little extra code is needed to properly import the data.

2. Check the size of the second image.

3. Get all the sizes into a list, then convert it to a set.

4. Display the set of sizes.

5. Practice resizing by converting the first image to 250 by 250.

6. Resize all images in the dataset to 250 by 250 using a `for` loop. A list comprehension can come in handy here.

7. View the pixel values of the first image by converting it to a NumPy array.

8. Convert all the values to floating point.

9. Normalize the pixel values by dividing them by the maximum value of 255.

10. Display the normalized pixel values from the first image to confirm that all values are between 0 and 1.

11. Export the preprocessed data into a new pickle file.

## Reference

Hajati, F. 2021. *DeFungi* [Dataset]. UCI Machine Learning Repository. Available: https://archive.ics.uci.edu/dataset/773/defungi [2023, December 5]. ([CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/legalcode))

---

&copy; 2024 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
