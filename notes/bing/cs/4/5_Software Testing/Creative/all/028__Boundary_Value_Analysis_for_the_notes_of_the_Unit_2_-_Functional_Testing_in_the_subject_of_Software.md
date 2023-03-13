### Boundary Value Analysis for the notes of the Unit 2 - Functional Testing in the subject of Software Testing

- Boundary Value Analysis (BVA) is a black-box testing technique that focuses on testing the values at the boundaries of the input domain of a software system.
- The idea behind BVA is that errors are more likely to occur at the edges of the input domain than in the center, so testing the boundary values can reveal more defects than testing the normal values.
- BVA can be applied to any input domain that has a finite and ordered set of values, such as numbers, dates, strings, etc.
- BVA can also be applied to output domain, where the expected output values are compared with the actual output values at the boundaries of the output domain.
- BVA can be used to test both valid and invalid input values, as well as equivalence classes of input values.
- BVA can be performed at different levels of testing, such as unit testing, integration testing, system testing, etc.

#### Steps of BVA

- Identify the input domain of the software system and divide it into equivalence classes based on the specifications or requirements.
- Identify the boundary values of each equivalence class, such as minimum, maximum, just above, just below, etc.
- Design test cases using the boundary values of each equivalence class, as well as the boundary values of the input domain as a whole.
- Execute the test cases and compare the actual output with the expected output.
- Report any defects or discrepancies found during the testing.

#### Example of BVA

- Suppose we have a software system that accepts an integer input between 1 and 100 and returns the square of the input.
- The input domain can be divided into three equivalence classes: valid input (1 to 100), invalid input below the minimum (less than 1), and invalid input above the maximum (greater than 100).
- The boundary values of each equivalence class are:

| Equivalence Class | Boundary Values |
|-------------------|-----------------|
| Valid input       | 1, 100, 2, 99   |
| Invalid input below the minimum | 0, -1, -2 |
| Invalid input above the maximum | 101, 102, 103 |

- The boundary values of the input domain as a whole are: 1, 100, 0, 101.
- The test cases using the boundary values are:

| Test Case | Input | Expected Output | Actual Output | Result |
|-----------|-------|-----------------|---------------|--------|
| TC1       | 1     | 1               | 1             | Pass   |
| TC2       | 100   | 10000           | 10000         | Pass   |
| TC3       | 2     | 4               | 4             | Pass   |
| TC4       | 99    | 9801            | 9801          | Pass   |
| TC5       | 0     | Error message   | Error message | Pass   |
| TC6       | -1    | Error message   | Error message | Pass   |
| TC7       | -2    | Error message   | Error message | Pass   |
| TC8       | 101   | Error message   | Error message | Pass   |
| TC9       | 102   | Error message   | Error message | Pass   |
| TC10      | 103   | Error message   | Error message | Pass   |

- All the test cases pass, so no defects are found in the software system.

#### Advantages of BVA

- BVA is a simple and effective technique that can reveal many defects in the software system.
- BVA can reduce the number of test cases required to cover the input domain, as compared to exhaustive testing or random testing.
- BVA can increase the test coverage and the confidence in the software quality.
- BVA can be easily automated and integrated with other testing techniques.

#### Disadvantages of BVA

- BVA may not be able to detect all the defects in the software system, especially those that are not related to the boundary values or the input domain.
- BVA may not be applicable to some input domains that do not have a finite and ordered set of values, such as complex data structures, images, etc.
- BVA may not be sufficient to test the functionality and usability of the software system, as it does not consider the user's perspective or expectations.