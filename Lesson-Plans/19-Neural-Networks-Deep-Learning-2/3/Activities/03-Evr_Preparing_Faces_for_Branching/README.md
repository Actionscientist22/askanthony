# Preparing Faces for Branching

## Introduction

In this activity, you will prepare the face images data for branched predictions on multiple columns.

## Instructions

Use the Jupyter notebook in the `Unsolved` folder to complete the following steps:

1. Import the data and images using the provided code.

2. Preprocess the images using the provided code. Make sure to read through and understand each step.

3. Display the first few rows of the file names DataFrame.

4. Create a new DataFrame for the `y` data by splitting the files column into four new columns.

5. Encode each column using tools from scikit-learn like OneHotEncoder and LabelEncoder.

6. Use pd.concat to combine all the `y` DataFrames into a new DataFrame.

7. Augment the images using the steps from previous activities.

8. Convert the `X` data into NumPy arrays.

9. Use list comprehensions to separate the `y` training data into separate variables for each classification task: userid, pose, expression, and eyes.

10. Repeat the process with the `y` testing data.

11. Create a dictionary to hold all the data variables and export the data as a pickle file for use in creating the model.

## References

Mitchel, T. 1999. *CMU face images* [Dataset]. UCI Machine Learning Repository. Available: https://archive.ics.uci.edu/dataset/124/cmu+face+images [2023, December 5]. ([CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/legalcode))

---

&copy; 2024 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
