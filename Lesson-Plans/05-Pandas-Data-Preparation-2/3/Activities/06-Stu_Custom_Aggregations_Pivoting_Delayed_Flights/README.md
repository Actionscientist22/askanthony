# Pivoting Custom Aggregations Delayed Flights

In this activity, you will reshape data and apply custom functions for aggregations to gain insights into airline flight delays.


## Instructions

1. Read in the delayed flight dataset into a DataFrame named `delayed_flights_df`.

2. Create a custom function that will calculate an average of values from a DataFrame column.

3. Using the average custom function on the `delayed_flights_df` DataFrame, create a pivot table that shows the largest average arrival delay for each carrier, day of the month, and day of the week. Then answer the following questions:
    * Which airline carrier had the largest average arrival delay?
    * What day of the month and day of the week has the largest average arrival delay for the carrier?

4. Using the average custom function on the `delayed_flights_df` DataFrame, show the average time for delayed arrivals ("ArrDelay") and delayed departures ("DepDelay") for each airline carrier, day of the month, and day of the week. Then answer the following questions:
    * Which airline carrier had the largest and smallest average arrival and departure delays?
    * What day of the month and day of the week has the largest and smallest average arrival and departure delays for the carrier?

5. Create a custom function that will calculate the total of a DataFrame column.

6. Using the total custom function on the `delayed_flights_df` DataFrame, create a pivot table that shows the total and average number of flights that were diverted for each carrier, their origin, and their destination. Then answer the following questions:
    * Which airline carrier had the largest average and largest number of diverted flights?
    * What origin and destination had the largest average and largest number of diverted flights?

## Hint

* Use the [IATA Airline And Airport Code Search](https://www.iata.org/en/publications/directories/code-search/) to find the airline name.

## Reference

Kaggle. 2021. *Airlines Delay*. Available: [https://www.kaggle.com/datasets/giovamata/airlinedelaycauses](https://www.kaggle.com/datasets/giovamata/airlinedelaycauses) [2023, September 11].


---

© 2023 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
