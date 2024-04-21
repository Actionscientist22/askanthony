# TV Ratings

## Introduction

In this activity, you will create an application that reads in a list of TV shows, makes multiple requests from an API to retrieve information, and creates two Pandas DataFrames.

## Instructions

1. You may use the list of TV shows provided in the starter file or create your own.

2. Request information on each TV show from the [TVmaze API's Show Search endpoint](https://www.tvmaze.com/api#show-search)

3. Store the name and rating information into the following lists: `titles` and `ratings`.

4. Separately, store the first `show` result of each show with all of its associated data in a separate list, `all_results`.

5. Store the titles and ratings data in a dictionary, and use it to create a Pandas DataFrame.

6. Use the Pandas `json_normalize()` function to convert the `all_results` list to a Pandas DataFrame.

7. Export the `all_results` DataFrame to a CSV file.

---

© 2023 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
