# Loop De Loop

## Introduction

In this activity, you will practice using nested loops and nested conditionals while storing information about an amusement park's rides and prices.

## Instructions

* Open the starter code and notice that two empty lists have been created: `rides` and `prices`.

* Create a continuous loop that exits when the user types the specific prompt `q`. Inside this loop, perform the following actions:

    * Ask the user for the name of a ride and append it to the `rides` list.

    * Create another continuous loop that will be used to check for a valid input. Inside this loop, perform the following actions:

        * Ask the user for the price of the ride they just input.

        * Check if the input can be converted to a float using `replace()` (see hint below) and `isdigit()`. If it can't, print an error and return to the start of the loop. If the input can be converted to a float, perform the following actions:

            * Check if the number is less than or equal to 15. If it is, convert the number to a float and append it to the `prices` list, then exit the loop using the `break` keyword. If it isn't, prompt the user to input a number that is less than or equal to 15.

    * Prompt the user to check if they want to continue adding rides or exit. If the user inputs `q`, exit the loop.

    * You may use the following pseudocode as a guide:

        ```python
        # Continuous loop until user chooses to exit
        #    Ask user what ride to add to the amusement park and append to rides list
        #    Continuous loop
        #        Ask user the price of the ride
        #        Conditional: If input can be converted to float
        #                         Conditional: If input is <= 15
        #                                          Convert input to float and append to prices list
        #                                          Exit loop
        #                                      Else
        #                                          Prompt user about condition
        #                     Else
        #                         Print an error
        #    Prompt the user to type 'q' to exit if they don't have another ride to add
        #    Conditional: If user input = 'q'
        #                     Exit loop 
        ```

## Bonus

If you have time, try this bonus problem to print out the values of the lists you created.

* Create a `for` loop that checks the length of the `rides` list to loop through the values of each item in both of the `rides` and `prices` lists.

* Inside this `for` loop, perform the following actions:

    * Create a Boolean variable called `discount` and set it to `False`.

    * Check if the value of the `prices` list is greater than $5. If it is, apply a 10% discount to the price, and set the `discount` variable to `True`.

    * Print the name of the ride and the associated price on the same line. The price should be formatted to two decimal places.

    * Check if the discount was applied. If it was, print out a notice about the 10% discount.

    * Print out a dash on the same line (`-`) 40 times.

* The output may be formatted as follows:

    ```text
    Rollercoaster costs $13.50 to ride.
    A discount of 10% is applied.
    ----------------------------------------
    Helicopter costs $3.50 to ride.
    ----------------------------------------
    ```

## Hint

* `.isdigit()` will only return True for strings that can be converted to positive integers. In order to test for strings that can be converted to floats, we need to check if the string contains a single `.`, and remove it from the string before checking `.isdigit()`. We can do this with the `replace()` method (see [documentation](https://docs.python.org/3/library/stdtypes.html?#str.replace)). `replace()` takes in 2-3 parameters: `replace(find_substring, replace_substring[,max_number_to_replace])`. To remove a single `.`, we would use `replace(".", "", 1)`.

---
© 2023 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
