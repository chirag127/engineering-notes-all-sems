### Mutation Testing

Mutation testing is a form of white box testing in which testers change specific components of an application's source code to ensure a software test suite will be able to detect the changes. Changes introduced to the software are intended to cause errors in the program. These changes are called **mutations** and the modified programs are called **mutants**.

The main objectives of mutation testing are:

- To design new software tests and evaluate the quality of existing software tests.
- To help the tester develop effective tests or locate weaknesses in the test data used for the program.
- To ensure the quality of a software testing suite, not the applications the suite will go on to test.

The steps to execute mutation testing are:

- Faults are introduced into the source code of the program by creating many versions called mutants. Each mutant differs from the original program by one small syntactic change.
- Test cases are applied to the original program and also to the mutant program. A test case is said to **kill** a mutant if it causes the mutant to produce a different output from the original program.
- The test suite is evaluated based on the percentage of mutants killed by the test cases. This percentage is called the **mutation score**. A higher mutation score indicates a better test suite.
- The test suite is improved by adding or modifying test cases to kill more mutants. The process is repeated until the desired mutation score is achieved or no more mutants can be killed.