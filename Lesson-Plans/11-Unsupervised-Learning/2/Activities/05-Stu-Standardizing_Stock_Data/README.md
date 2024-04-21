# Standardizing Stock Data

In this activity, you will standardize stock data and use the K-means algorithm to cluster the data.

## Instructions

1. Read in the `stock_data.csv` file from the `Resources` folder and create the DataFrame. Make sure to set the "Ticker" column as the DataFrame’s index. Then, review the DataFrame.

2. To preprocess the data, use the `StandardScaler()` function and the `fit_transform` function to scale all the columns containing numerical values. Review a five-row sample of the scaled data using bracket notation ([0:5]).

3. Create a new DataFrame called `df_stocks_scaled` that contains the scaled data. Make sure to do the following:

   * Use the same labels that were referenced in the `StandardScaler` for the column names.

   * Set the index for the new DataFrame to the "Ticker" column of the original DataFrame.

   * Review the scaled DataFrame.

4. Encode the "Sector" column using `pd.get_dummies`, and save the result in a separate DataFrame called `sector_encoded_df`.

5. Using the `pd.concat` function, concatenate the `df_stocks_scaled` DataFrame with the `sector_encoded_df` DataFrame along the column axis. Review the concatenated DataFrame.

6. Using the concatenated DataFrame, cluster the data by using the K-means algorithm and a k value of 3. Create a copy of the concatenated DataFrame, and add the resulting list of company segment values as a new column.

## Reference

Brown, M. 2014. *Dow Jones Index*. UCI Machine Learning Repository. Available:  https://archive.ics.uci.edu/dataset/312/dow+jones+index [2023, September 25] ([CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/legalcode)).

—--

© 2023 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
