## Unit 3 - Structural Testing

Structural testing is a type of software testing that uses the internal design and structure of the software for testing. It involves the development team members in the testing team, who know the code and implementation of the software. It tests different aspects of the software according to its types, such as control flow testing, data flow testing, slice based testing, and mutation testing.

The following diagram illustrates the basic architecture of a structural testing process:

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|   Test Cases    |---->|   Test Driver   |---->|   Software      |
|                 |     |                 |     |   Under Test    |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
      ^                        ^                        |
      |                        |                        |
      |                        |                        v
      |                        |                 +-----------------+
      |                        |                 |                 |
      |                        |                 |   Test Results  |
      |                        |                 |                 |
      |                        |                 |                 |
      +------------------------+-----------------+-----------------+
```

The test cases are derived from the code structure and logic of the software under test. The test driver is a program that executes the test cases and interacts with the software under test. The test results are the outputs and outcomes of the test cases, which are compared with the expected results to determine the correctness and quality of the software.