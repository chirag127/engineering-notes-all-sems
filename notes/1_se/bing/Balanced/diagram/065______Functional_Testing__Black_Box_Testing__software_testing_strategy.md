Functional testing (black box testing) is a software testing strategy that verifies the functionality of the software under test without knowing its internal structure or implementation details. It is based on the software requirements and specifications, and it checks whether the software meets the user's expectations and needs.

A possible diagram for functional testing (black box testing) software testing strategy is:

```
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  Test Cases     |       |  Software       |       |  Expected       |
|  (based on      |       |  Under Test     |       |  Results        |
|  requirements)  |       |  (SUT)          |       |  (based on      |
|                 |       |                 |       |  specifications)|
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  Input          |------>|  Functionality  |------>|  Output         |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
```

The diagram shows the input and output of the functional testing process. The input is the test cases, which are derived from the software requirements and specifications. The output is the expected results, which are also based on the software specifications. The software under test (SUT) is the application that is being tested for its functionality. The functional testing process compares the output of the SUT with the expected results, and reports any discrepancies or defects.