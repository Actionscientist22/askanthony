# Resampling and Melting DataFrames

In this activity, you'll use the `resample` function to down sample time series data and the `melt` function to reshape a DataFrame from a wider form to longer form.

## Instructions

### Using the `resample` Function

1. Use the provided code to read in the `ufoSightings.csv` CSV file into a DataFrame, clean the data, convert the "date" column to a datetime object, and drop any "datetime" values that didn't get converted to a datetime object.

2. Use the provided code to create the `ufo_pivot` DataFrame.

3. Resample the `ufo_pivot` DataFrame into weekly bins and get the average duration in seconds for each week rounded to one decimal place. Then, sort the resampled pivot table in ascending order on the "duration (seconds)" column.

4. Resample the `ufo_pivot` DataFrame into monthly bins and get the average duration in seconds for each month rounded to one decimal place. Then, sort the resampled pivot table in ascending order on the "duration (seconds)" column.

5. Use the provided code to create the `ufo_pivot_sum` DataFrame.

6. Resample the `ufo_pivot_sum` DataFrame into weekly bins and get the total number of sightings for each week. Then, sort the resampled pivot table in ascending order on the "shape" column.

7.  Resample the `ufo_pivot_sum` DataFrame into monthly bins and get the total number of sightings for each month. Then, sort the resampled pivot table in ascending order on the "shape" column.

### Using the `melt` Function

1. Use the provided code to read in the `book_sales.csv` CSV file, create `book_sales_pivot` DataFrame, and reset the index.

2. Convert the `book_sales_reindexed` DataFrame from short form to long form by using the `melt` function.

3. Convert the `book_sales_reindexed` DataFrame from short form to long form and set the `id_vars` to the "book_name" variable.

4. Convert the `book_sales_reindexed` DataFrame from short form to long form and rename the columns by setting the `id_vars`, `var_name`, and `value_name` parameters to the desired columns.

5. Group the previous melted DataFrame on the "date" and show the total sales by the date.


---

© 2023 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
