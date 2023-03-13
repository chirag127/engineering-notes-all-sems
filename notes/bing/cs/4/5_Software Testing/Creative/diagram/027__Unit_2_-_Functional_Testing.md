Functional testing is the process of verifying that a software system performs the functions that it is intended to do, according to the user requirements or specifications. Functional testing involves testing the functionality of the system from the user's perspective, without knowing the internal structure or logic of the code.

A typical functional testing process consists of the following steps:

- Identify the functions or features of the system that need to be tested
- Define the test scenarios or cases for each function or feature, based on the user requirements or specifications
- Prepare the test data and expected results for each test case
- Execute the test cases and compare the actual results with the expected results
- Report the defects or issues found during the test execution
- Repeat the test cycle until all the defects are fixed and the system meets the user requirements or specifications

A possible diagram for functional testing is shown below, using ASCII characters:

## Unit 2 - Functional Testing

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Test Planning  |---->|  Test Design    |---->|  Test Execution |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
                                    |                    |
                                    |                    |
                                    v                    v
                            +-----------------+     +-----------------+
                            |                 |     |                 |
                            |  Test Data      |     |  Test Results   |
                            |                 |     |                 |
                            +-----------------+     +-----------------+
                                    |                    |
                                    |                    |
                                    v                    v
                            +-----------------+     +-----------------+
                            |                 |     |                 |
                            |  Expected       |     |  Actual         |
                            |  Results        |     |  Results        |
                            |                 |     |                 |
                            +-----------------+     +-----------------+
                                    |                    |
                                    |                    |
                                    v                    v
                            +-----------------+     +-----------------+
                            |                 |     |                 |
                            |  Compare        |---->|  Report         |
                            |  Results        |     |  Defects        |
                            |                 |     |                 |
                            +-----------------+     +-----------------+
```