### Mutation Testing

- Mutation testing is a technique for evaluating the adequacy of a test suite by introducing artificial faults or mutations into the program under test.
- The test suite is run against the mutated program and the effectiveness of the test suite is measured by the percentage of mutants that are killed or detected by the test suite.
- A mutant is killed if the test suite produces a different output or behavior for the mutant than for the original program.
- A mutant is equivalent if it produces the same output or behavior as the original program for all possible inputs. Equivalent mutants are not considered in the mutation score.
- A mutant is live if the test suite does not produce a different output or behavior for the mutant than for the original program. Live mutants indicate that the test suite is inadequate or incomplete.
- The mutation score is the ratio of killed mutants to the total number of non-equivalent mutants. It is a measure of the fault-detection capability of the test suite.
- Mutation testing can be applied at different levels of abstraction, such as source code, intermediate code, or binary code. It can also be applied to different types of software artifacts, such as specifications, models, or databases.
- Mutation testing can be used to complement other testing techniques, such as structural testing or functional testing, by providing additional criteria for test suite adequacy and improvement.
- Mutation testing can also be used to generate new test cases, by analyzing the live mutants and finding inputs that can kill them.
- Mutation testing is computationally expensive, as it requires generating and executing a large number of mutants. Various techniques have been proposed to reduce the cost of mutation testing, such as selective mutation, weak mutation, higher-order mutation, or parallel mutation.