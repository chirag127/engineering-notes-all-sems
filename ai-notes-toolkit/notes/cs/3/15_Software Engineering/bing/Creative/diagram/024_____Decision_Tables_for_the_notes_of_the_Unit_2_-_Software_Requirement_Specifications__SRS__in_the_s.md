### Decision Tables for the notes of the Unit 2 - Software Requirement Specifications (SRS) in the subject of Software Engineering

- A decision table is a technique used in both testing and requirements management to represent complex logical relationships in a tabular or a matrix form    .
- The upper rows of the table specify the variables or conditions to be evaluated and the lower rows specify the actions to be taken when an evaluation test is satisfied.
- A decision table can be used to model complicated logic, such as business rules, and to test the system behavior for different input combinations  .
- A decision table can also be used to make a make-buy decision, which is a choice between developing a software product in-house or purchasing it from an external vendor.
- A decision table consists of four quadrants: condition stubs, condition entries, action stubs, and action entries .
- Condition stubs are the names of the variables or conditions to be evaluated .
- Condition entries are the possible values or states of the condition stubs .
- Action stubs are the names of the actions to be taken .
- Action entries are the indicators of whether an action is performed or not for a given combination of condition entries .
- A decision table can have different types of rules, such as limited entry, extended entry, and mixed entry .
- Limited entry rules have only two possible values for each condition entry and action entry, such as Y (yes) or N (no) .
- Extended entry rules have more than two possible values for each condition entry and action entry, such as A, B, C, etc. .
- Mixed entry rules have a combination of limited and extended entries in the same table .
- A decision table can be simplified by eliminating impossible, redundant, or conflicting rules .
- A decision table can be represented graphically as a decision tree, which is a hierarchical structure of nodes and branches that show the logical flow of the decision making process .

Here is an example of a decision table for testing the eligibility of a loan applicant:

| Condition Stubs | C1: Age >= 18 | C2: Income >= 25K | C3: Credit Score >= 700 |
|-----------------|---------------|-------------------|-------------------------|
| Rule 1          | Y             | Y                 | Y                       |
| Rule 2          | Y             | Y                 | N                       |
| Rule 3          | Y             | N                 | Y                       |
| Rule 4          | Y             | N                 | N                       |
| Rule 5          | N             | Y                 | Y                       |
| Rule 6          | N             | Y                 | N                       |
| Rule 7          | N             | N                 | Y                       |
| Rule 8          | N             | N                 | N                       |

| Action Stubs | A1: Approve Loan | A2: Reject Loan |
|--------------|------------------|-----------------|
| Rule 1       | Y                | N               |
| Rule 2       | N                | Y               |
| Rule 3       | N                | Y               |
| Rule 4       | N                | Y               |
| Rule 5       | N                | Y               |
| Rule 6       | N                | Y               |
| Rule 7       | N                | Y               |
| Rule 8       | N                | Y               |

Here is the same decision table represented as a decision tree:

![Decision Tree](https://www.guru99.com/images/1/decision-tree.png)