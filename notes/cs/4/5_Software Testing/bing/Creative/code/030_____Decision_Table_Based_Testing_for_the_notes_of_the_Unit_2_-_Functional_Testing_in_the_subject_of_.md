### Decision Table Based Testing

- Decision table based testing is a software testing technique used to test system behavior for different input combinations  .
- It is a systematic approach where the different input combinations and their corresponding system behavior (output) are captured in a tabular form.
- It is also called a cause-effect table, as it shows the causes (conditions) and effects (actions) of the system.
- It is useful for testing complex business logic that involves multiple conditions and rules  .
- It helps to make sure that all possible scenarios are covered and no important condition is missed  .
- It also helps to reduce redundancy and inconsistency in test cases .

#### How to create a decision table for testing?

- Identify the conditions (inputs) and actions (outputs) of the system under test   .
- List all the possible values or states for each condition and action   .
- Determine the number of columns in the decision table, which is equal to 2^n, where n is the number of conditions   .
- Assign a unique combination of values or states for each condition to each column   .
- Specify the expected action or output for each column based on the logic and rules of the system   .
- Simplify the decision table by eliminating duplicate or impossible columns   .
- Use the decision table as a basis for designing test cases   .

#### Example of a decision table for testing

- Consider a system that calculates the discount for a customer based on the following rules :

  - If the customer is a senior citizen or a student, they get a 10% discount.
  - If the customer is a loyal member, they get a 15% discount.
  - If the customer is both a senior citizen or a student and a loyal member, they get a 20% discount.
  - If the customer is none of the above, they get no discount.

- The conditions (inputs) are:

  - Customer is a senior citizen or a student (S)
  - Customer is a loyal member (M)

- The action (output) is:

  - Discount percentage (D)

- The decision table for this system is:

| S | M | D |
|---|---|---|
| T | T | 20% |
| T | F | 10% |
| F | T | 15% |
| F | F | 0% |

- The test cases derived from this decision table are:

  - Test case 1: S = T, M = T, D = 20%
  - Test case 2: S = T, M = F, D = 10%
  - Test case 3: S = F, M = T, D = 15%
  - Test case 4: S = F, M = F, D = 0%