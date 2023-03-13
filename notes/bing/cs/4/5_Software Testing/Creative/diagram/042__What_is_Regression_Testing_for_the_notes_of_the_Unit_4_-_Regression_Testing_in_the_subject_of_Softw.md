Regression testing is re-running functional and non-functional tests to ensure that previously developed and tested software still performs as expected after a change. Regression testing is responsible for the overall stability and functionality of the existing features. Whenever a new modification is added to the code, regression testing is applied to verify that the new code does not break or degrade the existing functionality.

The following diagram illustrates the basic process of regression testing using an example of a web application:

```
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Web Browser    |    |  Web Server     |    |  Database       |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
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
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
+------+-----+         +------+-----+         +------+-----+
| Test Case 1 |         | Test Case 2 |         | Test Case 3 |
+-------------+         +-------------+         +-------------+
| Login       |         | Search      |         | Checkout    |
+-------------+         +-------------+         +-------------+
| 1. Enter    |         | 1. Enter    |         | 1. Add      |
| username    |         | keywords    |         | items to    |
| and password|         | and click   |         | cart        |
| 2. Click    |         | search      |         | 2. Click    |
| login       |         | 2. Verify   |         | checkout    |
| 3. Verify   |         | results     |         | 3. Enter    |
| home page   |         | are relevant|         | payment     |
| is displayed|         |             |         | details     |
+-------------+         +-------------+         +-------------+
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
+------+-----+         +------+-----+         +------+-----+
| Test Result |         | Test Result |         | Test Result |
+-------------+         +-------------+         +-------------+
| Pass/Fail   |         | Pass/Fail   |         | Pass/Fail   |
+-------------+         +-------------+         +-------------+
```

The diagram shows three test cases that cover different functionalities of the web application: login, search, and checkout. Each test case has a set of steps and expected outcomes. The test results indicate whether the test case passed or failed after the code change. Regression testing aims to ensure that all the test cases pass and no regression occurs.