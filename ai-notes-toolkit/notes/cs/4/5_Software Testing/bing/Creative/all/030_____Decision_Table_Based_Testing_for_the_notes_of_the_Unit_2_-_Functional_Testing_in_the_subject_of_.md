# Decision Table Based Testing

- Decision table based testing is a software testing technique used to test system behavior for different input combinations  .
- It is a systematic approach where the different input combinations and their corresponding system behavior (output) are captured in a tabular form.
- It is also called a cause-effect table, as it shows the causes (conditions) and effects (actions) of the system.
- It is useful for testing complex business logic that involves multiple conditions and resulting actions  .

## Advantages of Decision Table Based Testing

- It helps to cover all possible scenarios and avoid missing any test cases  .
- It simplifies the test design and execution process by using a concise and clear format  .
- It facilitates communication and collaboration among developers, testers, and business analysts, as they can easily understand and verify the logic and requirements  .
- It reduces the maintenance effort by allowing easy updates and modifications to the table  .

## Scope of Decision Table Based Testing

- Decision table based testing is applicable for testing any system that has a finite number of inputs and outputs, and a well-defined set of rules or conditions that govern the system behavior   .
- Some examples of such systems are:

  - Banking systems that have different interest rates and fees based on customer type, account type, balance, etc.
  - E-commerce systems that have different discounts and offers based on product category, quantity, payment method, etc.
  - Insurance systems that have different premiums and benefits based on policy type, age, health, etc.
  - Login systems that have different access levels and permissions based on user role, password, etc.

## How to Create a Decision Table for Testing?

- The steps to create a decision table for testing are   :

  - Identify the input conditions and output actions of the system under test.
  - List all the possible values or states for each input condition and output action.
  - Determine the number of columns (test cases) required for the table by calculating the product of the number of values for each input condition.
  - Assign a unique identifier to each column (test case) and label each row with the input condition or output action name.
  - Fill the table with the appropriate values or states for each input condition and output action for each test case.
  - Simplify the table by eliminating any duplicate or redundant test cases, or by using wildcards (*) to represent any value or state.
  - Review and verify the table for accuracy and completeness.

## Example of a Decision Table for Testing

- Consider a login system that has the following input conditions and output actions:

  - Input conditions:
    - Username: valid or invalid
    - Password: valid or invalid
  - Output actions:
    - Login: success or failure
    - Error message: displayed or not displayed

- A decision table for testing this system can be created as follows:

| Test Case | Username | Password | Login | Error Message |
| --------- | -------- | -------- | ----- | ------------- |
| TC1       | Valid    | Valid    | Success | Not Displayed |
| TC2       | Valid    | Invalid  | Failure | Displayed     |
| TC3       | Invalid  | Valid    | Failure | Displayed     |
| TC4       | Invalid  | Invalid  | Failure | Displayed     |

- This table can be simplified by using a wildcard (*) to represent any value for the password input condition, as the system behavior is the same for any invalid password:

| Test Case | Username | Password | Login | Error Message |
| --------- | -------- | -------- | ----- | ------------- |
| TC1       | Valid    | Valid    | Success | Not Displayed |
| TC2       | Valid    | *        | Failure | Displayed     |
| TC3       | Invalid  | *        | Failure | Displayed     |