Decision Table Based Testing is a software testing technique used to test system behavior for different input combinations. It is a systematic approach where the different input combinations and their corresponding system behavior (Output) are captured in a tabular form. That is why it is also called as a Cause-Effect table where Cause and effects are captured for better test coverage. A Decision Table is a tabular representation of inputs versus rules/cases/test conditions. It is a very effective tool used for both complex software testing and requirements management. A decision table helps to check all possible combinations of conditions for testing and testers can also identify missed conditions easily. The conditions are indicated as True (T) and False (F) values.

A decision table has four parts: condition stubs, action stubs, condition entries and action entries. Condition stubs are the conditions that are used to determine a particular action or set of actions. Action stubs are the possible actions that are performed based on the conditions. Condition entries are the values that are inputted for each condition. Action entries are the values that are outputted for each action.

A decision table can be of two types: limited entry and extended entry. Limited entry decision tables have only binary values (T/F) for the condition entries. Extended entry decision tables have more than two values for the condition entries.

An example of a decision table for testing a login screen is given below:

| Conditions | Rule 1 | Rule 2 | Rule 3 | Rule 4 |
|------------|--------|--------|--------|--------|
| Username (T/F) | F | T | F | T |
| Password (T/F) | F | F | T | T |
| Output (E/H) | E | E | E | H |

Legend: T – Correct username/password F – Wrong username/password E – Error message is displayed H – Home screen is displayed

Interpretation: Case 1 – Username and password both were wrong. The user is shown an error message. Case 2 – Username was correct, but the password was wrong. The user is shown an error message. Case 3 – Username was wrong, but the password was correct. The user is shown an error message. Case 4 – Username and password both were correct, and the user navigated to the homepage.