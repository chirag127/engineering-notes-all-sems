### Boundary Value Analysis

- Boundary value analysis (BVA) is a black-box testing technique that focuses on testing the values at the boundaries of the input domain of a program or system.
- BVA is based on the assumption that errors are more likely to occur at the edges of the input domain than in the middle.
- BVA can be applied to both numeric and non-numeric inputs, such as dates, strings, characters, etc.
- BVA can also be applied to outputs, such as error messages, status codes, etc.
- BVA can be used to design both valid and invalid test cases, by testing the values at the valid boundaries, the invalid boundaries, and the values just inside and outside the boundaries.
- BVA can be combined with other testing techniques, such as equivalence partitioning, decision tables, state transition diagrams, etc.

#### Steps to perform BVA

- Identify the input domain of the program or system under test.
- Identify the boundaries of the input domain, such as minimum, maximum, or special values.
- Design test cases using the following values for each boundary:
  - The exact boundary value (on-point)
  - A value just below the boundary (off-point, lower)
  - A value just above the boundary (off-point, upper)
- Execute the test cases and verify the expected outputs or behaviors.

#### Example of BVA

- Consider a program that accepts an integer input between 1 and 100, and prints "Valid" if the input is within the range, and "Invalid" otherwise.
- The input domain of the program is 1 to 100, and the boundaries are 1 and 100.
- The test cases using BVA are:

| Test Case | Input | Expected Output |
|-----------|-------|-----------------|
| TC1       | 1     | Valid           |
| TC2       | 0     | Invalid         |
| TC3       | 2     | Valid           |
| TC4       | 100   | Valid           |
| TC5       | 99    | Valid           |
| TC6       | 101   | Invalid         |