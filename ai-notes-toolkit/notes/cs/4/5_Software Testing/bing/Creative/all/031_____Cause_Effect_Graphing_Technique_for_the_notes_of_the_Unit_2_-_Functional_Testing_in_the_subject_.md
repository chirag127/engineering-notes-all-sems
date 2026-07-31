# Cause Effect Graphing Technique

- Cause Effect Graphing Technique is a black box testing technique that illustrates the relationship between a outcome and the factors influencing the outcome graphically  .
- It is also known as Ishikawa diagram or fish bone diagram.
- It is generally used for hardware testing but now adapted to software testing, usually tests external behavior of a system.
- It starts with a set of requirements and determines the minimum possible test cases for maximum test coverage which reduces test execution time and cost.
- It involves the following steps  :
  - Identify the causes (input conditions) and effects (output conditions) for the system under test.
  - Draw a cause-effect graph that shows the logical relationships between the causes and effects using symbols such as AND, OR, NOT, etc.
  - Assign a unique identifier to each cause and effect.
  - Convert the cause-effect graph into a decision table that lists all possible combinations of causes and effects.
  - Simplify the decision table by eliminating redundant or invalid combinations.
  - Generate test cases from the decision table by selecting one test case for each column of the table.
- An example of cause-effect graphing technique for the triangle problem is shown below:

![Cause-effect graph for triangle problem](https://www.softwaretestingclass.com/wp-content/uploads/2014/01/Cause-Effect-Graph-Testing-Technique-1.png)

- The corresponding decision table and test cases are shown below:

![Decision table for triangle problem](https://www.softwaretestingclass.com/wp-content/uploads/2014/01/Cause-Effect-Graph-Testing-Technique-2.png)

![Test cases for triangle problem](https://www.softwaretestingclass.com/wp-content/uploads/2014/01/Cause-Effect-Graph-Testing-Technique-3.png)

- The advantages of cause-effect graphing technique are :
  - It helps to identify the root causes of a problem and the possible solutions.
  - It helps to reduce the number of test cases by eliminating redundant or invalid combinations.
  - It helps to ensure the completeness and consistency of the requirements.
  - It helps to improve the communication and collaboration among the stakeholders.
- The disadvantages of cause-effect graphing technique are :
  - It may be difficult to draw the cause-effect graph for complex systems with many causes and effects.
  - It may be time-consuming and tedious to convert the cause-effect graph into a decision table and test cases.
  - It may not be able to handle the dynamic behavior of the system or the dependencies among the causes and effects.