### Boundary Value Analysis for the notes of the Unit 2 - Functional Testing in the subject of Software Testing

- Boundary Value Analysis (BVA) is a black-box testing technique that focuses on testing the values at the boundaries of the input domain of a software system.
- The idea behind BVA is that errors are more likely to occur at the edges of the input domain than in the middle, so testing the boundary values can reveal more defects than testing the normal values.
- BVA can be applied to both valid and invalid input values, as well as output values. For example, if a system accepts an integer input between 1 and 100, the boundary values are 1, 100, 0, and 101. Testing these values can check the robustness and reliability of the system.
- BVA can also be extended to test the values at the boundaries of the equivalence classes of the input domain. For example, if a system accepts a date input in the format DD/MM/YYYY, the equivalence classes are:

  - Valid dates: 01/01/1900 to 31/12/2099
  - Invalid dates: any date outside the valid range, or any date with an invalid format

  The boundary values for the valid dates are:

  - 01/01/1900, 31/12/2099, 31/01/1900, 28/02/1900, 29/02/1900, 01/03/1900, ..., 30/11/2099, 01/12/2099, 31/12/2099

  The boundary values for the invalid dates are:

  - 00/01/1900, 32/01/1900, 01/00/1900, 01/13/1900, 31/02/1900, 29/02/1901, ..., 31/11/2099, 01/01/2100, 31/12/1899

- BVA can be used to design test cases that cover the boundary values and their combinations. For example, for the date input system, some possible test cases are:

  - TC1: Enter 01/01/1900 and verify that the system accepts the input as valid
  - TC2: Enter 31/12/2099 and verify that the system accepts the input as valid
  - TC3: Enter 00/01/1900 and verify that the system rejects the input as invalid
  - TC4: Enter 01/01/2100 and verify that the system rejects the input as invalid
  - TC5: Enter 29/02/1900 and verify that the system accepts the input as valid
  - TC6: Enter 29/02/1901 and verify that the system rejects the input as invalid
  - TC7: Enter 31/04/2000 and verify that the system rejects the input as invalid
  - TC8: Enter 01/01/2000 and verify that the system accepts the input as valid
  - TC9: Enter 01/01/200 and verify that the system rejects the input as invalid
  - TC10: Enter 01/01/20000 and verify that the system rejects the input as invalid

- BVA can help to improve the quality and coverage of the test cases, as well as reduce the number of test cases needed to test the system. However, BVA has some limitations, such as:

  - It does not test the values in the middle of the input domain, which may also contain defects
  - It does not test the interactions between different input values, which may cause unexpected behaviors
  - It does not test the functionality or logic of the system, only the input and output values
  - It may not be applicable to some types of input values, such as strings, booleans, or complex data structures