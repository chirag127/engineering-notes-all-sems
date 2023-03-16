# Boundary Value Analysis

- Boundary value analysis (BVA) is a technique for designing test cases based on the values at the boundaries of input domains or output ranges.
- BVA is based on the assumption that errors are more likely to occur at the boundaries than in the interior of the input or output domains.
- BVA can be applied to both valid and invalid input domains, as well as output ranges.
- BVA can be used to test both single and multiple input parameters, as well as equivalence classes.

## Steps for BVA

- Identify the input domains or output ranges of the system under test (SUT).
- Identify the boundaries of each input domain or output range. These include the minimum and maximum values, as well as any values just above or below the boundaries (called off-by-one values).
- Design test cases using the boundary values and the off-by-one values as inputs or expected outputs.
- Execute the test cases and compare the actual outputs with the expected outputs.

## Example of BVA

- Suppose the SUT is a function that calculates the discount for a customer based on the number of items purchased. The input domain is the number of items, and the output range is the discount percentage. The input domain and output range are divided into the following equivalence classes:

| Number of items | Discount |
| --------------- | -------- |
| < 1             | Invalid  |
| 1 - 10          | 0%       |
| 11 - 20         | 10%      |
| 21 - 50         | 20%      |
| > 50            | 30%      |

- The boundaries of the input domain are 1, 10, 11, 20, 21, and 50. The off-by-one values are 0, 9, 12, 19, 22, and 51. The boundaries of the output range are 0%, 10%, 20%, and 30%. The off-by-one values are -1%, 9%, 11%, 19%, 21%, 29%, and 31%.
- The test cases for BVA are:

| Test case | Number of items | Expected discount |
| --------- | --------------- | ----------------- |
| TC1       | 0               | Invalid           |
| TC2       | 1               | 0%                |
| TC3       | 9               | 0%                |
| TC4       | 10              | 0%                |
| TC5       | 11              | 10%               |
| TC6       | 12              | 10%               |
| TC7       | 19              | 10%               |
| TC8       | 20              | 10%               |
| TC9       | 21              | 20%               |
| TC10      | 22              | 20%               |
| TC11      | 49              | 20%               |
| TC12      | 50              | 20%               |
| TC13      | 51              | 30%               |

- The test cases for BVA can be executed and the actual outputs can be compared with the expected outputs to verify the correctness of the SUT.