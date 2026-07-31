### Decision Tables in Software Requirement Specification (SRS)

A decision table is a tabular representation of the conditions and actions of a system. It is used to specify the behavior of a system in a structured and organized manner. Here is an example of a decision table:

```
+----------------+------------+------------+------------+
| Condition      | Case 1     | Case 2     | Case 3     |
+----------------+------------+------------+------------+
| Input A        | True       | False      | True       |
| Input B        | False      | True       | True       |
+----------------+------------+------------+------------+
| Action X       | Perform    | Don't      | Perform    |
| Action Y       | Don't      | Perform    | Perform    |
+----------------+------------+------------+------------+
```

In this example, the decision table specifies the behavior of a system with two inputs (A and B) and two actions (X and Y). The table shows that when input A is true and input B is false (Case 1), the system should perform action X but not action Y. Similarly, when input A is false and input B is true (Case 2), the system should perform action Y but not action X. When both inputs are true (Case 3), the system should perform both actions.

Decision tables are commonly used in software requirement specification (SRS) documents to specify the behavior of a system in a clear and concise manner. They can help to reduce ambiguity and improve the communication between the development team and the stakeholders.
