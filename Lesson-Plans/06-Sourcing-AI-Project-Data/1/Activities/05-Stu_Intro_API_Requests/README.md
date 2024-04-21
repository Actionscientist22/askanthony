# Introductory API Requests

## Introduction

In this activity, you'll submit `GET` requests using the Python `requests` library for one of the below `request urls`. Then, interpret the JSON output and save a fact or other value from the JSON output, as a variable.

APIs

* Star Wars Characters -> https://swapi.dev/api/people/

* World Health Organization - Specialist medical practitioners (number) -> https://ghoapi.azureedge.net/api/HWF_0004

* Books by writer Greg Pak -> https://openlibrary.org/authors/OL2864471A/works.json

* Exchange Rates ->  https://open.er-api.com/v6/latest/CAD

* US Dept of Treasury Spending Stats -> https://api.usaspending.gov//api/v2/references/agency/456/

* US GDP Data -> http://api.worldbank.org/v2/country/us?format=json

## Instructions

1. Import the `requests` and `json` libraries.

2. Choose one of the above APIs to work with for this assignment.

3. Execute the `requests.get` function using one of the `request urls`, and store the output in a variable named `response_data`.

4. Retrieve the status code of the request.

5. Execute `response_data.content` to extract the data from the request. Store the data in a variable named `response_content`, and output the data to the screen.

6. Use the `json` function to format `response_content` as JSON. Store the output as a variable named `data`.

7. Use `json.dumps` to print `response_content` to the screen with formatting. Use the `indent=4` parameter to format with indentation.

8. Decipher the JSON data, then select an element from the JSON and store it into a new variable. Hint: JSON attribute names are like keys in dictionaries.

### Challenge

If time remains, use the `GET` function to explore the other APIs.

### Hint

Selecting values from JSON data requires data to be accessed first by the parent object and then child. When an API returns output with multiple JSON Objects, indexes have to be specified to indicate which object/record should be selected. For example,

  ```python
  selected_value = data['all'][0]['text']
  ```

---

© 2023 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
