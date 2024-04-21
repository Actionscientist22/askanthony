# LangChain Practice

In this activity you’ll be extending the recipe suggestion program to allow for diet types and dietary restrictions. You’ll ask the user for some desired ingredients as before, but will also ask them about dietary restrictions or preferences. You’ll use `LLMChain` and `ConstitutionalChain` to ensure that the recipes suggested fit the user’s needs.

## Instructions

1. Look over and run the first block for loading a `.env` file. This block will store your OpenAI API key in a variable, as well as the OpenAI model you would like to use. It’s suggested that you use `gpt-3.5-turbo` as in the example.

2. Look over and run the block with the imports for the LangChain components you’ll need, including `ChatOpenAI`, `LLMChain`, `ConstitutionalChain`, `ConstitutionalPrinciple`, and `ChatPromptTemplate`.

3. Prompt the user for the main ingredients they would like for the first and second days’ meals, storing each response in a variable.

4. Prompt the user for their diet type, listing some examples (such as vegan, omnivorous, kosher, etc.), storing the response in a variable.

5. Initialize your LLM using your API key and model name.
  * You can specify the `temperature` here to adjust how consistent or unique you would like the model to be when generating responses.

6. Create an `LLMChain` for generating the initial recipes, using the LLM you initialized above as a parameter.
  * Remember that we must also give it a prompt, and for now we can use a simple one as in the instructor’s example.

7. Create a `ConstitutionalPrinciple` using the supplied diet type. You will need to include the user’s diet type in the `critique_request` and `revision_request` strings, giving some context so the chain knows that it should ensure these dietary needs are met.

8. Create a `ConstitutionalChain` using the `from_llm` function, giving it your `LLMChain` principle and the original `ChatOpenAI` LLM as parameters.
  * For debugging purposes at first, you might choose to also pass `verbose-True` to this function, but you should remove it once you’ve confirmed your program is running correctly.

9. Construct a query that will be used to generate the initial recipe. It should only mention the two main ingredients, not the dietary restriction.

10. Call the `invoke` method of the `ConstitutionalChain` using the query as input, then print the result.

### Bonus

Some users might not want any dietary restrictions, or may not want to specify main ingredients for their recipes. Think of ways you could adapt the program to allow these inputs to be optional.
  * What parts of the program would or would not need to run if the user didn’t specify any dietary needs?
  * How would you construct your query if the user didn’t want to specify main ingredients?

---

© 2023 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
