Functional Testing (Black Box Testing) is a software testing method in which the functionality of the software under test is evaluated without looking at the internal code structure, implementation details or internal paths. It is based on the software specifications and requirements and focuses on the input and output of the software. It can be applied to every level of software testing such as Unit, Integration, System and Acceptance Testing  .

#### Functional Testing (Black Box Testing) software testing strategy

The following diagram illustrates the basic architecture of a Functional Testing (Black Box Testing) software testing strategy using ASCII art:

```
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|  Test Cases    |---->|  Software      |---->|  Expected      |
|  (Input)       |     |  Under Test    |     |  Results       |
|                |     |                |     |  (Output)      |
+----------------+     +----------------+     +----------------+
       |                      |                      |
       |                      |                      |
       v                      v                      v
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|  Test Data     |---->|  Test Execution|---->|  Actual        |
|                |     |                |     |  Results       |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
       |                      |                      |
       |                      |                      |
       v                      v                      v
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|  Test Scripts  |---->|  Test Harness  |---->|  Test Report   |
|                |     |                |     |                |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
```

The diagram shows the following steps:

- Test Cases (Input): These are the scenarios or conditions that are used to verify the functionality of the software. They are derived from the software specifications and requirements and contain the expected results for each input.
- Software Under Test: This is the software application or system that is being tested for its functionality. It receives the input from the test cases and produces the output for comparison.
- Expected Results (Output): These are the expected outcomes or behaviors of the software under test for each test case. They are used to evaluate the correctness and completeness of the software functionality.
- Test Data: These are the specific values or parameters that are used as input for the test cases. They are selected to cover different scenarios and boundary conditions of the software functionality.
- Test Execution: This is the process of running the test cases on the software under test using the test data. It involves applying the input and observing the output of the software.
- Actual Results: These are the actual outcomes or behaviors of the software under test for each test case. They are compared with the expected results to determine the pass or fail status of the test case.
- Test Scripts: These are the automated or manual instructions that are used to execute the test cases on the software under test. They can be written in different languages or tools depending on the testing environment and requirements.
- Test Harness: This is the software framework or tool that is used to execute the test scripts on the software under test. It provides the interface, environment and utilities for the test execution.
- Test Report: This is the document that summarizes the results and findings of the test execution. It contains the details of the test cases, test data, test scripts, test harness, actual results, expected results, pass or fail status, defects, issues, recommendations and conclusions of the test.