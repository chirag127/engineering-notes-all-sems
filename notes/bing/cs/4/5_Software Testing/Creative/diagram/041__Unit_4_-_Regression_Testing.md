## Unit 4 - Regression Testing

Regression testing is a type of software testing that verifies that a recent program or code change has not adversely affected existing features. Regression testing is performed to ensure that the software works fine with new functionality, bug fixes, or any change in the existing feature.

The following diagram illustrates the basic architecture of a regression testing process:

```
+----------------+        +----------------+        +----------------+
|                |        |                |        |                |
|  Test Cases    +------->+  Test Suite    +------->+  Test Report   |
|                |        |                |        |                |
+----------------+        +----------------+        +----------------+
       ^                         ^                         ^
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
+----------------+        +----------------+        +----------------+
|                |        |                |        |                |
|  Code Change   +------->+  Test Execution+------->+  Bug Fixing    |
|                |        |                |        |                |
+----------------+        +----------------+        +----------------+
```

The diagram shows the following steps:

- A code change is made in the software, which may introduce new bugs or affect existing features.
- A test execution is performed, which runs a test suite that contains a selection of test cases that cover the affected features and functionalities.
- A test report is generated, which shows the results of the test execution, such as passed, failed, or skipped test cases.
- A bug fixing is done, which resolves any defects or issues found in the test report.
- A regression testing is performed, which re-runs the test suite to verify that the bug fixing has not caused any new defects or affected any existing features. The test report is updated accordingly.

The regression testing process is repeated until the software meets the quality and functionality requirements. Regression testing can be done manually or automatically, depending on the complexity and scope of the software. Regression testing can also be done at different levels, such as unit, integration, system, or acceptance testing.