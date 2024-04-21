# Activity Planner

In this activity, you will create an agent that helps a user plan a weather-appropriate activity in a city they are visiting. The agent will use the OpenWeatherMap API to check the weather in that location and then suggest an activity for the user.

## Instructions

1. Look over and run the first block for loading a `.env` file and setting the OpenAI API key and model variables.

2. Look over and run the block with the imports for the LangChain components you’ll need, including `ChatOpenAI`, `initialize_agent`, and `load_tools`.

3. Initialize your LLM using your API key and model name.
  * You can specify the `temperature` here to adjust how consistent or unique you would like the model to be when generating responses.

4. Load the OpenWeatherMap API tool.
  * Remember that your API key will need to be stored in an environment variable named `OPENWEATHERMAP_API_KEY`.

5. Initialize your agent.

6. Prompt the user for the location they’re visiting. You may want to give additional instructions to help make sure they provide all the information that OpenWeatherMap will need (such as state/province/country.)

7. Construct the query to give your agent using the location. It should include instructions for the activities provided to be weather-appropriate. You may also want to instruct the agent to be specific about places to visit to avoid it suggesting very generic activity types.

8. Run the agent using the query and print the results.

9. If you run the program here, you may find that the agent fails to find an answer some of the time. Because ReAct agents don’t make certain that the actions they take will work before taking them, this is not uncommon. You can add the `handle_parsing_errors = True` parameter to your `initialize_agent` call. This gives the errors as feedback to the agent and allows it to try again.

10. You can also increase or decrease the number of steps the agent is allowed to try to take using the `max_iterations` parameter to `initialize_agent`. Try changing this to give your agent more chances to recover if its steps do not work.

* You may also want to use `try` and `except` blocks to handle if the agent encounters an error with API calls or fails to find an answer. Try to make your program as robust and user-friendly as possible.

### Hint

* Agents are an especially newly developing part of LangChain and are regularly changing. You may encounter deprecation warnings due to changes being made in the LangChain agents library. These are fine, as long as the program generates the correct result, but you may want to experiment with whatever new approach is suggested in the warning text.

### Bonus

Once the agent has checked the weather and suggested an activity, the user might want to ask for an alternative suggestion or give feedback to refine the suggestion. A loop could be used to have the agent completely re-run and suggest something else, but allowing conversation could be more challenging. The agent is suited to taking the steps needed for the first suggestion, but not general conversation after. Look back at how we used conversational memory before. You can create a memory buffer and give it to the agent via the `memory` parameter of `initialize_agent`, and then use that same buffer for a `ConversationChain` after the agent has made its suggestion. Add a conversation loop to the program to let the user keep engaging after the initial suggestion is made.

---

© 2023 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
