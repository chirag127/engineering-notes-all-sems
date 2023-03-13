### Boundary Value Analysis for the notes of the Unit 2 - Functional Testing in the subject of Software Testing

- Boundary Value Analysis (BVA) is a black-box testing technique that focuses on testing the values at the boundaries of the input domain or output range of a software system.
- The rationale behind BVA is that errors are more likely to occur at the edges of the input domain or output range, rather than in the center.
- BVA can be applied to both valid and invalid input values, as well as output values.
- BVA can be used to derive test cases for both single and multiple input variables, as well as for equivalence classes.
- BVA can be combined with other testing techniques, such as equivalence partitioning, decision tables, state transition diagrams, etc.
- BVA can help to reduce the number of test cases, while still achieving high coverage and effectiveness.

#### Steps for applying BVA

- Identify the input variables and output variables of the software system under test.
- Determine the minimum and maximum values for each input variable and output variable, as well as any other boundary values that are relevant or specified by the requirements.
- For each input variable and output variable, generate test cases using the following values:
  - The minimum value
  - The value just below the minimum value (invalid)
  - The value just above the minimum value (valid)
  - The maximum value
  - The value just below the maximum value (valid)
  - The value just above the maximum value (invalid)
- Execute the test cases and verify the expected results.

#### Example of BVA

- Suppose we have a software system that calculates the area of a rectangle, given the length and width as input variables. The requirements specify that the length and width should be positive integers between 1 and 100, inclusive. The output variable is the area, which should be a positive integer between 1 and 10000, inclusive.
- The boundary values for the input variables are: 1, 0, 2, 100, 99, 101
- The boundary values for the output variable are: 1, 0, 2, 10000, 9999, 10001
- The test cases for BVA are:

| Test Case ID | Length | Width | Expected Area | Actual Area | Pass/Fail |
|--------------|--------|-------|---------------|-------------|-----------|
| TC1          | 1      | 1     | 1             | 1           | Pass      |
| TC2          | 0      | 1     | Invalid input | Invalid input | Pass      |
| TC3          | 2      | 1     | 2             | 2           | Pass      |
| TC4          | 100    | 1     | 100           | 100         | Pass      |
| TC5          | 99     | 1     | 99            | 99          | Pass      |
| TC6          | 101    | 1     | Invalid input | Invalid input | Pass      |
| TC7          | 1      | 0     | Invalid input | Invalid input | Pass      |
| TC8          | 1      | 2     | 2             | 2           | Pass      |
| TC9          | 1      | 100   | 100           | 100         | Pass      |
| TC10         | 1      | 99    | 99            | 99          | Pass      |
| TC11         | 1      | 101   | Invalid input | Invalid input | Pass      |
| TC12         | 100    | 100   | 10000         | 10000       | Pass      |
| TC13         | 100    | 99    | 9900          | 9900        | Pass      |
| TC14         | 100    | 101   | Invalid input | Invalid input | Pass      |
| TC15         | 99     | 100   | 9900          | 9900        | Pass      |
| TC16         | 99     | 99    | 9801          | 9801        | Pass      |
| TC17         | 99     | 101   | Invalid input | Invalid input | Pass      |
| TC18         | 101    | 100   | Invalid input | Invalid input | Pass      |
| TC19         | 101    | 99    | Invalid input | Invalid input | Pass      |
| TC20         | 101    | 101   | Invalid input | Invalid input | Pass      |

- Note that some test cases are redundant, as they test