### Equivalence Class Testing for the notes of the Unit 2 - Functional Testing in the subject of Software Testing

- Equivalence Class Testing is a black-box testing technique that divides the input domain of a system into classes of data that are expected to behave similarly.
- The main idea is to select one representative value from each class as a test case, instead of testing all possible values in the class.
- This reduces the number of test cases while still covering the most likely scenarios and errors.
- Equivalence classes can be derived from the requirements specification, the design specification, or the code of the system.
- Equivalence classes can be either valid or invalid, depending on whether they satisfy the expected conditions or not.
- A valid equivalence class contains values that should be accepted by the system, while an invalid equivalence class contains values that should be rejected by the system.
- For example, suppose we have a system that accepts an integer input between 1 and 100. We can identify the following equivalence classes:

| Equivalence Class | Description | Example |
|-------------------|-------------|---------|
| Valid             | Values between 1 and 100, inclusive | 50 |
| Invalid           | Values less than 1 | -10 |
| Invalid           | Values greater than 100 | 200 |

- To test the system, we can select one value from each equivalence class, such as 50, -10, and 200, and check if the system behaves as expected.
- A mnemonic to remember the steps of equivalence class testing is **BIRD**:

  - **B**oundary values: Identify the boundaries of the input domain, such as minimum and maximum values, or special cases.
  - **I**nternal values: Identify the values within the boundaries that are valid and invalid, such as ranges, sets, or patterns.
  - **R**epresentative values: Select one value from each equivalence class as a test case, preferably covering both valid and invalid classes.
  - **D**efects: Execute the test cases and check for defects in the system, such as incorrect outputs, errors, or crashes.