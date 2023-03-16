### Decision Table Based Testing

- Decision table based testing is a software testing technique used to test system behavior for different input combinations  .
- It is a systematic approach where the different input combinations and their corresponding system behavior (output) are captured in a tabular form .
- It is also called a cause-effect table, as it shows the causes (conditions) and effects (actions) of the system behavior .
- It is useful for testing complex business logic, where the system behavior is different for different inputs and not the same for a range of inputs .
- It helps to make sure that all possible scenarios are covered and no important test cases are missed  .
- It also helps to simplify the test cases and avoid redundancy  .
- It can be used for both functional and non-functional testing .

#### How to create a decision table for testing?

- Identify the conditions (inputs) and actions (outputs) of the system behavior  .
- List all the possible values or states for each condition and action  .
- Assign a unique identifier to each condition and action  .
- Create a table with four quadrants: condition stub, condition entries, action stub, and action entries  .
- In the condition stub, list all the conditions with their identifiers  .
- In the action stub, list all the actions with their identifiers  .
- In the condition entries, fill in the values or states for each condition for each test case  .
- In the action entries, fill in the values or states for each action for each test case  .
- Eliminate any duplicate or invalid test cases  .
- Number the test cases and execute them  .

#### Example of a decision table for testing

- Suppose we want to test the login functionality of a website, where the user can enter a username and a password, and the system can either accept or reject the login attempt  .
- The conditions are: username is valid, password is valid  .
- The actions are: login is accepted, login is rejected, error message is displayed  .
- The possible values or states for each condition and action are: Y (yes), N (no)  .
- The identifiers for each condition and action are: C1, C2, A1, A2, A3  .
- The decision table for testing the login functionality is:

| Condition Stub | Condition Entries | Action Stub | Action Entries |
| -------------- | ----------------- | ----------- | -------------- |
| C1: Username is valid | Y | Y | N | N | A1: Login is accepted | Y | N | N | N |
| C2: Password is valid | Y | N | Y | N | A2: Login is rejected | N | Y | Y | Y |
|                    |   |   |   |   | A3: Error message is displayed | N | N | N | Y |

- The test cases are:

| Test Case | C1 | C2 | A1 | A2 | A3 |
| --------- | -- | -- | -- | -- | -- |
| 1 | Y | Y | Y | N | N |
| 2 | Y | N | N | Y | N |
| 3 | N | Y | N | Y | N |
| 4 | N | N | N | Y | Y |

- Test case 1: Enter a valid username and a valid password, the login should be accepted.
-