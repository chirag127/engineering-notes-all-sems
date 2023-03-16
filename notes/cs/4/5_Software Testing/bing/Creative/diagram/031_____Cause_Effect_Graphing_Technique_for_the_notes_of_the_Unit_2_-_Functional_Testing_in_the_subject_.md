Hello, I am Sydney, your AI assistant. I will help you with your query.

### Cause Effect Graphing Technique

- Cause Effect Graphing Technique is a black box testing technique that illustrates the relationship between a outcome and the factors influencing the outcome graphically .
- It is also known as Ishikawa diagram or fish bone diagram, invented by Kaoru Ishikawa.
- It is generally used for hardware testing but now adapted to software testing, usually tests external behavior of a system.
- It starts with a set of requirements and determines the minimum possible test cases for maximum test coverage which reduces test execution time and cost.
- It involves the following steps :
  - Identify the causes (input conditions) and effects (output conditions) for the system under test.
  - Draw a cause-effect graph that shows the logical relationship between the causes and effects using symbols such as AND, OR, NOT, etc.
  - Assign a unique identifier to each cause and effect.
  - Convert the cause-effect graph into a decision table that lists all possible combinations of causes and effects.
  - Simplify the decision table by eliminating redundant or invalid cases.
  - Derive test cases from the decision table by assigning values to the causes and verifying the effects.

- An example of cause-effect graphing technique for the triangle problem is shown below:

![Cause-effect graph for triangle problem](https://www.softwaretestingclass.com/wp-content/uploads/2014/01/Cause-Effect-Graph-Testing-Technique-1.png)

- The decision table for the above graph is:

| C1 | C2 | C3 | C4 | C5 | E1 | E2 | E3 | E4 |
|----|----|----|----|----|----|----|----|----|
| T  | T  | T  | T  | T  | T  | F  | F  | F  |
| T  | T  | T  | T  | F  | F  | T  | F  | F  |
| T  | T  | T  | F  | T  | F  | F  | T  | F  |
| T  | T  | T  | F  | F  | F  | F  | F  | T  |
| F  | T  | T  | -  | -  | F  | F  | F  | F  |
| T  | F  | T  | -  | -  | F  | F  | F  | F  |
| T  | T  | F  | -  | -  | F  | F  | F  | F  |

- The test cases for the above table are:

| Test Case | x  | y  | z  | Expected Output |
|-----------|----|----|----|-----------------|
| TC1       | 5  | 5  | 5  | Equilateral     |
| TC2       | 5  | 5  | 4  | Isosceles       |
| TC3       | 5  | 4  | 5  | Isosceles       |
| TC4       | 5  | 4  | 3  | Scalene         |
| TC5       | 5  | 4  | 10 | Not a triangle  |
| TC6       | 5  | 10 | 4  | Not a triangle  |
| TC7       | 10 | 5  | 4  | Not a triangle  |