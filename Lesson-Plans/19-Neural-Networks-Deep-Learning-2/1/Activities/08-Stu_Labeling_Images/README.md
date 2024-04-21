# Labeling Images

## Introduction

You will import a .csv file containing the file names of the 250 fungi images. Using pandas, you will manipulate the file names to extract the class labels for each image.

## Instructions

Use the Jupyter notebook in the `Unsolved` folder to complete the following steps:

1. Use the provided path to import the CSV file into a DataFrame and display the first few rows.

2. Using pandas str functions, remove the .jpg file extension and split the file names into three new columns: class, sample, and image. This can be done on one line or multiple; use whatever methods you are most comfortable with.

3. For our purposes, select the class column as y.

4. Export the y variable to a new pkl file.

## Reference

Hajati, F. 2021. *DeFungi* [Dataset]. UCI Machine Learning Repository. Available: https://archive.ics.uci.edu/dataset/773/defungi [2023, December 5]. ([CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/legalcode))

---

&copy; 2024 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
