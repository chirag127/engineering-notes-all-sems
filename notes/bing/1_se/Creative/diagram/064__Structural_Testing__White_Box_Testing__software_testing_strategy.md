Structural testing, also known as white box testing, is a software testing strategy that tests the internal structure, design, and implementation of an application, using the knowledge of the source code and programming skills. Structural testing can be applied at different levels of testing, such as unit, integration, and system testing. The main objective of structural testing is to verify the code coverage, such as statements, branches, paths, and conditions.

The following diagram illustrates the basic steps of structural testing:

```
+----------------+       +----------------+       +----------------+
|                |       |                |       |                |
|  Test Design   | +---> |  Test Case     | +---> |  Test Execution|
|                |       |  Generation    |       |                |
+----------------+       +----------------+       +----------------+
       ^                        ^                        |
       |                        |                        v
       |                        |                +----------------+
       |                        |                |                |
       |                        |                |  Test Results  |
       |                        |                |                |
       +------------------------+----------------+----------------+
                        |
                        |
                        v
                +----------------+
                |                |
                |  Source Code   |
                |                |
                +----------------+
```

Structural testing involves the following techniques:

- Statement coverage: It measures the percentage of executable statements that are covered by the test cases.
- Branch coverage: It measures the percentage of decision outcomes (such as if-else, switch-case, etc.) that are covered by the test cases.
- Path coverage: It measures the percentage of possible paths (from entry to exit) that are covered by the test cases.
- Condition coverage: It measures the percentage of logical conditions (such as AND, OR, etc.) that are evaluated to both true and false by the test cases.