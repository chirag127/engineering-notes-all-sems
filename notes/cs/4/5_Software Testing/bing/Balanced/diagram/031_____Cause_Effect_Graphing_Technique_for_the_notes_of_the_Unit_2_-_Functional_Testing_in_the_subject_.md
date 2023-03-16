### Cause Effect Graphing Technique

- Cause Effect Graphing Technique is a black box testing technique that graphically illustrates the relationship between a given outcome and all the factors that influence the outcome  .
- It is also known as Ishikawa diagram or fish bone diagram because of the way it looks, invented by Kaoru Ishikawa .
- It is based on a collection of requirements and used to determine minimum possible test cases which can cover a maximum test area of the software.
- The main advantage of cause-effect graph testing is, it reduces the time of test execution and cost.
- The steps involved in cause-effect graph testing are :
  - Identify the causes (input conditions) and effects (output conditions) for the system under test.
  - Draw a cause-effect graph that shows the logical relationships between the causes and effects.
  - Convert the cause-effect graph into a decision table that lists all the possible combinations of causes and effects.
  - Generate test cases from the decision table by selecting one or more true effects for each cause combination.
- An example of cause-effect graph testing is the triangle problem, where the system under test takes three sides of a triangle as input and determines whether the triangle is equilateral, isosceles, or scalene as output.
- The cause-effect graph for the triangle problem is shown below:

![Cause-effect graph for triangle problem](https://www.softwaretestingclass.com/wp-content/uploads/2014/01/Cause-Effect-Graph-Testing-Technique-1.png)

- The decision table for the triangle problem is shown below:

![Decision table for triangle problem](https://www.softwaretestingclass.com/wp-content/uploads/2014/01/Cause-Effect-Graph-Testing-Technique-2.png)

- The test cases for the triangle problem can be derived from the decision table as follows:
  - C1: Side “x” is less than sum of “y” and “z”.
  - C2: Side “y” is less than sum of “x” and “z”.
  - C3: Side “z” is less then sum of “x” and “y”.
  - C4: Side “x” is equal to side “y”.
  - C5: Side “x” is equal to side “z”.
  - E1: Not a triangle.
  - E2: Equilateral triangle.
  - E3: Isosceles triangle.
  - E4: Scalene triangle.
  - Test case 1: C1 = T, C2 = T, C3 = T, C4 = T, C5 = T, E1 = F, E2 = T, E3 = F, E4 = F (Input: 3, 3, 3; Output: Equilateral triangle)
  - Test case 2: C1 = T, C2 = T, C3 = T, C4 = T, C5 = F, E1 = F, E2 = F, E3 = T, E4 = F (Input: 3, 3, 4; Output: Isosceles triangle)
  - Test case 3: C1 = T, C2 = T, C3 = T, C4 = F, C5 = T, E1 = F, E2 = F, E3 = T, E4 = F (Input: 3, 4, 3; Output: Isosceles triangle)
  - Test case 4: C1 = T, C2 = T, C3 = T, C4 = F, C5 = F, E1 = F, E2 = F, E3 = F, E4 = T (Input: 3, 4, 5; Output: Scalene triangle)
  - Test case 5: C1 = F, C2 = T, C3 = T, C4 = F, C5 = F, E1 = T, E2 = F, E3 = F, E4 = F (Input: 7, 3, 3; Output: Not a triangle)
  - Test case 6: C1 = T, C2 = F, C3 = T, C4 = F, C5 = F, E1 = T, E2 = F, E3