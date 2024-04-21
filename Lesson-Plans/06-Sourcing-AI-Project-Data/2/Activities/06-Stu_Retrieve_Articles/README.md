# Retrieving Articles

## Introduction

In this activity, you will create an application that grabs articles from the New York Times (NYT) API, stores them within a list, and prints snippets of the articles to the screen.

## Instructions

1. Copy your `.env` file with your `NYT_API_KEY` environment variable into your working folder.

2. Review the [New York Times Article Search API documentation](https://developer.nytimes.com/docs/articlesearch-product/1/overview) to assist you in building your query URL.

3. Retrieve your API key from your `.env` file and save it to a variable. **Warning:** Be sure not to print out any of the query URLs. The query URLs will include your API key and, if pushed to a public repository, someone could steal and use your key.

4. Save the NYT API endpoint to a variable. Make sure that you include the right query parameter for retrieving JSON data!

5. Decide on a search term, and save it to a variable.

6. Limit your search to articles published within a range of dates&mdash;for example, only articles published in 2014. **Hint:** Read the documentation on `end_date`.

7. Build your query URL, and save it to a variable.

8. Retrieve a response from the NYT API with a get request.

9. Review the documentation. How do you get a hold of the articles in the response?

10. Traverse through the returned JSON to retrieve the list of articles and store it in a variable.

11. Print a `snippet` from each article, and separate each snippet using dashes (`-`).

## Bonus

Figure out how we could get 30 results. **Hint:** Look up the `page` query parameter. If you get a message saying you've exceeded your rate limit, don't fret&mdash;you've solved the problem.

---

© 2023 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
