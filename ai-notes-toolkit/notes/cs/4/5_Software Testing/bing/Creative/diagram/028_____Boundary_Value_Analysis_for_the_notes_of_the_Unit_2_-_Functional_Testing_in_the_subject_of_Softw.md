### Boundary Value Analysis for the notes of the Unit 2 - Functional Testing in the subject of Software Testing

- Boundary value analysis (BVA) is a software testing technique in which tests are designed to include representatives of boundary values in a range.
- Boundary values are the values at the edges or limits of an equivalence class or a valid or invalid input domain.
- The idea behind BVA is that the behavior of the software is more likely to be incorrect at the boundaries than within the equivalence classes.
- BVA can be applied to both input and output values of the software.
- BVA can help to reduce the number of test cases by focusing on the most critical values.
- BVA can also help to detect errors and bugs that may occur between the extreme limits or boundaries of the software.

#### Steps to perform BVA

- Identify the equivalence classes for the input and output values of the software.
- Select the minimum and maximum values for each equivalence class.
- Select the values just above and below the minimum and maximum values for each equivalence class.
- Design test cases using the selected boundary values as inputs and outputs.
- Execute the test cases and verify the results.

#### Example of BVA

- Suppose we have a software that accepts an integer input between 1 and 100 and returns the square of the input.
- The equivalence classes for the input are: valid (1 to 100) and invalid (<1 or >100).
- The boundary values for the input are: 0, 1, 2, 99, 100, 101.
- The boundary values for the output are: 1, 4, 9801, 10000, 10201.
- The test cases using BVA are:

| Test Case ID | Input | Expected Output | Actual Output | Result |
|--------------|-------|-----------------|---------------|--------|
| TC1          | 0     | Invalid input   | Invalid input | Pass   |
| TC2          | 1     | 1               | 1             | Pass   |
| TC3          | 2     | 4               | 4             | Pass   |
| TC4          | 99    | 9801            | 9801          | Pass   |
| TC5          | 100   | 10000           | 10000         | Pass   |
| TC6          | 101   | Invalid input   | Invalid input | Pass   |