# Collect HTML Table Data

## Introduction

In this activity, you will use `read_html` from Pandas to scrape a Wikipedia article. You will then clean the resulting DataFrame and export it to a CSV.

## Instructions

1. Use the Pandas `read_html` method to parse the URL.

2. There are many tables on this Wikipedia page. Locate the "Tournament ranking" table and convert it to a DataFrame.

    **Hint:** It's in the 70–80 range.

    ![A screenshot of the first four rows of the "Tournament ranking" table from Wikipedia](https://static.bc-edx.com/ai/ail-v-1-0/m6/lesson_1/img/tournament-ranking-table.png)

3. Drop the NA rows from the DataFrame and reset the index.

4. Check the data types of the columns.

5. The "GD" column requires some cleaning before it can be converted to an integer data type. Note that the longer hyphen (`−`) from the original table is subtly different from the minus sign (`-`) that can be converted to an integer. The following changes should be made:

    * Remove the plus sign (`+`).

    * Replace the longer hyphen (`−`) with a minus sign (`-`).

6. Use a loop to convert the following columns to data type `int`: "Pos", "Pld", "W", "D", "L", "GF", "GA", "GD", "Pts".

7. Export the resulting DataFrame to a CSV file without the index.

---

© 2023 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
