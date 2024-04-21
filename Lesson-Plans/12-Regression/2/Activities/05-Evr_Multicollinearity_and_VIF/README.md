# Detecting Multicollinearity Using VIF

## Introduction

In this activity, you will use automotive data to predict the price of a car. You will compare a model trained with columns selected using a VIF calculation to a model trained with all columns.

## Instructions

Use the starter code in the Jupyter notebook in the unsolved folder to complete the following steps:

1. Calculate VIF for the DataFrame by passing the X variable to the provided calc_vif function.

2. Investigate the contents of the engine-location column to determine why it returned a VIF of NaN.

3. Use value_counts to confirm the issue with the engine-location column.

4. Create another X variable named X_vif by dropping engine-location and the four columns with the highest VIF scores from the original X data.

5. Create and train two models using the two X variables.

6. Calculate the adjusted r-squared values for each model.

    * Which model performed better according to adjusted r-squared?

## References

Schlimmer, J. 1987. *Automobile* [Dataset]. UCI Machine Learning Repository. Available: https://archive.ics.uci.edu/dataset/10/automobile [2023, August 17]. ([CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/legalcode))

---

© 2023 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
