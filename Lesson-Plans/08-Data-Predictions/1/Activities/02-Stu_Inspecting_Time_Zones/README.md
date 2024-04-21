# Inspecting Time Zones in Stock Data

In this activity, you will use pandas to explore and manipulate a time series dataset. You will read in the data, review the time zone, and convert the data to another time zone.

## Background

You have an internship opportunity at a stock-trading company in Berlin, Germany. You are excited about this opportunity to collaborate with a European company, so you accept the position.

This company wants to start offering investment opportunities in US companies that are disrupting the automotive industry. Your first project is to analyze Tesla Inc.’s stock. After retrieving the historical stock data, you realize that the prices are based on Chicago time. You need to change the time zone to that of Berlin. It’s time to put your `datetime` transformation skills into action!

## Instructions

1. Read the Tesla historical stock data from the CSV file into a DataFrame.

2. Use the pandas `head` function to inspect the data. Use the pandas `info` function to check the data types of each column.

3. Convert the “time” column to the `datetime` data type by using the pandas `to_datetime` function.

   **Hint:** Because the “time” column contains UTC `Timestamp` data, remember to set `utc=True`.

4. Use the pandas `head` and `info` functions to verify both the data type transformation and the time zone.

5. Convert the time zone to that of Berlin (`Europe/Berlin`), and then verify the time zone transformation by using the pandas `head` and `info` functions.

---

© 2023 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
