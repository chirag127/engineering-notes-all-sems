Hello, I am Sydney, your AI assistant. I can help you with your query. Here is some information on the cause effect graphing technique for the notes of the unit 2 - functional testing in the subject of software testing.

### Cause Effect Graphing Technique

- Cause effect graphing technique is a black box testing technique that illustrates the relationship between a outcome and the factors influencing the outcome graphically .
- It is also known as Ishikawa diagram or fish bone diagram because of the way it looks, invented by Kaoru Ishikawa.
- It is generally used for hardware testing but now adapted to software testing, usually tests external behavior of a system.
- It starts with a set of requirements and determines the minimum possible test cases for maximum test coverage which reduces test execution time and cost.
- It involves the following steps :
  - Identify the causes (input conditions) and effects (output conditions) of the system under test.
  - Draw a cause effect graph using symbols such as AND, OR, NOT, etc. to represent the logical relationship between the causes and effects.
  - Assign a unique number to each cause and effect.
  - Convert the cause effect graph into a decision table by using the following rules:
    - Each column of the decision table represents a test case.
    - Each row of the decision table represents a cause or an effect.
    - A value of 0 or 1 is assigned to each cause depending on whether it is absent or present in the test case.
    - A value of T or F is assigned to each effect depending on whether it is true or false in the test case.
    - A dash (-) is assigned to a cause or an effect if it is irrelevant for the test case.
  - Simplify the decision table by eliminating duplicate or invalid test cases.
  - Derive the test cases from the decision table by providing the actual values for the causes and effects.

- Here is an example of the cause effect graphing technique for the triangle problem:

![Cause effect graph for triangle problem](https://www.softwaretestingclass.com/wp-content/uploads/2014/01/Cause-Effect-Graph-Testing-Technique-1.png)

- The decision table for the above graph is:

| C1 | C2 | C3 | C4 | C5 | E1 | E2 | E3 | E4 |
|----|----|----|----|----|----|----|----|----|
| 0  | 1  | 1  | -  | -  | F  | F  | F  | T  |
| 1  | 0  | 1  | -  | -  | F  | F  | F  | T  |
| 1  | 1  | 0  | -  | -  | F  | F  | F  | T  |
| 1  | 1  | 1  | 0  | 0  | T  | F  | F  | F  |
| 1  | 1  | 1  | 1  | 0  | F  | T  | F  | F  |
| 1  | 1  | 1  | 0  | 1  | F  | F  | T  | F  |
| 1  | 1  | 1  | 1  | 1  | F  | F  | F  | F  |

- The test cases for the above decision table are:

| Test Case | x  | y  | z  | Expected Output |
|-----------|----|----|----|-----------------|
| 1         | 1  | 3  | 4  | Not a triangle  |
| 2         | 3  | 1  | 4  | Not a triangle  |
| 3         | 3  | 4  | 1  | Not a triangle  |
| 4         | 3  | 4  | 5  | Scalene triangle|
| 5         | 3  | 3  | 5  | Isosceles triangle|
| 6         | 3  | 5  | 5  | Isosceles triangle|
| 7         | 3  | 3  | 3  | Equilateral