# Smooth Operator

## Introduction

In this activity, you will practice writing complex conditional statements with comparison, logical, membership, and identity operators.

## Instructions

Using the declared variables, lists, and inputs in the starter code, write conditional statements that do the following:

* Check if `days` is a number using `isdigit()` and convert it to an integer if it is. Print an error message if the condition is not met.

* Check if `days` and `budget` are integers using the `type()` function. If they are, calculate the daily budget and save it to a variable. Print an error message if the condition is not met.

* Check if the `city_to_visit` input is in the `cities` list. 

    * If the condition is met, find the index of that city from the `cities` list and use it to find the daily cost from the `cities_daily_cost` list. Save this daily cost to a variable called `city_daily_cost`.

    * If the condition is not met, set the `city_daily_cost` variable to 0. This will be used for error-checking in the next conditional.

* Check if `city_daily_cost` is greater than 0 `and` equal to or less than the daily budget.

    * If this condition is met, tell the traveler they can afford the vacation.

* Use `elif` to check if `city_daily_cost` is greater than 0 `and` greater than the daily budget.

    * If this condition is met, calculate and print out how much more per day the traveler needs.

* If the previous two conditions are not met, print an error message.

---

© 2023 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
