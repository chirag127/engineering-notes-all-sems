### Boundary Value Analysis for the notes of the Unit 2 - Functional Testing in the subject of Software Testing

- Boundary Value Analysis (BVA) is a black-box testing technique that is based on testing the boundary values of valid and invalid partitions .
- The boundary values are the minimum and maximum values of a partition, and they are more likely to be incorrect than the values within the partition  .
- BVA can be used to test a range of numbers, dates, and time, and it can be performed at all test levels .
- BVA is an extension of Equivalence Partitioning (EP), and it can be used to complement EP by testing the edge cases of the partitions .
- BVA can be applied to both valid and invalid partitions, and it can use a single fault assumption to test multiple variables.
- BVA can be done using a three-step approach:
  - Identify the exact boundary values of the partition
  - Identify the boundary values that are one less and one more than the exact boundary values
  - Test the application with all the identified boundary values
- BVA can help to find defects that are caused by off-by-one errors, incorrect comparisons, or improper validations .
- BVA can also be done using a four-step approach:
  - Identify the minimum and maximum values of the partition
  - Identify the nominal value of the partition (the midpoint or the most common value)
  - Test the application with the minimum, maximum, and nominal values
  - Test the application with the values that are just above and below the minimum and maximum values
- BVA can be illustrated using a table or a diagram to show the different boundary values and their expected outputs  .
- BVA can be used to test both numeric and non-numeric inputs, such as strings, characters, or booleans.
- BVA can be combined with other testing techniques, such as Decision Table Testing or State Transition Testing, to cover more scenarios and increase test coverage .

Example:

Consider a system that accepts ages from 18 to 56. The following table shows the boundary values and their expected outputs using the three-step approach:

| Test Case | Age | Expected Output |
|-----------|-----|-----------------|
| 1         | 17  | Invalid         |
| 2         | 18  | Valid           |
| 3         | 19  | Valid           |
| 4         | 37  | Valid           |
| 5         | 55  | Valid           |
| 6         | 56  | Valid           |
| 7         | 57  | Invalid         |

The following diagram shows the boundary values and their expected outputs using the four-step approach:

![Boundary Value Analysis Diagram](https://artoftesting.com/wp-content/uploads/2021/02/boundary-value-analysis-diagram.png)

Mnemonics and learning tricks:

- One possible mnemonic to remember the steps of BVA is **BENT**:
  - **B**oundary values
  - **E**xact values
  - **N**ominal values
  - **T**est cases
- Another possible mnemonic to remember the steps of BVA is **MINT**:
  - **M**inimum and maximum values
  - **I**ncrement and decrement values
  - **N**ominal value
  - **T**est cases
- A possible learning trick to remember the difference between EP and BVA is to think of EP as testing the **inside** of the partitions, and BVA as testing the **edges** of the partitions.