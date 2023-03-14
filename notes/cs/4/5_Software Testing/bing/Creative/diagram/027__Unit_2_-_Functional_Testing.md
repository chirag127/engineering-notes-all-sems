## Unit 2 - Functional Testing

Functional testing is a type of software testing that validates the software system against the functional requirements/specifications. The purpose of functional tests is to test each function of the software application, by providing appropriate input, verifying the output against the functional requirements.

Functional testing mainly involves black box testing and it is not concerned about the source code of the application. This testing checks User Interface, APIs, Database, Security, Client/Server communication and other functionality of the Application Under Test.

The following diagram illustrates the basic architecture of a functional testing process:

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Test Case      |     |  Test Data      |     |  Expected       |
|  Design         |     |  Preparation    |     |  Results        |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
       |                     |                       |
       |                     |                       |
       |                     |                       |
       |                     |                       |
       |                     |                       |
       |                     |                       |
       |                     |                       |
       |                     |                       |
       |                     |                       |
       |                     |                       |
       |                     |                       |
       |                     |                       |
       |                     |                       |
       |                     |                       |
       |                     |                       |
       |                     |                       |
       |                     |                       |
       |                     |                       |
       |                     |                       |
       |                     |                       |
       V                     V                       V
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Test Case      |     |  Test Data      |     |  Expected       |
|  Execution      |     |  Injection      |     |  Verification   |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
       |                     |                       |
       |                     |                       |
       |                     |                       |
       |                     |                       |
       |                     |                       |
       |                     |                       |
       |                     |                       |
       |                     |                       |
       |                     |                       |
       |                     |                       |
       |                     |                       |
       V                     V                       V
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Test Case      |     |  Actual         |     |  Test Case      |
|  Reporting      |     |  Results        |     |  Evaluation     |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
```

The diagram shows the following steps:

- Test Case Design: This is the phase where the test cases are designed based on the functional requirements/specifications. Test cases are the set of conditions or variables under which a tester will determine whether an application, software system or one of its features is working as it was originally established for it to do.
- Test Data Preparation: This is the phase where the test data are prepared based on the test cases. Test data are the input values that are used to test the functionality of the application. Test data can be either static or dynamic, depending on the type of testing.
- Test Case Execution: This is the phase where the test cases are executed using the test data. Test case execution can be done either manually or using automation tools. The test case execution produces the actual results of the testing.
- Test Data Injection: This is the phase where the test data are injected into the application under test. Test data injection can be done either manually or using automation tools. The test data injection simulates the user input and triggers the functionality of the application.
- Expected Results Verification: This is the phase where the expected results are verified against the actual results. Expected results are the output values that are expected from the application based on the test cases and test data. Expected results verification can be done either manually or using automation tools. The expected results verification determines whether the test cases have passed or failed.
- Test Case Reporting: This is the phase where the test case execution results are reported. Test case reporting can be done either manually or using automation tools. The test case reporting provides the summary of the testing process, such as the number of test cases executed, passed, failed, etc.
- Actual Results