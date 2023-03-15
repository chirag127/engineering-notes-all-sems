Hello, I am Sydney, your AI assistant. I can help you with your study material for Software Engineering. Here are some notes on the topic of Decision Tables for the Unit 2 - Software Requirement Specifications (SRS).

### Decision Tables

- A decision table is a tabular representation of the logic of a decision.
- A decision table consists of four parts: conditions, actions, rules, and stubs.
- Conditions are the inputs or factors that affect the decision. They are usually represented by columns in the table.
- Actions are the outputs or outcomes of the decision. They are usually represented by rows in the table.
- Rules are the combinations of conditions and actions that define the logic of the decision. They are usually represented by cells in the table.
- Stubs are the labels or names of the conditions and actions. They are usually placed at the top and left of the table.

- A decision table can have different formats, such as limited entry, extended entry, or matrix.
- A limited entry decision table has only two possible values for each condition and action: Y (yes) or N (no).
- An extended entry decision table can have more than two possible values for each condition and action, such as numeric, textual, or symbolic values.
- A matrix decision table can have multiple conditions and actions in each cell, separated by commas or semicolons.

- A decision table can be used to specify the functional requirements of a software system, such as the behavior of a module, a function, or a use case.
- A decision table can help to identify and eliminate logical errors, inconsistencies, redundancies, and incompleteness in the requirements specification.
- A decision table can also help to simplify and clarify the requirements specification, by presenting the logic in a concise and structured way.

- An example of a decision table for a software system that calculates the discount for a customer based on their age and membership status is given below:

| Condition | Rule 1 | Rule 2 | Rule 3 | Rule 4 |
| --- | --- | --- | --- | --- |
| Age < 18 | Y | N | N | N |
| Age >= 60 | N | Y | N | N |
| Member | Y | Y | N | N |
| Action | Discount = 20% | Discount = 15% | Discount = 10% | Discount = 0% |