### Decision Table Based Testing

- Decision table based testing is a software testing technique used to test system behavior for different input combinations  .
- It is a systematic approach where the several input combinations and their corresponding system behavior (output) are represented in tabular form .
- It is also called a cause-effect table because it shows the causes (conditions) and effects (actions) of the system.
- It is useful for testing complex business logic that involves multiple conditions and outcomes  .

#### Advantages of Decision Table Based Testing

- It helps to identify all the possible scenarios and test cases for a given functionality  .
- It reduces the redundancy and inconsistency of test cases by eliminating duplicate or contradictory conditions and actions  .
- It simplifies the test design and execution process by providing a clear and concise representation of the system behavior  .
- It facilitates the communication and collaboration among the stakeholders, such as developers, testers, and business analysts, by using a common language and format  .

#### How to Create a Decision Table for Testing?

- Identify the input conditions and output actions for the system under test   .
- Assign a unique identifier to each condition and action, such as C1, C2, A1, A2, etc   .
- Create a table with four quadrants: condition stub, condition entries, action stub, and action entries   .
- List all the conditions in the condition stub and all the actions in the action stub   .
- Determine the number of columns (test cases) needed for the table by calculating the power of two of the number of conditions, such as 2^n, where n is the number of conditions   .
- Fill the condition entries with either Y (yes), N (no), or - (don't care) to indicate whether the condition is true, false, or irrelevant for each test case   .
- Fill the action entries with either X (execute) or - (don't execute) to indicate whether the action is performed or not for each test case   .
- Optimize the table by removing any unnecessary or impossible test cases, such as those with contradictory or redundant conditions or actions   .

#### Example of a Decision Table for Testing

- Suppose we want to test a login functionality of a web application that has the following requirements:
  - The user must enter a valid username and password to login.
  - The user can choose to remember the password for future logins.
  - The user can reset the password by clicking on the forgot password link.
  - The user can cancel the login by clicking on the cancel button.
- The input conditions and output actions for this functionality are:
  - C1: Username is valid
  - C2: Password is valid
  - C3: Remember password is checked
  - C4: Forgot password is clicked
  - C5: Cancel is clicked
  - A1: Login successful
  - A2: Login failed
  - A3: Password remembered
  - A4: Password reset
  - A5: Login canceled
- The decision table for this functionality is:

| Condition Stub | C1 | C2 | C3 | C4 | C5 |
| -------------- | -- | -- | -- | -- | -- |
| Condition Entries | Y | Y | Y | - | - |
|  | Y | Y | N | - | - |
|  | Y | N | Y | - | - |
|  | Y | N | N | - | - |
|  | N | Y