 Here is the content in markdown format for ## Unit 2 - Functional Testing:

## Unit 2 - Functional Testing

Functional testing is a type of black-box testing that bases its test cases on the specifications of the software component under test. Functions are tested by feeding them input and examining the output, and internal program structure is rarely considered. This tutorial covers the following topics related to functional testing:

1. Test case design techniques:
- Equivalence partitioning: Dividing the input data into partitions where each partition is expected to exhibit the same functionality.
- Boundary value analysis: Testing boundary values of equivalence partitions.
- Decision table testing: Systematically testing different combinations of inputs and conditions.

2. Test coverage criteria:
- Statement coverage: Ensuring each executable statement in the program is executed at least once.
- Decision coverage: Ensuring each decision takes all possible outcomes at least once.
- Condition coverage: Ensuring each logical condition in a decision takes all possible outcomes at least once.
- Modified condition/decision coverage (MC/DC): Ensuring each condition in a decision takes True/False and each decision takes all possible outcomes at least once.

3. Functional test automation: Using automated testing tools to facilitate repetitive testing and increase test coverage. This includes tools like Selenium, Watir, etc. to automate web application testing.

Advantages:
- Checks compliance to functional requirements.
- Easy to understand and create test cases.
- Works at the user level and does not require knowledge of code.

Disadvantages:
- May not detect certain defects like memory leaks or thread safety issues.
- Time-consuming to execute large test suites and track results.
- Difficult to achieve high test coverage.

[Detailed diagrams and examples can be included here if helpful for learning]