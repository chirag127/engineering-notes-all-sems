### Decision Table Based Testing

- Decision table based testing is a software testing technique used to test system behavior for different input combinations  .
- It is a systematic approach where the several input combinations and their corresponding system behavior (output) are represented in tabular form .
- It is also called a cause-effect table because it shows the causes (conditions) and effects (actions) of the system.
- It is useful for testing complex business logic that involves multiple conditions and outcomes  .
- It helps to identify test cases that cover all possible scenarios and avoid redundant or missing test cases  .
- It also helps to simplify the test design and documentation process and make it easy to understand and communicate  .

#### How to create a decision table for testing?

- Identify the input conditions and output actions of the system under test   .
- List the input conditions as columns and output actions as rows in a table   .
- Assign a unique identifier to each condition and action for easy reference   .
- Determine the possible values or states for each condition and action   .
- Calculate the number of test cases required by multiplying the number of values for each condition   .
- List the test cases as columns and fill in the values for each condition and action   .
- Simplify the table by eliminating duplicate or impossible test cases   .
- Verify the table by checking the completeness, consistency, and correctness of the test cases   .

#### Example of a decision table for testing

- Consider a system that calculates the discount for a customer based on the following rules   :

  - If the customer is a regular customer and the purchase amount is more than $100, then the discount is 10%.
  - If the customer is a regular customer and the purchase amount is less than or equal to $100, then the discount is 5%.
  - If the customer is not a regular customer and the purchase amount is more than $200, then the discount is 5%.
  - If the customer is not a regular customer and the purchase amount is less than or equal to $200, then the discount is 0%.

- The input conditions are:

  - C: Customer is regular (Y/N)
  - P: Purchase amount (>100, <=100, >200, <=200)

- The output action is:

  - D: Discount (10%, 5%, 0%)

- The decision table for testing is:

| C | P | D |
|---|---|---|
| Y | >100 | 10% |
| Y | <=100 | 5% |
| N | >200 | 5% |
| N | <=200 | 0% |

- The number of test cases required is 2 x 2 = 4.
- The test cases are:

| Test Case | C | P | D |
|-----------|---|---|---|
| TC1 | Y | >100 | 10% |
| TC2 | Y | <=100 | 5% |
| TC3 | N | >200 | 5% |
| TC4 | N | <=200 | 0% |

- The table is already simplified and verified.