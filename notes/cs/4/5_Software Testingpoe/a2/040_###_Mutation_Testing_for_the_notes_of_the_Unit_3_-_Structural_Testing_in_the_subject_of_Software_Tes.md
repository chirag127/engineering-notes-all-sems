 Here is the content in markdown format for the given topic:

### Mutation Testing for the notes of the Unit 3 - Structural Testing in the subject of Software Testing

Mutation Testing is a type of structural testing technique in which the source code of a program is slightly modified or mutated and tests are re-run on the mutated code. If the existing test cases fail to detect the mutation, then the test cases are considered as inadequate. This helps in evaluating and improving the quality of test cases.

Some key points about Mutation Testing:

- It is a method to evaluate the quality of test cases.
- The source code is mutated in small ways to create mutated versions or mutants of the original program.
- The test cases are run on the mutants.
- If the test cases fail to detect the mutation, then the test cases are considered as inadequate and need improvement.
- The effectiveness of the test cases is measured in terms of mutation score which is the percentage of mutants that are killed by the test cases.
- Higher mutation score indicates better test cases.
- It is a costly technique as it requires executing the test cases multiple times on the mutants.
- It helps to strengthen the test cases and find corner cases.
- It can be applied to both white box and black box testing.

Some examples of mutations are:

- Replacing < (less than) with <= (less than or equal to)
- Replacing > (greater than) with >= (greater than or equal to)
- Replacing = (equal to) with != (not equal to)
- Inverting the logic of an if condition
- Removing a variable assignment

Advantages:

- Evaluates the quality of test cases.
- Helps to improve the test cases.
- Finds faults in the test cases that are undetected otherwise.

Disadvantages:

- It is a time-consuming and costly technique as it requires executing the test cases multiple times.
- The mutants need to be closely related to realistic faults.
- The test cases can be strengthened only for the type of mutants introduced.

Applications:

- Mutation Testing is mainly used by researchers to evaluate and improve the quality of test cases.
- It can be used in conjunction with other testing techniques to further strengthen the test cases.