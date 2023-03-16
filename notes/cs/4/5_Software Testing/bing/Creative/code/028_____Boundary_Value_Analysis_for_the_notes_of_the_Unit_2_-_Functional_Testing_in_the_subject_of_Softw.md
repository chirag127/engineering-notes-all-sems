### Boundary Value Analysis

- Boundary value analysis (BVA) is a black-box testing technique that focuses on testing the values at the boundaries of the input domain of a program or system.
- BVA is based on the assumption that errors are more likely to occur at the edges of the input domain than in the middle.
- BVA can be applied to both numeric and non-numeric inputs, such as dates, strings, characters, etc.
- BVA can also be applied to outputs, such as error messages, status codes, etc.
- BVA can help to reduce the number of test cases by selecting representative values from the boundary regions of the input domain, rather than testing all possible values.
- BVA can be used in conjunction with equivalence partitioning (EP), which divides the input domain into disjoint subsets of equivalent values, and selects one value from each subset for testing.
- BVA can be performed in two ways: robust and weak.
  - Robust BVA tests the values at the exact boundaries, as well as one value above and one value below each boundary.
  - Weak BVA tests only the values at the exact boundaries, and does not test the values outside the boundaries.
- BVA can be illustrated by using a boundary value diagram, which shows the input domain, the boundary values, and the test cases.
- BVA can be applied to both single and multiple input variables, by using one-dimensional and two-dimensional boundary value diagrams, respectively.
- BVA can help to detect boundary-related errors, such as off-by-one errors, incorrect comparisons, incorrect data types, etc.