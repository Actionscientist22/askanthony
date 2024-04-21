# Data Preprocessing

## Introduction

You have been provided with a dataset about rental properties in the United States. The real estate company you work for would like to use this dataset to create a machine learning model that can make recommendations about rental prices. Before the model can be trained, this data must undergo preprocessing so that all of the necessary features are numerical values. Once the data is encoded, you will split it into training and testing sets.

## Instructions

Use the Jupyter notebook in the `Unsolved` folder to complete the following steps:

1. Load Pandas and the dataset.

2. Check the data types of the columns in `rent_data`.

3. Drop the following columns from the dataset: `"id"`, `"title"`, `"body"`, `"currency"`, `"price_display"`, and `"address"`.

4. The amenities column may contain multiple amenities, separated by a comma. Each amenity should have its own column with binary values where 0 means the property does not have the amenity and 1 means that it does.

   Review and run the provided code to perform these actions. This code has been provided to you because it has not been covered previously, but may be useful if you encounter other datasets that are stored this way.

5. There will now be eight features remaining that are stored as strings: `"category"`, `"fee"`, `"has_photo"`, `"pets_allowed"`, `"price_type"`, `"cityname"`, `"state"`, and `"source"`. Practice one or more of the following encoding methods on these columns:

    * Pandas' `get_dummies()` function.

    * Pandas' `.astype("category").cat.codes` method.

    * Scikit-learn's `OneHotEncoder`.

    * Scikit-learn's `LabelEncoder`.

6. Choose one of the encoded datasets to create your features `X` and target `y`, where "price" is the target variable. When creating your features set `X`, drop the target variable and a few other features you don't want to include.

7. Split your `X` and `y` into training and testing sets using scikit-learn's `train_test_split()`.

8. Preview `X_train`, `X_test`, `y_train`, and `y_test`.

## Reference

UC Irvine Machine Learning Repository. 2019. *Apartment for rent classified* [Dataset]. Available: https://archive.ics.uci.edu/dataset/555/apartment+for+rent+classified [2023, August 24]. ([CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/legalcode))

---

© 2023 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
