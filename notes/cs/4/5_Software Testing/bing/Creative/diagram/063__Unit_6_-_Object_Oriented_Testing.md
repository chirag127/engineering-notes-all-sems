The following is a possible ascii diagram for Unit 6 - Object Oriented Testing. It shows the relationship between different classes and objects involved in the testing process, such as Test Case, Test Suite, Test Runner, Test Result, and Test Report. It also shows the attributes and methods of each class and object, as well as the messages and associations between them.

## Unit 6 - Object Oriented Testing

+----------------+       +----------------+       +----------------+
|   Test Case    |       |   Test Suite   |       |  Test Runner   |
+----------------+       +----------------+       +----------------+
| - name         |       | - name         |       | - name         |
| - description  |       | - description  |       | - description  |
| - input        |       | - testCases    |       | - testSuite    |
| - expected     |       |                |       | - testResult   |
| - actual       |       |                |       |                |
+----------------+       +----------------+       +----------------+
| + setUp()      |       | + addTestCase()|       | + run()        |
| + tearDown()   |       | + removeTestCase()     | + generateReport()
| + execute()    |       | + execute()    |       |                |
| + verify()     |       |                |       |                |
+----------------+       +----------------+       +----------------+
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       v                       v                       v
+----------------+       +----------------+       +----------------+
|   Test Case    |       |   Test Suite   |       |  Test Runner   |
|   Object       |       |   Object       |       |  Object        |
+----------------+       +----------------+       +----------------+
| - name         |       | - name         |       | - name         |
| - description  |       | - description  |       | - description  |
| - input        |       | - testCases    |       | - testSuite    |
| - expected     |       |                |       | - testResult   |
| - actual       |       |                |       |                |
+----------------+       +----------------+       +----------------+
| + setUp()      |       | + addTestCase()|       | + run()        |
| + tearDown()   |       | + removeTestCase()     | + generateReport()
| + execute()    |       | + execute()    |       |                |
| + verify()     |       |                |       |                |
+----------------+       +----------------+       +----------------+
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       v                       v                       v
+----------------+       +----------------+       +----------------+
|   Test Result  |       |   Test Report  |       |  Test Report   |
+----------------+       +----------------+       |  Generator     |
| - name         |       | - name         |       +----------------+
| - description  |       | - description  |       | - name         |
| - testCases    |       | - testResult   |       | - description  |
| - passed       |       | - summary      |       | - testResult   |
| - failed       |       | - details      |       | - testReport   |
| - errors       |       |                |       |                |
+----------------+       +----------------+       +----------------+
| + addTestCase()|       | + generateSummary()    | + generateReport()
| + removeTestCase()     | + generateDetails()    |                |
| + countPassed()|       |                |       |                |
| + countFailed()|       |                |       |                |
| + countErrors()|       |                |