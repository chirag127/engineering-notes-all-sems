Testing Objectives in Software Testing are the goals and expectations that guide the testing process and its outcomes. Some of the common objectives are:

- To check whether the software meets the requirements and specifications
- To find and fix defects before the software is delivered to the customers
- To gain confidence in and provide information about the quality and reliability of the software
- To prevent defects from occurring or recurring in the future
- To ensure that the software is usable, secure, efficient and maintainable

The following diagram illustrates the basic architecture of a software testing process using ASCII art:

### Testing Objectives in Software Testing

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Requirements   |     |   Test Cases    |     |   Test Data     |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        V                      V                      V
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|   Test Plan     |---->|   Test Suite    |---->|   Test Script   |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        V                      V                      V
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|   Test Runner   |---->|   Test Report   |---->|   Test Result   |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
```

The diagram shows the following steps:

- The requirements are the expectations and specifications of the software that are defined by the stakeholders and customers.
- The test cases are the scenarios and conditions that are used to verify the requirements and find defects in the software.
- The test data are the inputs and outputs that are used to execute the test cases and simulate the real-world situations.
- The test plan is the document that describes the scope, objectives, strategy, resources, schedule and risks of the testing process.
- The test suite is the collection of test cases that are grouped by functionality, feature, module or component of the software.
- The test script is the code or command that automates the execution of the test cases and test data.
- The test runner is the tool or framework that runs the test script and interacts with the software under test.
- The test report is the document that summarizes the test execution, test coverage, test metrics and test findings.
- The test result is the outcome of the test execution, which can be pass, fail, error or skip.