# Returned Goods

In this activity, you’ll create a function that automatically determines insurance payouts each week.

## Background

You've started a new company with an innovative idea: an insurance offering for e-retailing firms that face risk of product returns. If a merchant experiences a return rate that's higher than their seasonal average for that product, your firm pays out a moderate amount to them.

Your task is to automate part of this process. You'll create a function that automatically determines the firm's weekly total insurance payouts.

## Instructions

Open the [returned_goods.py](Unsolved/returned_goods.py) file and complete the following steps:

* Define a new function called `process_claims`. This function should accept a variable `claims`, which is a list of all new claims for that week.

* In the first line of the function, create a variable named `total_claims`. This variable should contain the total amount of claims in the list of claims.

    > **Hint** Use the `sum()` function for lists.

*  Your insurance company isn't a nonprofit; you only pay out 30% of the losses, or claims, that any merchant submits. So, in the second line of the function, create a variable named `total_payout`. This variable should be equal to `total_claims`, multiplied by 30% (0.30).

* Make the function return the `total_payout`.

* Use the list of `weekly claims` for your function.

* Print the total insurance payout.

---

© 2023 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
