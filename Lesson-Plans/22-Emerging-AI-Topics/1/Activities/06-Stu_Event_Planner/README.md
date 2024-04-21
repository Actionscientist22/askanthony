# Group Event Planner

In this activity, you will create an AI event planner that takes a group of people’s likes and dislikes into consideration when planning an event for them. It will ask the user about the attendees for the event, and represent those attendees as entities to generate the overall event plan.

## Instructions

1. Look over and run the first block for loading a `.env` file and setting the OpenAI API key and model variables.

2. Look over and run the block with the imports for the LangChain components you’ll need, including `ChatOpenAI`, `ConversationChain`, `ConversationEntityMemory`, and the entity memory conversation template.

3. Initialize your LLM using your API key and model name.
  * You can specify the `temperature` here to adjust how consistent or unique you would like the model to be when generating responses.

4. Create a `ConversationEntityMemory` object, using the LLM you initialized above as a parameter.

5. Create a `ConversationChain`, giving as parameters your `ConversationEntityMemory`, the entity memory conversation template, and the original `ChatOpenAI` LLM.
  * For debugging purposes at first, you might choose to also pass `verbose-True` to this function, but you should remove it once you’ve confirmed your program is running correctly.

6. Prompt the user for their own name, and store it in a variable.

7. Prompt the user for their own likes and dislikes for activities.

8. Create a string containing a sentence or two that includes the name and provided description to give to the `ConversationChain`.
  * The sentence(s) should be in first-person, so it is clear that this is the user.
  * It should also include a statement that this person will be organizing and attending the event.

9. Call the `run` method of the `ConversationChain`, giving the above string as an input.
  * You do not need to print the response here, but you may want to execute the program to test it to make sure the user is being correctly recorded as an entity.

10. Prompt the user, asking how many other people they want to plan the event for, storing their response as an integer.

11. Create a loop that will run once for each other attendee.

12. Within the loop, prompt the user for the name of the attendee and a description of their likes and dislikes.

13. Combine the name and the likes/dislikes into a single string. Make sure that it mentions that this person will be attending the event.

14. Call the `run` method of the `ConversationChain`, giving the above string as an input.
  * Again, you do not need to print the response here.

15. Outside of the loop, create a string that asks the LLM to plan an event for all the people previously described.

16. Call the `predict` method of the `ConversationChain` using the above string as input, then print the result.

### Bonus

The user might want to specify more details about the event invitees or ask for an alternate activity idea from the program. Add an additional loop that lets the user have an ongoing conversation with the program after the first activity suggestion is given.

---

© 2023 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
