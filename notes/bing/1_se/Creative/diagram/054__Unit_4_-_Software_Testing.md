## Unit 4 - Software Testing

Software testing is the process of verifying and validating that a software product or service meets the specified requirements and expectations of the stakeholders. Software testing can be performed at different levels of granularity, such as unit testing, integration testing, system testing, and acceptance testing. Software testing can also follow different approaches, such as black-box testing, white-box testing, and gray-box testing. Software testing can be done manually or with the help of automated tools.

The following diagram illustrates the basic phases of a software testing process:

```
+----------------+     +----------------+     +----------------+     +----------------+
|                |     |                |     |                |     |                |
|  Requirement   |     |   Test Plan    |     |   Test Case    |     |   Test Data    |
|  Analysis      |---->|   Development  |---->|   Development  |---->|   Generation   |
|                |     |                |     |                |     |                |
+----------------+     +----------------+     +----------------+     +----------------+
                                                                 |
                                                                 |
                                                                 V
                                                          +----------------+
                                                          |                |
                                                          |   Test Case    |
                                                          |   Execution    |
                                                          |                |
                                                          +----------------+
                                                                 |
                                                                 |
                                                                 V
                                                          +----------------+
                                                          |                |
                                                          |   Test Result  |
                                                          |   Analysis     |
                                                          |                |
                                                          +----------------+
                                                                 |
                                                                 |
                                                                 V
                                                          +----------------+
                                                          |                |
                                                          |   Defect       |
                                                          |   Reporting    |
                                                          |                |
                                                          +----------------+
                                                                 |
                                                                 |
                                                                 V
                                                          +----------------+
                                                          |                |
                                                          |   Defect       |
                                                          |   Fixing       |
                                                          |                |
                                                          +----------------+
                                                                 |
                                                                 |
                                                                 V
                                                          +----------------+
                                                          |                |
                                                          |   Regression   |
                                                          |   Testing      |
                                                          |                |
                                                          +----------------+
                                                                 |
                                                                 |
                                                                 V
                                                          +----------------+
                                                          |                |
                                                          |   Test Report  |
                                                          |   Generation   |
                                                          |                |
                                                          +----------------+
                                                                 |
                                                                 |
                                                                 V
                                                          +----------------+
                                                          |                |
                                                          |   Test Closure |
                                                          |                |
                                                          +----------------+
```

The diagram shows the following steps:

- Requirement analysis: The process of understanding the business and technical requirements of the software product or service, and identifying the test objectives and scope.
- Test plan development: The process of defining the test strategy, test environment, test resources, test schedule, test deliverables, and test risks.
- Test case development: The process of designing and documenting the test scenarios, test steps, test inputs, and expected outputs for each test objective.
- Test data generation: The process of creating or obtaining the data sets that are required to execute the test cases.
- Test case execution: The process of running the test cases on the software product or service under test, and recording the actual outputs and test status.
- Test result analysis: The process of comparing the actual outputs with the expected outputs, and determining the test outcome (pass or fail) and test coverage.
- Defect reporting: The process of logging and tracking the defects that are found during the test case execution, and assigning them to the responsible developers or testers.
- Defect fixing: The process of resolving the defects that are reported by the testers, and verifying that they are fixed correctly.
- Regression testing: The process of re-testing the software product or service after the defects are fixed, to ensure that no new defects are introduced and the existing functionality is not affected.
- Test report generation: The process of summarizing and presenting the test results, test coverage, defect status, and test metrics in a formal document or dashboard.
- Test closure: The process of evaluating the test process and deliverables, and identifying the lessons learned and best practices for future improvement.