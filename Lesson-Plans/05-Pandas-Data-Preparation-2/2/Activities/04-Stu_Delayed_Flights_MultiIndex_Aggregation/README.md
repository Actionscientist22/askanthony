# Airline Delays Multi-Index and Aggregations

In this activity, you will practice creating multiple indices and aggregations to gain insights into airline delays.


## Instructions

1. After reading in the delayed flight dataset, group the data on the airline carrier ("UniqueCarrier") and show the average time for delayed arrivals ("ArrDelay") for each.

2. Show the average time for delayed arrivals ("ArrDelay") and delayed departures ("DepDelay") for each carrier ("UniqueCarrier").

3. Show first and last 25 rows of the total number of flights that were diverted for each airline carrier ("UniqueCarrier") by day of the week.

4. Show the total and average number of flights that were diverted and canceled for each airline carrier ("UniqueCarrier") by day of the week.

5. Show the total and average number of flights that were diverted and canceled for each origin ("Origin") and destination ("Dest").

6. Show the total and average number of flights that were diverted and canceled for each airline carrier ("UniqueCarrier"), flight origin ("Origin"), and destination ("Dest") by day of the week.

7. Flatten the multi-index from the DataFrame in Step 6 so the column name is "Diverted_sum".

## Reference

Kaggle. 2021. *Airlines Delay*. Available. [https://www.kaggle.com/datasets/giovamata/airlinedelaycauses](https://www.kaggle.com/datasets/giovamata/airlinedelaycauses) [2023, September 11].

---

© 2023 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
