Structural testing is a software testing approach that tests the code structure and intended system flows. It is also known as white-box testing or glass-box testing. It involves the development team members in the testing team and requires a good understanding of the programming language in which the code has been written. Structural testing is the opposite of behavioral testing, which tests the functionality of the system without looking at the internal structure.

There are different types of structural testing, such as statement coverage, branch coverage, path coverage, condition coverage, data flow testing, slice-based testing, and mutation testing. Each type has its own criteria and techniques to derive test cases and measure the test coverage.

The following diagram illustrates the basic steps of structural testing:

```
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|  Source code   |----->|  Test cases    |----->|  Test results  |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
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
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|  Code metrics  |<-----|  Test coverage |<-----|  Test analysis |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
```

The diagram shows that the source code is used to generate test cases, which are then executed to produce test results. The test results are analyzed to measure the test coverage, which indicates how much of the code structure has been tested. The test coverage is also used to calculate code metrics, such as cyclomatic complexity, which measures the number of linearly independent paths through the code. The code metrics can help to identify the areas of the code that are more prone to errors or need more testing.