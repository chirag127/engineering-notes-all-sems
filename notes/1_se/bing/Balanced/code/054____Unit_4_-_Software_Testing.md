## Unit 4 - Software Testing

Software testing is the process of verifying and validating that a software product meets the requirements and expectations of the stakeholders. Software testing can be performed at different levels of abstraction, such as unit testing, integration testing, system testing, and acceptance testing. Software testing can also be classified into different types, such as functional testing, non-functional testing, white-box testing, black-box testing, and grey-box testing.

One of the most common methods of software testing is writing test cases. A test case is a set of inputs, expected outputs, and execution conditions for a specific software component or feature. Test cases can be written in natural language, pseudocode, or a formal notation, such as the IEEE 829 standard. Test cases can be executed manually or automatically, using tools such as Selenium, JUnit, or TestNG.

A test case can be represented by the following template:

- Test case ID: A unique identifier for the test case
- Test case description: A brief summary of the test case purpose and scope
- Test case preconditions: The assumptions and prerequisites for the test case execution
- Test case steps: The detailed steps to perform the test case, including the inputs, actions, and expected results
- Test case postconditions: The expected state of the system after the test case execution
- Test case status: The result of the test case execution, such as pass, fail, or error

An example of a test case for a calculator application is:

- Test case ID: TC-001
- Test case description: Verify that the calculator can perform addition of two positive integers
- Test case preconditions: The calculator application is launched and ready for input
- Test case steps:
  - Step 1: Enter the first operand, such as 5, and press the + button
  - Step 2: Enter the second operand, such as 7, and press the = button
  - Step 3: Verify that the result displayed is the sum of the two operands, such as 12
- Test case postconditions: The calculator displays the correct result and is ready for the next input
- Test case status: Pass