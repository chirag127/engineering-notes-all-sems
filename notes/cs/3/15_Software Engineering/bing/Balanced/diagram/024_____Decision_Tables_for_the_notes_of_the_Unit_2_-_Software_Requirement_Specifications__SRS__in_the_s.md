Hello, I am Sydney, your AI assistant. I can help you with your study material for Software Engineering. Here are some notes on Decision Tables for Unit 2 - Software Requirement Specifications (SRS).

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
- A matrix decision table has only one value for each condition and action, and uses symbols such as +, -, or 0 to indicate the presence, absence, or irrelevance of the condition or action.

- A decision table can be used to specify the functional requirements of a software system, such as the behavior of a module, a function, or a feature.
- A decision table can help to identify and eliminate logical errors, inconsistencies, redundancies, or incompleteness in the requirements.
- A decision table can also help to simplify and clarify the requirements, and to facilitate communication and verification among stakeholders.

- An example of a decision table for a software system that calculates the discount for a customer based on their age and membership status is shown below.

| Age | Membership | Discount | Rule |
| --- | --- | --- | --- |
| <18 | Y | 20% | R1 |
| <18 | N | 10% | R2 |
| >=18 and <60 | Y | 15% | R3 |
| >=18 and <60 | N | 5% | R4 |
| >=60 | Y | 25% | R5 |
| >=60 | N | 15% | R6 |

- This is a limited entry decision table with two conditions (Age and Membership) and one action (Discount).
- The stubs are Age, Membership, and Discount.
- The rules are R1 to R6, which define the logic of the decision.
- For example, rule R1 states that if the customer is less than 18 years old and has a membership, then the discount is 20%.