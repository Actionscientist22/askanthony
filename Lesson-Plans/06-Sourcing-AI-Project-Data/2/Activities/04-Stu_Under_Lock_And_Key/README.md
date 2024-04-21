# Under Lock and Key

## Introduction

You will create a `.env` file to store the API keys you created prior to this class, and test one of them out to ensure it works. You will then be able to copy your `.env` file into each activity folder that needs it.

## Instructions

### Store API keys

1. Navigate to the following resources to retrieve your API keys:

    * [New York Times API](https://developer.nytimes.com/my-apps) and navigate to the App you created previously.

    * [The Movie Database (TMDB) API Settings](https://www.themoviedb.org/settings/api)

    * [OpenWeather](https://home.openweathermap.org/api_keys)

2. Create a new `.env` file, and declare the following environment variables:

    * `NYT_API_KEY` that stores your New York Times API key.

    * `TMDB_API_KEY` that stores your TMDB API key.

    * `WEATHER_API_KEY` that stores your OpenWeather API key.

3. Open the Jupyter Notebook starter file, and import the Python `requests`, `os` and `dotenv` libraries.

### Execute API call with API key/env variable

4. Use the `load_dotenv()` method from the `dotenv` package to load and export the environment variables.

5. Use the `os.getenv()` function to retrieve the environment variable named `TMDB_API_KEY`, and store it as a Python variable named `api_key`.

6. Use the `type` function to confirm the retrieval of the API key. Hint: If `NoneType` is returned, the environment variable does not exist. Revisit steps 2 and 3.

7. Review the [documentation](https://developer.themoviedb.org/docs/search-and-query-for-details) to create your search by title `request_url`. Create a variable for the title.

8. Concatenate the `request_url`, `title`, and `api_key` variables. Don't forget to include the parameter strings for the title and API key!

9. Execute a `GET` request using Python requests library and the newly created `request_url`.

10. Display content to screen using the `json.dumps()`.

### Bonus: Retrieve Movie Credits Data

If time permits, create a function that accepts a movie ID and uses the [credits](https://developer.themoviedb.org/reference/movie-credits) API request to retrieve the credits information for a film, then use it to retrieve the credits for the following films:

* Elemental;

* House of Flying Daggers;

* Howl's Moving Castle;

* The Adventures of Priscilla: Queen of the Desert; and

* Moana.

**Note:** You will need to retrieve the movie ID from the search request before you can use the credits API request.

---

© 2023 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
