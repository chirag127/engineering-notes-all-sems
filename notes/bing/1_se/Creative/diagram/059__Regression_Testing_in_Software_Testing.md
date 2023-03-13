Regression testing is a software testing practice that ensures an application still functions as expected after any code changes, updates, or improvements. Regression testing is responsible for the overall stability and functionality of the existing features.

There are different types of regression testing, such as corrective, progressive, selective, complete, and partial. Each type has its own advantages and disadvantages depending on the scope, complexity, and frequency of the changes.

The following diagram illustrates the basic architecture of a regression testing process using the example of a web application:

```
+----------------+    +----------------+    +----------------+
|                |    |                |    |                |
|  Source Code   |    |  Test Cases    |    |  Test Results  |
|                |    |                |    |                |
+----------------+    +----------------+    +----------------+
       |                     |                     ^
       |                     |                     |
       |                     |                     |
       v                     v                     |
+----------------+    +----------------+    +----------------+
|                |    |                |    |                |
|  Code Changes  |    |  Test Runner   |    |  Test Report   |
|                |    |                |    |                |
+----------------+    +----------------+    +----------------+
       |                     |                     ^
       |                     |                     |
       |                     |                     |
       v                     v                     |
+----------------+    +----------------+    +----------------+
|                |    |                |    |                |
|  Build System  |    |  Test Suite    |    |  Test Analysis |
|                |    |                |    |                |
+----------------+    +----------------+    +----------------+
       |                     |                     ^
       |                     |                     |
       |                     |                     |
       v                     v                     |
+----------------+    +----------------+    +----------------+
|                |    |                |    |                |
|  Web Server    |    |  Web Browser   |    |  Bug Tracking  |
|                |    |                |    |                |
+----------------+    +----------------+    +----------------+
```

The diagram shows the following steps:

- The source code is modified by the developers to implement new features or fix bugs.
- The test cases are written or updated by the testers to cover the expected behavior of the application.
- The code changes are compiled and deployed to the web server by the build system.
- The test runner executes the test suite on the web browser, which interacts with the web server and the application.
- The test results are collected and reported by the test runner, which shows the status of each test case (pass, fail, skip, etc.).
- The test report is analyzed by the testers, who verify if the application meets the requirements and if there are any regression issues.
- The bug tracking system is used to record and track any defects found during the testing process.