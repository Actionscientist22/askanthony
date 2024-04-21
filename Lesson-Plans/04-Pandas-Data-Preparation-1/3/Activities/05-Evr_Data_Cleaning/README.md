# Spring Cleaning

For this activity, use Pandas to clean stock portfolio data to get it fit for use.

## Instructions

Using the starter file and the stock data CSV, complete the following steps.

1. Load CSV data into Pandas using `read_csv`.

2. Identify the number of rows and columns in the DataFrame, otherwise known as its shape/structure.

3. Generate a sample of the data to visually ensure data has been loaded in correctly.

4. Identify the number of records in the DataFrame, and compare it with the number of rows in the original file.

5. Identify null records by calculating average percent of nulls for each Series. **Hint:** This step will require the `mean` function.

6. Drop null records.

7. Validate all nulls have been dropped by calculating the `sum` of values that are null.

8. Default null `ebitda` values to 0.

9. Check that there are no null `ebitda` values using the `sum` function.

10. Remove duplicate rows.

11. Now that nulls and duplicates have been wrangled, clean up the data a little more by removing the `$` currency symbols from the `price` field.

12. Use the `astype` function to cast `price` to a `float`.

## Hint

Pandas offers a `replace` function that can be executed against a Series. Documentation can be found [here](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.replace.html).

---

© 2023 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
