# Cause Effect Graphing Technique

- Cause Effect Graphing Technique is a black box testing technique that graphically illustrates the relationship between a given outcome and all the factors that influence the outcome  .
- It is also known as Ishikawa diagram or fish bone diagram because of the way it looks . It was invented by Kaoru Ishikawa.
- It is based on a collection of requirements and used to determine minimum possible test cases which can cover a maximum test area of the software. The main advantage of cause-effect graph testing is, it reduces the time of test execution and cost.
- The steps involved in cause-effect graph testing are  :
  - Identify the causes (input conditions) and effects (output conditions) for the system under test.
  - Draw a cause-effect graph that shows the logical relationship between the causes and effects using symbols such as AND, OR, NOT, etc.
  - Convert the cause-effect graph into a decision table that lists all the possible combinations of causes and effects.
  - Generate test cases from the decision table by assigning values to the causes and verifying the effects.
- An example of cause-effect graph testing is the triangle problem, where the system under test takes three sides of a triangle as input and determines the type of triangle as output. The possible types of triangle are scalene, isosceles, equilateral, or not a triangle. The cause-effect graph and the decision table for this problem are shown below:

![Cause-effect graph for triangle problem](https://www.softwaretestingclass.com/wp-content/uploads/2014/01/Cause-Effect-Graph-Testing-Technique-1.png)

| C1 | C2 | C3 | C4 | C5 | E1 | E2 | E3 | E4 |
|----|----|----|----|----|----|----|----|----|
| T  | T  | T  | T  | T  | F  | F  | F  | T  |
| T  | T  | T  | T  | F  | F  | F  | T  | F  |
| T  | T  | T  | F  | T  | F  | F  | T  | F  |
| T  | T  | T  | F  | F  | F  | T  | F  | F  |
| T  | T  | F  | T  | T  | F  | F  | T  | F  |
| T  | T  | F  | T  | F  | F  | F  | F  | F  |
| T  | T  | F  | F  | T  | F  | F  | F  | F  |
| T  | T  | F  | F  | F  | F  | F  | F  | F  |
| T  | F  | T  | T  | T  | F  | F  | T  | F  |
| T  | F  | T  | T  | F  | F  | F  | F  | F  |
| T  | F  | T  | F  | T  | F  | F  | F  | F  |
| T  | F  | T  | F  | F  | F  | F  | F  | F  |
| T  | F  | F  | T  | T  | F  | F  | F  | F  |
| T  | F  | F  | T  | F  | F  | F  | F  | F  |
| T  | F  | F  | F  | T  | F  | F  | F  | F  |
| T  | F  | F  | F  | F  | F  | F  | F  | F  |
| F  | T  | T  | T  | T  | F  | F  | F  | F  |
| F  | T  | T  | T  | F  | F  | F  | F  | F  |
| F  | T  | T  | F  | T  | F  |