### Boundary Value Analysis for the notes of the Unit 2 - Functional Testing in the subject of Software Testing

Boundary Value Analysis is a black-box testing technique used to identify errors at the boundaries of input values. The technique involves testing at the minimum and maximum limits of input values, as well as just inside and outside of those limits. This technique is very useful in identifying errors that may not be apparent during normal testing.

#### Steps to perform Boundary Value Analysis:

1. Identify the input variables in the software under test.
2. Determine the minimum and maximum valid values for each input variable.
3. Determine values just below and above the minimum and maximum values for each input variable.
4. Develop test cases using these values.
5. Execute the test cases and identify any errors.

#### Advantages of Boundary Value Analysis:

1. Helps identify errors that may not be apparent during normal testing.
2. Increases the effectiveness of testing by focusing on the boundaries of input values.
3. Helps to save time and effort by reducing the number of test cases required.

#### Disadvantages of Boundary Value Analysis:

1. Does not guarantee that all defects will be identified.
2. Can be time-consuming if there are many input variables.
3. Requires a good understanding of the input variables and their boundaries.

#### Example:

Consider a program that accepts a weight in pounds as input and calculates the corresponding weight in kilograms. The program has the following requirements:

- The weight must be between 0 and 1000 pounds.
- The program should be able to handle decimal values.

Using boundary value analysis, we can identify the following test cases:

- Test Case 1: Weight = 0 (minimum valid value)
- Test Case 2: Weight = 0.1 (just below minimum value)
- Test Case 3: Weight = 500 (mid-range value)
- Test Case 4: Weight = 999.9 (just below maximum value)
- Test Case 5: Weight = 1000 (maximum valid value)

By testing at the boundaries of input values, we can identify any errors that may occur due to rounding errors or other issues.

#### Learning Trick:

To remember the steps to perform Boundary Value Analysis, you can use the mnemonic "IDEA":

- Identify the input variables.
- Determine the boundary values.
- Establish values just inside the boundaries.
- Analyze the results.