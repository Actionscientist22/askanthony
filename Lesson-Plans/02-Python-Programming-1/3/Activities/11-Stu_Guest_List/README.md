# List Comprehensions

## Introduction

In this activity, you’ll practice extracting data from dictionaries and use list comprehensions to determine the number of guests attending an event.

## Instructions

* Open the file called `guest_list.py`. You will notice the provided starter code includes the script to input the guest name as well as the number of adults and children in that guest's party. The inputs are stored in a list of dictionaries.

* Run the provided program and try out some inputs. At the end of the script, it will print out the information you provided.

* Using list comprehension format and the `guests` list of dictionaries, generate and print out the following results:

  * A list of tuples with the guests for each party of guests in the format `(adults, children)`

  * The total number of adult guests

  * The total number of child guests

  * The total number of all guests

## Bonus

* Use a list comprehension to generate a string for each guest in the following format: `guest_name_converted_to_title_case: party of total_number_of_guests_in_party`

* Use a `for` loop to print out the string for each guest.

**Note:** We convert the guest name to title case because there is nothing that requires you to write the name properly in title case&mdash;for example, as "Jane" instead of "jAnE".

## Hints

* Recall the `sum()` list function.

---

© 2023 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
