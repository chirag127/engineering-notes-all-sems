### Regression Testing in Software Testing

Here is an ASCII diagram that illustrates the process of regression testing in software testing:

```
+----------------+           +----------------+
|                |           |                |
|   Code Change  +---------->+  Regression    |
|                |           |    Testing     |
|                |           |                |
+-------+--------+           +--------+-------+
        |                             |
        |                             |
        |                             |
        v                             v
+-------+--------+           +--------+-------+
|                |           |                |
|   Build Code   |           |  Test Results  |
|                |           |                |
|                |           |                |
+----------------+           +----------------+
```

In this diagram, a code change triggers the process of regression testing. The changed code is built and then tested to ensure that the changes did not introduce any new bugs or regressions. The test results are then analyzed to determine if any further action is needed.
