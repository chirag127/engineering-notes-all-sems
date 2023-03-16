### Boundary Value Analysis

- Boundary value analysis (BVA) is a black-box testing technique that focuses on testing the values at the boundaries of the input domain of a program or system.
- The rationale behind BVA is that errors are more likely to occur at the edges of the input domain, and testing these values can reveal defects that might be missed by testing values in the middle of the input domain.
- BVA can be applied to both numeric and non-numeric inputs, such as dates, strings, characters, etc.
- BVA can also be applied to outputs, such as the range of values that a function can return or the status codes that a system can generate.
- BVA can be used to design test cases at different levels of testing, such as unit testing, integration testing, system testing, and acceptance testing.

#### Steps for BVA

- Identify the input domain of the program or system under test.
- Identify the boundaries of the input domain, such as the minimum and maximum values, or the first and last elements of a list or array.
- Identify the valid and invalid partitions of the input domain, such as the range of values that are accepted or rejected by the program or system.
- Design test cases that cover the boundary values of each partition, such as the minimum, maximum, and just above and below the boundary values for valid partitions, and the values on and off the boundary for invalid partitions.
- Execute the test cases and compare the actual results with the expected results.

#### Example of BVA

- Suppose we have a program that calculates the discount for a customer based on the number of items purchased. The program accepts an integer input between 1 and 100, and returns a percentage discount as follows:

| Number of items | Discount |
| --------------- | -------- |
| 1-10            | 0%       |
| 11-50           | 10%      |
| 51-100          | 20%      |

- The input domain of the program is the integer values between 1 and 100, and the output domain is the percentage values between 0% and 20%.
- The boundaries of the input domain are 1, 10, 11, 50, 51, and 100. The boundaries of the output domain are 0%, 10%, and 20%.
- The valid partitions of the input domain are 1-10, 11-50, and 51-100. The invalid partitions of the input domain are <1 and >100.
- The valid partitions of the output domain are 0%, 10%, and 20%. The invalid partitions of the output domain are <0% and >20%.
- The test cases for BVA are as follows:

| Test case ID | Input | Expected output |
| ------------ | ----- | --------------- |
| TC1          | 1     | 0%              |
| TC2          | 10    | 0%              |
| TC3          | 11    | 10%             |
| TC4          | 50    | 10%             |
| TC5          | 51    | 20%             |
| TC6          | 100   | 20%             |
| TC7          | 0     | Invalid input   |
| TC8          | 101   | Invalid input   |
| TC9          | -1    | Invalid input   |
| TC10         | 9     | 0%              |
| TC11         | 12    | 10%             |
| TC12         | 49    | 10%             |
| TC13         | 52    | 20%             |
| TC14         | 99    | 20%             |