### Cause Effect Graphing Technique for the notes of the Unit 2 - Functional Testing in the subject of Software Testing

- Cause Effect Graphing Technique is a black box testing technique that graphically illustrates the relationship between a given outcome and all the factors that influence the outcome  .
- It is also known as Ishikawa diagram or fish bone diagram because of the way it looks, invented by Kaoru Ishikawa .
- It is based on a collection of requirements and used to determine minimum possible test cases which can cover a maximum test area of the software.
- The main advantage of cause-effect graph testing is, it reduces the time of test execution and cost.
- The steps involved in cause-effect graph testing are :
  - Identify the causes (input conditions) and effects (output conditions) for the system under test.
  - Draw a cause-effect graph that shows the logical relationship between the causes and effects using symbols such as AND, OR, NOT, etc.
  - Convert the cause-effect graph into a decision table that lists all the possible combinations of causes and effects.
  - Derive test cases from the decision table by selecting one test case for each column of the table.
- An example of cause-effect graph testing is the triangle problem, where the system under test takes three sides of a triangle as input and determines the type of triangle as output.
  - The causes are the three sides of the triangle, denoted by x, y, and z.
  - The effects are the four types of triangle, denoted by E1 (scalene), E2 (isosceles), E3 (equilateral), and E4 (not a triangle).
  - The cause-effect graph for the triangle problem is shown below:

```
    x < y + z
    / \   / \
   /   \ /   \
  /     X     \
 /     / \     \
x=y   /   \   y=z
|    /     \    |
|   /       \   |
|  /         \  |
| /           \ |
V V           V V
E3          E2
| \         / |
|  \       /  |
|   \     /   |
|    \   /    |
|     \ /     |
|      X      |
|     / \     |
|    /   \    |
|   /     \   |
|  /       \  |
| /         \ |
V/           \V
E1          E4
```

  - The decision table for the triangle problem is shown below:

| Cause | x=y | y=z | x< y+z | Effect | E1 | E2 | E3 | E4 |
|-------|-----|-----|--------|--------|----|----|----|----|
| T1    | T   | T   | T      | E3     | F  | F  | T  | F  |
| T2    | T   | F   | T      | E2     | F  | T  | F  | F  |
| T3    | F   | T   | T      | E2     | F  | T  | F  | F  |
| T4    | F   | F   | T      | E1     | T  | F  | F  | F  |
| T5    | T   | T   | F      | E4     | F  | F  | F  | T  |
| T6    | T   | F   | F      | E4     | F  | F  | F  | T  |
| T7    | F   | T   | F      | E4     | F  | F  | F  | T  |
| T8    | F   | F   | F      | E4     | F  | F  | F  | T  |

  - The test cases for the triangle problem are derived from the decision table as follows:

| Test Case | x  | y  | z  | Expected Output |
|-----------|----|----|----|-----------------|
| T1        | 5  | 5  | 5  | Equilateral     |
| T2        | 5  | 5  | 4  | Isosceles       |
| T3