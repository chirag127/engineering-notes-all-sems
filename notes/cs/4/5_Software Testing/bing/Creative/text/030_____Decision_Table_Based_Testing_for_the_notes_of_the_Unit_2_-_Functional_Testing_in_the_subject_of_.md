### Decision Table Based Testing

- Decision table based testing is a technique for testing the functionality of a system based on the combinations of inputs and outputs that can occur in different scenarios.
- A decision table is a tabular representation of the logical rules that govern the behavior of a system. Each row in the table corresponds to a test case, and each column corresponds to a condition or an action.
- A condition is a variable or a parameter that can affect the outcome of a system. An action is a result or an effect that the system produces based on the conditions.
- A decision table can have four possible types of entries: Y (yes), N (no), - (don't care), and X (invalid or error).
- Y means that the condition must be true or the action must be performed for the test case to be valid. N means that the condition must be false or the action must not be performed for the test case to be valid. - means that the condition or the action is irrelevant or optional for the test case. X means that the condition or the action is invalid or causes an error for the test case.
- The steps for creating a decision table are:

  1. Identify the conditions and actions that are relevant for the system under test.
  2. Determine the possible values or states for each condition and action.
  3. Construct a decision table with one column for each condition and action, and one row for each test case.
  4. Fill in the entries for each test case based on the logical rules of the system.
  5. Simplify the decision table by eliminating duplicate or redundant test cases, or by combining test cases with the same outcome.
  6. Execute the test cases and verify the results against the expected actions.

- An example of a decision table for testing a login system is shown below:

| Condition | Condition | Action | Action |
| --------- | --------- | ------ | ------ |
| Username  | Password  | Login  | Error  |
| Y         | Y         | Y      | N      |
| Y         | N         | N      | Y      |
| N         | Y         | N      | Y      |
| N         | N         | N      | Y      |
| X         | -         | N      | Y      |
| -         | X         | N      | Y      |

- The advantages of decision table based testing are:

  - It is easy to understand and communicate the logic of the system.
  - It can cover all possible combinations of inputs and outputs.
  - It can detect inconsistencies or gaps in the requirements or specifications of the system.
  - It can facilitate traceability and maintainability of the test cases.

- The disadvantages of decision table based testing are:

  - It can be tedious and time-consuming to create and update the decision table, especially for complex systems with many conditions and actions.
  - It can result in a large number of test cases, which may be impractical or costly to execute and manage.
  - It may not be suitable for testing non-functional aspects of the system, such as performance, usability, or security.