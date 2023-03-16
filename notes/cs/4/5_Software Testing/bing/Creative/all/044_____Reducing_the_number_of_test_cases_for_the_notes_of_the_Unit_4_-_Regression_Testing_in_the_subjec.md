# Reducing the number of test cases for the notes of the Unit 4 - Regression Testing in the subject of Software Testing

- Regression testing is the process of retesting the modified or updated software to ensure that it still meets the specified requirements and does not introduce any new defects.
- Regression testing is considered to be the most expensive phase in software testing, as it requires running a large number of test cases repeatedly.
- Test case reduction is the technique of eliminating or minimizing the redundant or unnecessary test cases from the regression test suite, while preserving the fault detection capability and coverage criteria  .
- Test case reduction can save time, cost, and resources in regression testing, and improve the efficiency and effectiveness of the testing process  .
- Test case reduction can be performed manually or with the help of automated tools.
- Some of the common techniques for test case reduction are  :
  - Requirement-based: This technique selects the test cases that satisfy the testing requirements with the minimum number of test cases. It can be done by mapping the test cases to the requirements and eliminating the test cases that do not cover any requirement or cover the same requirement as another test case.
  - Coverage-based: This technique selects the test cases that ensure the maximum coverage of the code, functionality, or features with the minimum number of test cases. It can be done by measuring the coverage of each test case and eliminating the test cases that do not contribute to the coverage or have overlapping coverage with another test case.
  - Genetic algorithm: This technique uses a population-based search method that mimics the natural evolution process to find the optimal test case subset. It can be done by encoding the test cases as chromosomes, assigning fitness values based on the coverage and fault detection criteria, and applying genetic operators such as selection, crossover, and mutation to generate new test case subsets until a termination condition is met.
  - Case-based reasoning: This technique uses a memory-based approach that searches for the most similar problems and solutions to the current problem. It can be done by classifying the test cases into three categories: case, auxiliary, and pivotal. Case test cases are the ones that are most relevant to the current problem and are retained in the test suite. Auxiliary test cases are the ones that are less relevant to the current problem and are removed from the test suite. Pivotal test cases are the ones that are critical for the fault detection and are retained in the test suite.
- The effectiveness of the test case reduction technique can be evaluated by comparing the original and reduced test suites in terms of the following metrics  :
  - Reduction rate: The percentage of test cases that are eliminated from the original test suite.
  - Fault detection rate: The percentage of faults that are detected by the reduced test suite.
  - Coverage rate: The percentage of code, functionality, or features that are covered by the reduced test suite.
  - Execution time: The time required to run the reduced test suite.
  - Cost: The resources required to perform the test case reduction and execute the reduced test suite.