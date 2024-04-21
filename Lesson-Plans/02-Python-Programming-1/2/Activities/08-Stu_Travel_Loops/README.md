# Travel Loops

## Introduction

In this activity, you'll practice writing loops to make changes to lists and print out their values.

## Instructions

Using the lists in the starter code, create loops that perform the following actions:

* Create a loop that performs the following actions three times:

    * Ask the user for a city and convert it to title case.

    * Append the city to the cities list.

* Create a `while` loop that will continue as long as the `cities_daily_cost` list is shorter than the `cities` list, and perform the following actions:

    * Get the length of `cities_daily_cost` to use as the index of `cities` to print the city value when asking the daily cost of that city.

    * Append the `cities_daily_cost` list with the user input, converted to an integer.

* Create a `for` loop to loop through the `cities_daily_cost` list and add 10 to each item in the list.

* Create a `for` loop to loop through both of the lists at the same time, since they're the same length. For each index value, print out the city and daily cost on the same line in the format `Daily cost of {city} is ${cost}`.

## Hints

* Use `len()` to check the length of the lists.

* Remember that you can update the value of a list by referencing it by its index in the format `list_name[index] = new_value`.

* `while` loops can accept the same types of conditionals as if-else statements, whereas `for` loops must be in the format `for iterator_variable in sequence_to_iterate`.

---

© 2023 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
