Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is some content on the topic of decision tables for the notes of the Unit 2 - Software Requirement Specifications (SRS) in the subject of Software Engineering.

### Decision Tables

- A decision table is a tabular representation of the logic of a decision.
- A decision table consists of four parts: conditions, actions, rules, and stubs.
- Conditions are the inputs or factors that affect the decision. They are usually expressed as questions or statements that can be answered by yes or no.
- Actions are the outputs or consequences of the decision. They are usually expressed as statements that describe what to do or what will happen.
- Rules are the combinations of conditions and actions that define the decision logic. They are usually expressed as columns that show the values of the conditions and the actions for each case.
- Stubs are the labels or names of the conditions and actions. They are usually expressed as rows that identify the parts of the decision table.

- An example of a decision table is shown below:

| Stub | Rule 1 | Rule 2 | Rule 3 | Rule 4 |
| --- | --- | --- | --- | --- |
| Condition 1: Is the customer a member? | Y | Y | N | N |
| Condition 2: Is the order amount more than $100? | Y | N | Y | N |
| Action 1: Apply 10% discount | X | - | - | - |
| Action 2: Apply 5% discount | - | X | - | - |
| Action 3: Charge full price | - | - | X | X |
| Action 4: Give a free gift | X | - | X | - |

- The decision table above can be interpreted as follows:

  - Rule 1: If the customer is a member and the order amount is more than $100, then apply 10% discount and give a free gift.
  - Rule 2: If the customer is a member and the order amount is less than or equal to $100, then apply 5% discount.
  - Rule 3: If the customer is not a member and the order amount is more than $100, then charge full price and give a free gift.
  - Rule 4: If the customer is not a member and the order amount is less than or equal to $100, then charge full price.

- Some advantages of using decision tables are:

  - They can simplify complex decision logic by showing all possible cases in a structured format.
  - They can improve the consistency and completeness of the decision logic by avoiding gaps or overlaps in the rules.
  - They can facilitate the communication and verification of the decision logic by using a common notation and language.

- Some disadvantages of using decision tables are:

  - They can become large and unwieldy if there are too many conditions or actions.
  - They can be difficult to maintain and update if the decision logic changes frequently or involves multiple sources.
  - They can be prone to errors or ambiguities if the conditions or actions are not clearly defined or understood.