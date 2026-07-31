# Equivalence Class Testing

Equivalence class testing is a black box testing technique that divides the input domain of a software system into classes of data that are expected to behave similarly. The main idea is to select one representative value from each class as a test case, instead of testing all possible values. This reduces the number of test cases and increases the test coverage.

Some key points about equivalence class testing are:

- Equivalence classes can be derived from the requirements specification, the design specification, or the code of the software system.
- Equivalence classes can be based on valid or invalid inputs, outputs, or internal states of the system.
- Equivalence classes can be defined for both discrete and continuous data types.
- Equivalence classes should be mutually exclusive, meaning that no value can belong to more than one class.
- Equivalence classes should be collectively exhaustive, meaning that all possible values are covered by at least one class.

An example of equivalence class testing is:

- Suppose we have a software system that accepts an integer input between 1 and 100 and prints "Pass" if the input is divisible by 5, and "Fail" otherwise.
- The input domain can be divided into two valid equivalence classes: {5, 10, 15, ..., 100} and {1, 2, 3, 4, 6, 7, ..., 99}.
- The output domain can be divided into two valid equivalence classes: {"Pass"} and {"Fail"}.
- The input domain can also be divided into two invalid equivalence classes: {0} and {< 0, > 100}.
- The output domain can also be divided into one invalid equivalence class: {any other string}.
- To test the system, we can select one value from each valid input class, such as 5 and 6, and one value from each invalid input class, such as 0 and 101, and check the corresponding outputs. We do not need to test all 100 possible inputs.