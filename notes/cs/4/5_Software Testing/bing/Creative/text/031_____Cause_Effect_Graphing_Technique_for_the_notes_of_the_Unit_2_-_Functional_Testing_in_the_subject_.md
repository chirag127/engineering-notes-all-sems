### Cause Effect Graphing Technique

- Cause Effect Graphing Technique is a black box testing technique that illustrates the relationship between a outcome and the factors influencing the outcome graphically .
- It is also known as Ishikawa diagram or fish bone diagram.
- It is generally used for hardware testing but now adapted to software testing, usually tests external behavior of a system.
- It is a technique that starts with a set of requirements and determines the minimum possible test cases for maximum test coverage which reduces test execution time and cost.
- It involves the following steps :
  - Identify the causes (input conditions) and effects (output conditions) for the system under test.
  - Draw a cause-effect graph that shows the logical relationship between the causes and effects using symbols such as AND, OR, NOT, etc.
  - Assign a unique identifier to each cause and effect.
  - Convert the cause-effect graph into a decision table that lists all the possible combinations of causes and effects.
  - Simplify the decision table by eliminating redundant or invalid cases.
  - Derive test cases from the decision table by covering each column with at least one test case.
- An example of cause-effect graphing technique for the triangle problem is shown below:

![Cause-effect graph for triangle problem](https://www.softwaretestingclass.com/wp-content/uploads/2014/01/Cause-Effect-Graph-Testing-Technique-1.png)

- The decision table for the above graph is:

| C1 | C2 | C3 | C4 | C5 | E1 | E2 | E3 | E4 |
|----|----|----|----|----|----|----|----|----|
| T  | T  | T  | T  | T  | T  | F  | F  | F  |
| T  | T  | T  | T  | F  | F  | T  | F  | F  |
| T  | T  | T  | F  | T  | F  | F  | T  | F  |
| T  | T  | T  | F  | F  | F  | F  | F  | T  |
| T  | T  | F  | -  | -  | F  | F  | F  | F  |
| T  | F  | T  | -  | -  | F  | F  | F  | F  |
| F  | T  | T  | -  | -  | F  | F  | F  | F  |
| F  | F  | F  | -  | -  | F  | F  | F  | F  |

- The test cases for the above table are:

| Test Case | C1 | C2 | C3 | C4 | C5 | Expected Output |
|-----------|----|----|----|----|----|-----------------|
| TC1       | T  | T  | T  | T  | T  | Equilateral     |
| TC2       | T  | T  | T  | T  | F  | Isosceles       |
| TC3       | T  | T  | T  | F  | T  | Isosceles       |
| TC4       | T  | T  | T  | F  | F  | Scalene         |
| TC5       | T  | T  | F  | -  | -  | Not a triangle  |
| TC6       | T  | F  | T  | -  | -  | Not a triangle  |
| TC7       | F  | T  | T  | -  | -  | Not a triangle  |
| TC8       | F  | F  | F  | -  | -  | Not a triangle  |