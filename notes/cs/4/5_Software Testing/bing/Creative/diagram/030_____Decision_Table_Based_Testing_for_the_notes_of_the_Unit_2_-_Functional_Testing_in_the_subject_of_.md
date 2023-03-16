### Decision Table Based Testing

- Decision table based testing is a software testing technique used to test system behavior for different input combinations  .
- It is a systematic approach where the several input combinations and their corresponding system behavior (output) are represented in tabular form .
- It is also called a cause-effect table because it shows the causes (conditions) and effects (actions) of the system.
- It is useful for testing complex business logic that involves multiple conditions and outcomes  .
- It helps to identify test cases that cover all possible scenarios and avoid redundant or missing test cases  .
- It also helps to simplify the test design and documentation process and make it easy to understand and maintain  .

#### How to create a decision table for testing?

- Identify the input conditions and output actions of the system under test   .
- List all the input conditions as columns and output actions as rows in a table   .
- Assign a unique identifier to each condition and action for easy reference   .
- Determine the possible values or states for each condition and action   .
- For each condition, use Y (Yes) or N (No) to indicate whether it is true or false   .
- For each action, use X to indicate whether it is performed or not   .
- For each combination of conditions, fill in the corresponding actions   .
- Eliminate any duplicate or impossible combinations of conditions and actions   .
- Number each remaining combination as a test case   .

#### Example of a decision table for testing

- Consider a system that calculates the discount for a customer based on the following rules  :

  - If the customer is a member and the purchase amount is more than $100, then the discount is 10%.
  - If the customer is a member and the purchase amount is less than or equal to $100, then the discount is 5%.
  - If the customer is not a member and the purchase amount is more than $200, then the discount is 5%.
  - If the customer is not a member and the purchase amount is less than or equal to $200, then the discount is 0%.

- A decision table for this system can be created as follows  :

| Condition | C1: Customer is a member | C2: Purchase amount > $100 | C3: Purchase amount > $200 |
|-----------|--------------------------|---------------------------|---------------------------|
| Action    | A1: Discount = 10%       | A2: Discount = 5%         | A3: Discount = 0%         |
| Test Case |                          |                           |                           |
| 1         | Y                        | Y                         | -                         |
| 2         | Y                        | N                         | -                         |
| 3         | N                        | -                         | Y                         |
| 4         | N                        | -                         | N                         |

- The dash (-) indicates that the condition or action is irrelevant or not applicable for that test case  .
- The test cases can be executed by using the input values that satisfy the conditions and verifying the output values that match the actions  .

#### Advantages of decision table based testing

- It covers all possible scenarios and ensures complete test coverage  .
- It avoids redundant or missing test cases by eliminating duplicate or impossible combinations [