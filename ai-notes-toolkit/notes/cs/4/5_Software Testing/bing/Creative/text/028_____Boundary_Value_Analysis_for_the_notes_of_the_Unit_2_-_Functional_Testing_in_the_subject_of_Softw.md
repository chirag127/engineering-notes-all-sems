### Boundary Value Analysis

- Boundary value analysis (BVA) is a black-box testing technique that focuses on testing the values at the boundaries of the input domain of a program or system.
- The rationale behind BVA is that errors are more likely to occur at the edges of the input domain, rather than in the center.
- BVA can be applied to both valid and invalid input values, as well as output values.
- BVA can be used to derive test cases for both single and multiple input variables, as well as for equivalence classes and decision tables.
- BVA can be combined with other testing techniques, such as equivalence partitioning, error guessing, and cause-effect graphing, to increase the test coverage and effectiveness.

#### Steps for BVA

- Identify the input variables and their ranges.
- Divide the input domain into valid and invalid regions, and identify the boundary values for each region.
- Select test cases that include the boundary values, as well as values just above and below the boundaries.
- Execute the test cases and verify the expected results.

#### Example of BVA

- Consider a program that accepts an integer input N between 1 and 100, and prints "Valid" if N is within the range, and "Invalid" otherwise.
- The input domain can be divided into three regions: valid (1 to 100), invalid below (less than 1), and invalid above (greater than 100).
- The boundary values for each region are: 0, 1, 100, and 101.
- The test cases for BVA are:

| Test Case | Input | Expected Output |
|-----------|-------|-----------------|
| TC1       | 0     | Invalid         |
| TC2       | 1     | Valid           |
| TC3       | 100   | Valid           |
| TC4       | 101   | Invalid         |
| TC5       | -1    | Invalid         |
| TC6       | 2     | Valid           |
| TC7       | 99    | Valid           |
| TC8       | 102   | Invalid         |