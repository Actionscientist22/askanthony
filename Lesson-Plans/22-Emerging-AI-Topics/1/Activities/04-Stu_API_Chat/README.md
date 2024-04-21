# API Chat

In this activity, you will connect LangChain with the Open Library API to allow a user to ask questions about books and authors. You’ll use the API’s human-readable documentation as the specification for LangChain and allow the user to give queries.

## Instructions

1. Look over and run the first block for loading a `.env` file and setting the OpenAI API key and model variables.

2. Look over and run the block with the imports for the LangChain components you’ll need, including `ChatOpenAI` and `APIChain`.

3. Look over the API description stored in `spec_str`. Notice that this is just the human-readable [documentation](https://openlibrary.org/dev/docs/api/search) from the Open Library API website.
  * Optional: For cleaner, simpler code, save the specification text in a file named `open_library_spec.txt` and read it into a string within your program.

4. Initialize your LLM using your API key and model name.
  * Consider what `temperature` would be best here, and set it appropriately.

5. Create an `APIChain` using the `from_llm_and_api_docs` function, giving it the API specifications and the original `ChatOpenAI` LLM as parameters. Set the allowed domains to a list only including `https://openlibrary.org/` .
  * For debugging purposes at first, you might choose to also pass `verbose-True` to this function, but you should remove it once you’ve confirmed your program is running correctly.

6. Create a loop that will continue until the user enters “exit.”

  * Within the loop, prompt the user to enter a question they have about a book or author.

  * Call the `invoke` method of the `APIChain` using the user’s question as input, then print the result.

7. Execute your program and test it with a few questions about books or authors.

8. Remember that sometimes the API’s response is too large for our LLM and this generates an exception. Add `try` and `except` blocks inside your loop to handle this, informing the user when their query resulted in too large of a response.

---

© 2023 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.

