#### Unit Tests with MR Unit

Here is an ASCII diagram that represents the process of unit testing with MR Unit:

```
+----------------+      +----------------+
|                |      |                |
|   Test Case    |      |   Test Runner  |
|                |      |                |
+-------+--------+      +--------+-------+
        |                        |
        |                        |
        |                        |
        v                        v
+-------+--------+      +--------+-------+
|                |      |                |
|   Test Suite   |      |   Test Result  |
|                |      |                |
+----------------+      +----------------+
```

In this diagram, the test case is the individual unit test that is written to test a specific functionality. The test suite is a collection of test cases that are run together. The test runner is the tool that runs the test suite and generates the test result, which shows whether the tests passed or failed.
