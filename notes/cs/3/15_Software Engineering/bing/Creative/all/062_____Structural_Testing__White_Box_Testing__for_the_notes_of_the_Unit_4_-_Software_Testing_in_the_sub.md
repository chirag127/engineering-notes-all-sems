# Structural Testing (White Box Testing)

- Structural testing, also known as white box testing, is a method of software testing that tests the internal structure, logic, and code of the software system  .
- The tester has access to the source code and can create test cases based on the code paths, branches, conditions, loops, and statements  .
- The main objective of structural testing is to verify the quality, reliability, security, and performance of the software system by checking its code coverage, data flow, control flow, and error handling  .
- Structural testing can be performed at any level of testing, such as unit testing, integration testing, system testing, or acceptance testing .
- Structural testing can be done manually or with the help of automated tools that can generate, execute, and measure test cases based on the code .

## Types of Structural Testing

- There are different types of structural testing techniques that can be used to measure the code coverage and test the software system. Some of the common types are:

  - Statement coverage: It measures the percentage of executable statements that are covered by the test cases. It ensures that every statement in the code is executed at least once.
  - Branch coverage: It measures the percentage of branches or decision points that are covered by the test cases. It ensures that every possible outcome of a branch is executed at least once.
  - Condition coverage: It measures the percentage of logical conditions that are covered by the test cases. It ensures that every possible value of a condition is tested at least once.
  - Path coverage: It measures the percentage of paths that are covered by the test cases. It ensures that every possible path from the entry point to the exit point of the code is executed at least once.
  - Loop coverage: It measures the percentage of loops that are covered by the test cases. It ensures that every loop in the code is executed with different iterations and boundary values.
  - Function coverage: It measures the percentage of functions or subroutines that are covered by the test cases. It ensures that every function in the code is called at least once.

## Advantages and Disadvantages of Structural Testing

- Structural testing has some advantages and disadvantages that should be considered before applying it to a software system  . Some of them are:

  - Advantages:
    - It helps to find errors, bugs, and defects in the code that may not be detected by functional testing .
    - It helps to improve the design, readability, maintainability, and security of the code .
    - It helps to measure the code quality, complexity, and coverage .
    - It helps to optimize the performance and efficiency of the code .
    - It helps to ensure compliance with coding standards and guidelines .
  - Disadvantages:
    - It requires access to the source code, which may not be available or feasible in some cases .
    - It requires skilled and experienced testers who can understand and analyze the code .
    - It can be time-consuming, costly, and complex to perform .
    - It can be difficult to achieve 100% code coverage, especially for large and complex systems .
    - It can miss some errors, bugs, and defects that are related to the functionality, usability, or user interface of the system .

## Example of Structural Testing

- To illustrate how structural testing can be done, let us consider a simple example of a function that calculates the factorial of a given number:

```python
def factorial(n):
  if n < 0:
    return -1
  elif n == 0 or n == 1:
    return 1
  else:
    return n * factorial(n-1)
```

- To test this function, we can use the following test cases based on the statement