### Equivalence Class Testing

- Equivalence class testing is a black box testing technique that divides the input domain of a system into classes of data that are expected to behave similarly.   
- The main idea is to select one representative value from each class as a test case, instead of testing all possible values. This reduces the number of test cases and saves time and resources.   
- Equivalence classes can be derived from the requirements specification, the design specification, or the code of the system.  
- Equivalence classes can be either valid or invalid, depending on whether they satisfy the expected conditions or not.   
- Equivalence class testing can be combined with boundary value analysis, which is another technique that focuses on testing the values at the boundaries of each class.   

#### Example

- Suppose we have a system that accepts an integer input between 1 and 100, and returns the square of the input. The input domain can be partitioned into three equivalence classes:   

  - Valid class: any integer from 1 to 100
  - Invalid class 1: any integer less than 1
  - Invalid class 2: any integer greater than 100

- We can select one value from each class as a test case, such as 50, 0, and 101. We can also test the boundary values of the valid class, such as 1, 100, and the values just outside the boundary, such as 0 and 101.   

- The expected outputs for these test cases are:

  - 50 -> 2500
  - 0 -> error message
  - 101 -> error message
  - 1 -> 1
  - 100 -> 10000
  - 0 -> error message
  - 101 -> error message

- The test cases can be represented in a table as follows:

| Test Case | Input | Expected Output |
| --------- | ----- | --------------- |
| TC1       | 50    | 2500            |
| TC2       | 0     | error message   |
| TC3       | 101   | error message   |
| TC4       | 1     | 1               |
| TC5       | 100   | 10000           |
| TC6       | 0     | error message   |
| TC7       | 101   | error message   |