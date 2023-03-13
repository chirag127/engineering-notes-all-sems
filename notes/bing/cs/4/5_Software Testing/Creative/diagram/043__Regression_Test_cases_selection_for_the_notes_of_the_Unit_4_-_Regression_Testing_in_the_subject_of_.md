Regression test cases selection is the process of choosing a subset of test cases from the original test suite to verify that the modified software behaves as expected and does not introduce any new errors. There are different techniques for selecting regression test cases, such as coverage, minimisation, and safe techniques.

The following diagram illustrates the basic architecture of a regression test cases selection process using a safe technique:

```
+-----------------+      +-----------------+      +-----------------+
| Original test   |      | Modified        |      | Regression test |
| suite           |      | program         |      | suite           |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|  T1             |      |                 |      |                 |
|  T2             |      |                 |      |                 |
|  T3             |      |                 |      |                 |
|  T4             |      |                 |      |                 |
|  T5             |      |                 |      |                 |
|  T6             |      |                 |      |                 |
|  T7             |      |                 |      |                 |
|  T8             |      |                 |      |                 |
|  T9             |      |                 |      |                 |
|  T10            |      |                 |      |                 |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
         |                      |                      ^
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
         v                      v                      |
+-----------------+      +-----------------+      +-----------------+
| Original        |      | Modified        |      | Regression test |
| program         |      | program         |      | cases selection |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|  P              |----->|  P'             |----->|  R              |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
```

The diagram shows that the original test suite T consists of 10 test cases, T1 to T10, that are used to test the original program P. The program P is modified to P' due to some changes in the requirements or the code. The regression test cases selection technique R selects a subset of test cases from T that are safe, meaning that they can detect any faults introduced by the modification. The selected test cases are then used to test the modified program P' and ensure its correctness and reliability. The selection technique R can be based on different criteria, such as code coverage, test case minimisation, or test case prioritisation.