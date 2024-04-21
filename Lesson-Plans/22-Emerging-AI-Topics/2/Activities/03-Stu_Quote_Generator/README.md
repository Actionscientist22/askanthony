# Quote Generator

In this activity, you will write a program to generate new “quotes” in a particular style by following examples given. You will select quotes on various topics and use them to create a prompt template. The program will ask the user for a topic that’s on their mind and will provide them with a fictional quote in the style of the examples you chose.

## Instructions

1. Look over and run the first block for loading a `.env` file and setting the OpenAI API key and model variables.

2. Look over and run the block with the imports for the LangChain components you’ll need, including `ChatOpenAI`, `PromptTemplate`, `FewShotPromptTemplate`, and `LLMChain`.

3. Initialize your LLM using your API key and model name.
  * You likely want to use a higher `temperature` here to encourage the LLM to generate new quotes rather than just recreating existing ones.

4. Create a list of dictionaries for your examples with keys of `topic` and `quote` for each entry.

5. Find or create quotes that you want to use as examples. Try to find at least 3 to 4 examples, and try to make sure they cover a variety of topics but share a similar style. The more distinct the style is, the more clear it will be if your program is matching that style or not. Things that might work well are authors from a past time period, specific comedy styles, or quotes that use a regional dialect or accent.

6. Define the format for your examples as a string. Make sure the names used match the keys in your example dictionaries.

7. Create a template object for your examples.

8. Define a prefix for your prompt template as a string. Make sure it gives guidance on the specific task of generating quotes that match the style of the examples given, focused on the topic the human provides.

9. Create a suffix for your prompt template that includes a spot for the user’s query.

10. Create your prompt template using the examples, prefix, suffix, and other necessary parameters.

11. Create an `LLMChain` using your prompt template.
  * For debugging purposes at first, you might choose to also pass `verbose-True` to the chain, but you should remove it once you’ve confirmed your program is running correctly.

12. Prompt the user for a topic, and use that to define your query as a dictionary.

13. Call the chain’s `invoke` method and print the output.

If the resulting quote doesn’t match the style you expected, make sure that your chain’s prompt is actually correctly including the examples. You can also add more examples or swap others in to better inform the LLM of the style you’re looking for it to match.

### Bonus

The LLM would likely match the desired quote style better if it had a wider range of examples, but too many examples would make our prompt exceed the token limit for our models. One way to address this is to create a larger set of examples and then use an `ExampleSelector` to pick specific ones for the query given. (You can look at the [ExampleSelector documentation] (https://python.langchain.com/docs/modules/model_io/prompts/few_shot_examples#using-an-example-selector) for more details.) Compile a longer list of quotes (possibly in a separate text file that your program can read from), and create an `ExampleSelector` to manage them.

---

© 2023 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
