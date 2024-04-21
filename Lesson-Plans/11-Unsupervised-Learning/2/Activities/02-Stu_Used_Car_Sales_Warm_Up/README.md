# Clustering Used Car Sales

In this activity, you will use the K-means algorithm to identify trends within a dataset of used car sales.

## Instructions

1. Review the pandas DataFrame and elbow plot associated with `used-car-sales-data.csv` data.

2. Run the K-means algorithm identifying three clusters in the data. To do so, complete these steps:

   * Create and initialize the K-means model for three clusters. Use a `random_state` value of 1 for the model.

   * Fit, or train, the model by using the `used_car_sales_df` DataFrame.

   * Make predictions about the clustering by using the trained model. Save the predictions to a variable called `car_sales_segment_3`, and print that variable.

   * Create a copy of the DataFrame and name it `used_car_sales_predictions_df`.

   * Add a column to the `used_car_sales_predictions_df` DataFrame called "car_sales_segment_3", and add the `car_sales_segment_3` information to the column.

   * Plot the "selling_price" versus "km_driven" by using the DataFrame adjusted to include used car sales segment information for three clusters.

3. Run the K-means algorithm identifying four clusters in the data. To do so, complete these steps:

   * Create and initialize the K-means model for four clusters. Use a `random_state` value of 1 for the model.

   * Fit, or train, the model by using the `used_car_sales_df` DataFrame.

   * Make predictions about the clustering by using the trained model. Save the predictions to a variable called `car_sales_segment_4`, and print that variable.

   * Add a column to the `used_car_sales_predictions_df` DataFrame called "car_sales_segment_4", and add the `car_sales_segment_4` information to the column.

   * Plot the "selling_price" versus "km_driven" by using the DataFrame adjusted to include used car sales segment information for four clusters.

4. Is the data segmented better into three or four clusters? Why?

## Reference

Birla, N., Verma, N. & Kushwaha, N. 2023. *Vehicle dataset*. Kaggle. Available: https://www.kaggle.com/datasets/nehalbirla/vehicle-dataset-from-cardekho [2023, September 25] ([Database Contents License (DbCL)](https://opendatacommons.org/licenses/dbcl/1-0/)).

---

© 2023 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
