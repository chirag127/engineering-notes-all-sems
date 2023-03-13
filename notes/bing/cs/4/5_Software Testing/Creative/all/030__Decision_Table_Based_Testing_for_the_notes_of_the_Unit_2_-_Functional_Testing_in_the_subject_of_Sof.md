### Decision Table Based Testing for the notes of the Unit 2 - Functional Testing in the subject of Software Testing

- Decision table based testing is a technique that uses a table to represent the logical relationships between inputs and expected outputs of a system or a component.
- A decision table consists of four quadrants: conditions, actions, rules, and rule numbers.
- Conditions are the inputs or preconditions that affect the behavior of the system or component.
- Actions are the outputs or postconditions that result from the execution of the system or component.
- Rules are the combinations of conditions and actions that define the expected behavior of the system or component for a given scenario.
- Rule numbers are the identifiers of the rules in the table.
- A decision table can be represented in two formats: horizontal or vertical. The horizontal format has the conditions on the left and the actions on the right, while the vertical format has the conditions on the top and the actions on the bottom.
- An example of a horizontal decision table is shown below:

| Rule | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- |
| Condition | | | | |
| User is logged in | Y | Y | N | N |
| User has sufficient balance | Y | N | Y | N |
| Action | | | | |
| Allow withdrawal | Y | N | N | N |
| Display error message | N | Y | Y | Y |

- An example of a vertical decision table is shown below:

| Condition | User is logged in | User has sufficient balance |
| --- | --- | --- |
| Action | Allow withdrawal | Display error message |
| --- | --- | --- |
| Rule 1 | Y | Y | Y | N |
| Rule 2 | Y | N | N | Y |
| Rule 3 | N | Y | N | Y |
| Rule 4 | N | N | N | Y |

- The advantages of decision table based testing are:
  - It is easy to understand and communicate the logic of the system or component.
  - It can cover all possible combinations of inputs and outputs.
  - It can reduce the number of test cases by eliminating redundant or invalid scenarios.
  - It can facilitate the identification of gaps or inconsistencies in the requirements or specifications.
- The disadvantages of decision table based testing are:
  - It can become complex and difficult to maintain if the number of conditions or actions is large.
  - It can be time-consuming and error-prone to create and update the decision table manually.
  - It can be challenging to verify the completeness and correctness of the decision table.
- A mnemonic to remember the four quadrants of a decision table is **CARR** (Conditions, Actions, Rules, Rule numbers).
- A learning trick to create a decision table is to use the following steps:
  - Identify the conditions and actions that are relevant to the system or component under test.
  - Assign a unique identifier to each condition and action.
  - Determine the number of rules by calculating the product of the number of possible values for each condition.
  - Assign a unique number to each rule.
  - Fill in the values for each condition and action in each rule, using Y (yes), N (no), or - (don't care) as appropriate.
  - Check the validity and completeness of the decision table by ensuring that each rule is consistent with the requirements or specifications, and that there are no missing or overlapping rules.