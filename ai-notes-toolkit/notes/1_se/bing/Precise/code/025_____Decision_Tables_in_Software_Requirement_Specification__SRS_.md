### Decision Tables in Software Requirement Specification (SRS)

A decision table is a tool used in software requirement specification (SRS) to represent complex business rules and logic in a tabular format. It is a structured way of organizing and representing the different combinations of conditions and the resulting actions.

Here is an example of a decision table:

| Condition 1 | Condition 2 | Condition 3 | Action |
|-------------|-------------|-------------|--------|
| T           | T           | T           | A1     |
| T           | T           | F           | A2     |
| T           | F           | T           | A3     |
| T           | F           | F           | A4     |
| F           | T           | T           | A5     |
| F           | T           | F           | A6     |
| F           | F           | T           | A7     |
| F           | F           | F           | A8     |

In this example, there are three conditions and eight possible combinations of these conditions. For each combination, there is a corresponding action. The decision table helps to ensure that all possible combinations of conditions are considered and that the resulting actions are well-defined.

Decision tables can be used in the SRS to specify the behavior of the system in different scenarios. They can also be used by developers and testers to ensure that the system is implemented and tested correctly.