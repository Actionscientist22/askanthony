# Concatenate Country Products

In this activity, you will practice concatenating DataFrames and appending their data to a combined DataFrame.

## Instructions

1. Import the pandas and pathlib libraries.

2. Create variables to import the [CSV files](Unsolved/Resources/) using the pathlib library.

3. Read the `uk_products.csv`, `france_products.csv`, `netherlands_products.csv`, `products.csv`, and `customer_info.csv` datasets into pandas DataFrames, with the `index_col` parameter set to the "CustomerID" column.

4. Display the first five rows of the France, UK, and Netherlands DataFrames.

5. Concatenate the France, UK, and Netherlands DataFrames using the `concat` function, with the `axis` parameter set to "rows" and the `join` parameter set to "inner", and display the results.

6. Repeat Step 5, but add the countries; `["France", "United Kingdom", "Netherlands"]` to the `keys` parameter. Then, drop the `Country` column from the concatenated DataFrame, and display the results.

7. Display the first five rows of the customer and products DataFrames.

8. Concatenate the customer and products DataFrames using the `concat` function, with the `axis` parameter set to "columns" and the `join` parameter set to "inner", and display the results.


---

© 2023 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
