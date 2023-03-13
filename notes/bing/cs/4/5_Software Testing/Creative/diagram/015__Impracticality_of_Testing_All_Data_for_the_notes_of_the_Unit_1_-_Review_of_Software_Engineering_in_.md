The impracticality of testing all data means that it is impossible to test a software system with every possible input and output combination, because the number of such combinations is too large and the time required to test them is too long. Testing all data would also require a testing oracle, which is a mechanism or a person that can determine the correctness of the output for a given input  .

The following diagram illustrates the impracticality of testing all data using an example of a simple program that takes two integers as input and returns their sum as output. The diagram shows that the input domain is infinite, and the output domain is also infinite. Therefore, testing all data would require infinite time and resources, which is impractical.

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Input Domain   |     |  Program Under  |     |  Output Domain  |
|                 |     |    Test (PUT)   |     |                 |
|                 |     |                 |     |                 |
|  Infinite set   |     |                 |     |  Infinite set   |
|  of integers    |     |                 |     |  of integers    |
|                 |     |                 |     |                 |
|                 |     |                 |     |                 |
|                 |     |                 |     |                 |
|                 |     |                 |     |                 |
|                 |     |                 |     |                 |
|                 |     |                 |     |                 |
|                 |     |                 |     |                 |
|                 |     |                 |     |                 |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       V                        V                        V
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Test Data      |     |  Test Cases     |     |  Expected       |
|                 |     |                 |     |  Results        |
|                 |     |                 |     |                 |
|  Finite subset  |     |  Finite subset  |     |  Finite subset  |
|  of integers    |     |  of input-output|     |  of integers    |
|                 |     |  pairs          |     |                 |
|                 |     |                 |     |                 |
|  Example:       |     |  Example:       |     |  Example:       |
|  1, 2, 3, 4, 5  |     |  1 + 2 = 3      |     |  3, 5, 6, 7, 8  |
|                 |     |  2 + 3 = 5      |     |                 |
|                 |     |  3 + 3 = 6      |     |                 |
|                 |     |  4 + 3 = 7      |     |                 |
|                 |     |  5 + 3 = 8      |     |                 |
|                 |     |                 |     |                 |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
```

The diagram shows that the test data is a finite subset of the input domain, and the test cases are a finite subset of the input-output pairs. The expected results are a finite subset of the output domain. The test data, test cases, and expected results are selected based on some criteria, such as equivalence classes, boundary values, error conditions, etc. However, these criteria cannot cover all possible scenarios, and there may be some inputs and outputs that are not tested. Therefore, testing all data is impractical and unrealistic.