# Finding the Best `k`

In this activity, you will use the elbow method to determine the optimal number of clusters that should be used to segment a dataset of stock pricing information. Once the elbow curve has been established, evaluate the two most likely values for `k` using the K-means algorithm and generate scatter plots for each value of `k`.

## Instructions

1. Read in the `stock_data.csv` file from the Resources folder and create a DataFrame. Set the “date” column to create the DatetimeIndex. Be sure to include parameters for `parse_dates` and `infer_datetime_format`.

2. Create two lists: one for the range of k-values (from 1 to 11) to analyze, and another to hold the list of inertia scores.

3. Use a `for` loop to evaluate each instance of k, define a K-means model, fit the K-means model based on the DataFrame, and append the model’s inertia to the empty inertia list that you created in the previous step.

4. Store the values for k and the inertia in a dictionary called `elbow_data`. Use `elbow_data` to create a pandas DataFrame called `df_elbow`.

5. Using pandas, plot the `df_elbow` DataFrame to visualize the elbow curve.

6. Next, perform the following tasks for each of the two most likely values of `k`:

   * Define a K-means model by using `k` to define the clusters, fit the model, make predictions, and add the prediction values to a copy of the scaled DataFrame named `spread_predictions_df`.

   * Plot the clusters. The x-axis should reflect the "hi_low_spread", and the y-axis should reflect the "volume".

7. Considering the plot, what’s the best number of clusters or value of k to choose?

---

© 2023 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
