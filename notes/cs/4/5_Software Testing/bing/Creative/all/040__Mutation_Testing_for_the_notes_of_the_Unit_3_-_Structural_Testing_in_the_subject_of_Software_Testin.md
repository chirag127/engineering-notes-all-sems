### Mutation Testing for the notes of the Unit 3 - Structural Testing in the subject of Software Testing

- Mutation testing is a type of white box testing in which testers change specific components of an application's source code to ensure a software test suite will be able to detect the changes.
- The changes introduced to the software are intended to cause errors in the program. These changes are called **mutations** and the modified versions of the program are called **mutants**.
- The goal of mutation testing is to evaluate the quality and effectiveness of the test suite by measuring how many mutants it can **kill**. A mutant is killed if the test suite detects a difference in the output or behavior of the original program and the mutant.
- If the test suite fails to detect any difference, the mutant is said to have **survived**. This indicates that the test suite is not adequate or complete enough to cover all possible scenarios.
- Mutation testing also helps to identify **equivalent mutants**, which are mutants that produce the same output and behavior as the original program, regardless of the test suite. These mutants are not useful for testing and should be avoided or removed.
- Mutation testing can be performed at different levels of granularity, such as statement, expression, or operator level. Depending on the level, different types of mutations can be applied, such as value mutation, statement mutation, or decision mutation.
- Value mutation involves changing the value of a variable, constant, or literal in the program. For example, changing `x = 5` to `x = 6` or `y = "Hello"` to `y = "Hi"`.
- Statement mutation involves inserting, deleting, or replacing a statement in the program. For example, inserting a `break` statement in a loop, deleting a `return` statement in a function, or replacing an assignment statement with a different one.
- Decision mutation involves changing the condition or outcome of a decision statement in the program. For example, changing `if (x > y)` to `if (x < y)` or `if (x == y)` or changing the `then` or `else` branch of an `if` statement.
- Mutation testing can be performed manually or automatically using various tools and frameworks. Some examples of mutation testing tools are PIT, Jumble, MuJava, and MutPy .
- Mutation testing has some advantages and disadvantages. Some of the advantages are :
  - It helps to improve the quality and coverage of the test suite by finding gaps and weaknesses in the test cases.
  - It helps to measure the effectiveness of the test suite by providing a metric called **mutation score**, which is the ratio of killed mutants to the total number of mutants.
  - It helps to find subtle and complex errors in the program that may not be detected by other testing techniques.
- Some of the disadvantages are :
  - It is computationally expensive and time-consuming, as it requires generating and executing a large number of mutants for each program.
  - It may produce a lot of equivalent mutants, which are difficult to identify and eliminate.
  - It may require human intervention and judgment to analyze the results and decide which mutants are relevant and meaningful.

- A possible mnemonic to remember the concept of mutation testing is **MUTATE**:
  - **M**odify the source code in small ways
  - **U**se a test suite to run the original and mutated programs
  - **T**est the difference in the output or behavior
  - **A**ssess the quality and effectiveness of the test suite
  - **T**ry to kill all the mutants
  - **E**liminate the equivalent mutants

: https://www.techtarget.com/searchitoperations/definition/mutation-testing
: https://www.softwaretestinghelp.com/what-is-mutation-testing/
: https://www.guru99.com/mutation-testing.html
: https://en.wikipedia.org/wiki/Mutation_testing
: https://www.geeksforgeeks.org/software-testing-mutation-testing/