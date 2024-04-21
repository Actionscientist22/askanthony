# Recipe Selection

In this activity, you will create a more user-friendly recipe suggestion program that allows the user to get more information about dishes they’re interested in. You’ll first use an LLM to generate the names of some dishes, then you’ll use an output parser to process the output, and then allow the user to select one of the dishes to see a full recipe.

## Instructions

1. Look over and run the first block for loading a `.env` file and setting the OpenAI API key and model variables.

2. Look over the imports given in the starter code for the LangChain components you’ll need, including `ChatOpenAI` and `CommaSeparatedListOutputParser`.

3. Initialize your LLM using your API key and model name.
  * You can specify the `temperature` here to adjust how consistent or unique you would like the model to be when generating responses.

4. Initialize a `CommaSeparatedListOutputParser` object.

5. Get the format instructions from the parser.

6. Create a query that asks the LLM for the names of several dishes, and combine the query with the format instructions.

7. Invoke the LLM with the query.
  * You may want to test the program at this point and ensure the output is what you expect and is in the correct format. If it’s not, you can adjust your query or add additional instructions.

8. Parse the LLM’s output and store it.
  * This is another good point to test the result to make sure it parsed properly.

9. Print out each suggested dish name, along with a number the user can use to identify it.

10. Prompt the user to ask them for the number of the dish they would like more information for, and store it as an integer.
  * Remember that the list will be indexed starting at zero.

11. Get the name of the dish the user selected from the list, and use it to build a new query that asks the LLM to give a full recipe for that dish. Print the result.

### Bonus

The LLM might not generate any dishes that the user is interested in. You could integrate more of the user’s preferences like we did before to ensure they are recommended dishes they’ll like. You could also introduce a loop, allowing the user to ask for a new set of dishes altogether.

---

© 2023 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.

