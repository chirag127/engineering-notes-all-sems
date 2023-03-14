Function Point (FP) Based Measures are a way of estimating the size and complexity of a software project based on the functionality that the user requests and receives. They are calculated by counting the number and type of external inputs, outputs, inquiries, files and interfaces that the software interacts with, and applying a complexity adjustment factor based on 14 general system characteristics. The result is a dimensionless number that can be used to compare different software projects or to estimate the cost, effort and duration of a project.

The following diagram illustrates the basic architecture of a Function Point (FP) Based Measure in software design:

```
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  External       |    |  External       |    |  External       |
|  Input (EI)     |    |  Output (EO)    |    |  Inquiry (EQ)   |
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
       V                      V                      V
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Internal       |    |  External       |    |  Complexity     |
|  Logical File   |    |  Interface File |    |  Adjustment     |
|  (ILF)          |    |  (EIF)          |    |  Factor (CAF)   |
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
       V                      V                      V
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Unadjusted     |    |  Function       |    |  Function Point |
|  Function Point |    |  Point (FP)     |    |  (FP)           |
|  (UFP)          |    |                 |    |                 |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
```