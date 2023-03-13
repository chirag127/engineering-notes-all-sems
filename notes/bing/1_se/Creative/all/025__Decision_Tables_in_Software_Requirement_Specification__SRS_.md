### Decision Tables in Software Requirement Specification (SRS)

- A decision table is a tabular representation of the logic and rules that govern the behavior of a software system based on different combinations of inputs and outputs.
- A decision table consists of four quadrants: condition stub, condition entry, action stub and action entry.
- The condition stub lists the possible inputs or conditions that affect the system's behavior. The condition entry shows the values or states of each condition for a given situation or scenario.
- The action stub lists the possible outputs or actions that the system performs based on the inputs or conditions. The action entry shows which actions are executed or not executed for a given situation or scenario.
- A decision table can be used to specify the functional requirements of a software system in a clear, concise and consistent way. It can also be used to verify and validate the system's behavior against the expected outcomes.
- A decision table can be represented in different formats, such as horizontal, vertical, matrix or nested. The choice of format depends on the complexity and readability of the table.
- A decision table can be constructed using the following steps:
  - Identify the inputs or conditions that affect the system's behavior.
  - Identify the outputs or actions that the system performs based on the inputs or conditions.
  - Identify the possible values or states of each input or condition.
  - Identify the possible combinations of inputs or conditions that cover all the scenarios or situations.
  - Identify the outputs or actions that are executed or not executed for each combination of inputs or conditions.
  - Arrange the inputs or conditions, outputs or actions, and their values or states in a tabular format.
  - Simplify the table by eliminating redundant or contradictory rows or columns.
  - Test the table by checking if it covers all the scenarios or situations and if it produces the expected outcomes.

- An example of a decision table for a software system that calculates the discount for a customer based on the type of product and the quantity purchased is shown below:

| Condition Stub | Condition Entry | Condition Entry | Condition Entry | Condition Entry |
| -------------- | --------------- | --------------- | --------------- | --------------- |
| Product Type   | A               | A               | B               | B               |
| Quantity       | < 10            | >= 10           | < 10            | >= 10           |
| Action Stub    | Action Entry    | Action Entry    | Action Entry    | Action Entry    |
| Discount       | 0%              | 10%             | 5%              | 15%             |

- A mnemonic to remember the four quadrants of a decision table is CACA: Condition-Action-Condition-Action.