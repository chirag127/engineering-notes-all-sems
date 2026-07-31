# Decision Table Based Testing

- Decision table based testing is a software testing technique used to test system behavior for different input combinations  .
- It is a systematic approach where the different input combinations and their corresponding system behavior (output) are captured in a tabular form.
- It is also called a cause-effect table, as it shows the causes (conditions) and effects (actions) of the system.
- It is useful for testing complex business logic that involves multiple conditions and rules  .
- It helps to ensure the completeness and consistency of the test cases  .

## How to create a decision table for testing?

- Identify the input conditions and output actions of the system under test   .
- List all the possible combinations of input conditions and output actions in a tabular form   .
- Assign a unique identifier to each combination (such as T1, T2, etc.)   .
- Mark the input conditions and output actions as true (Y), false (N), or don't care (-) for each combination   .
- Simplify the table by eliminating duplicate or redundant combinations   .
- Use the table as a guide to design and execute the test cases   .

## Example of a decision table for testing

- Suppose we want to test a system that calculates the discount for a customer based on the following rules  :

  - If the customer is a senior citizen, they get a 10% discount.
  - If the customer is a student, they get a 5% discount.
  - If the customer is a senior citizen and a student, they get a 15% discount.
  - If the customer is neither a senior citizen nor a student, they get no discount.

- The input conditions are:

  - C1: Customer is a senior citizen
  - C2: Customer is a student

- The output action is:

  - A1: Discount percentage

- The decision table for this system is:

| Test Case | C1 | C2 | A1 |
| --------- | -- | -- | -- |
| T1        | Y  | Y  | 15 |
| T2        | Y  | N  | 10 |
| T3        | N  | Y  | 5  |
| T4        | N  | N  | 0  |

- The test cases derived from the table are:

  - T1: Verify that the system calculates a 15% discount for a customer who is a senior citizen and a student.
  - T2: Verify that the system calculates a 10% discount for a customer who is a senior citizen and not a student.
  - T3: Verify that the system calculates a 5% discount for a customer who is not a senior citizen and a student.
  - T4: Verify that the system calculates no discount for a customer who is neither a senior citizen nor a student.

## Advantages of decision table based testing

- It helps to cover all the possible scenarios and outcomes of the system  .
- It helps to avoid missing or overlapping test cases  .
- It helps to simplify and organize the test cases in a clear and concise way  .
- It helps to communicate and document the system logic and requirements  .
- It helps to reduce the testing effort and time  .

## Scope of decision table based testing

- Decision table based testing is suitable for testing systems that have multiple input conditions and output actions   .
- It is especially useful for testing systems that have complex business rules and logic[^