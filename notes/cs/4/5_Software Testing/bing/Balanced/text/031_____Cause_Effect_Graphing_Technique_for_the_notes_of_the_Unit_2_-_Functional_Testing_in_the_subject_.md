### Cause Effect Graphing Technique

- Cause Effect Graphing Technique is a black box testing technique that graphically illustrates the relationship between a given outcome and all the factors that influence the outcome  .
- It is also known as Ishikawa diagram or fish bone diagram because of the way it looks, invented by Kaoru Ishikawa .
- It is based on a collection of requirements and used to determine minimum possible test cases which can cover a maximum test area of the software .
- The main advantage of cause-effect graph testing is, it reduces the time of test execution and cost.
- The steps involved in cause-effect graph testing are :
  - Identify the causes (input conditions) and effects (output conditions) for the system under test.
  - Draw a cause-effect graph that shows the logical relationship between the causes and effects using symbols such as AND, OR, NOT, etc.
  - Convert the cause-effect graph into a decision table that lists all the possible combinations of causes and effects.
  - Derive test cases from the decision table by selecting one or more columns that cover all the causes and effects.
- An example of cause-effect graph testing is the triangle problem, where the system under test takes three sides of a triangle as input and determines whether the triangle is equilateral, isosceles, or scalene as output.
  - The causes are the three sides of the triangle (x, y, z) and the effects are the three types of triangle (equilateral, isosceles, scalene).
  - The cause-effect graph for the triangle problem is shown below:

  ```
  x < y + z
  / \   / \
 /   \ /   \
x = y x = z  \
 \   / \   / \
  \ /   \ /   \
   AND   AND   OR
    \     /    /
     \   /    /
      \ /    /
       OR   /
        \  /
         \/
    equilateral
  ```

  - The decision table for the triangle problem is shown below:

  | x < y + z | x = y | x = z | equilateral | isosceles | scalene |
  |-----------|-------|-------|-------------|-----------|---------|
  | T         | T     | T     | T           | F         | F       |
  | T         | T     | F     | F           | T         | F       |
  | T         | F     | T     | F           | T         | F       |
  | T         | F     | F     | F           | F         | T       |
  | F         | -     | -     | F           | F         | F       |

  - The test cases for the triangle problem are shown below:

  | Test Case | x | y | z | Expected Output |
  |-----------|---|---|---|-----------------|
  | TC1       | 5 | 5 | 5 | equilateral     |
  | TC2       | 5 | 5 | 4 | isosceles       |
  | TC3       | 5 | 4 | 5 | isosceles       |
  | TC4       | 5 | 4 | 3 | scalene         |
  | TC5       | 5 | 2 | 1 | invalid         |