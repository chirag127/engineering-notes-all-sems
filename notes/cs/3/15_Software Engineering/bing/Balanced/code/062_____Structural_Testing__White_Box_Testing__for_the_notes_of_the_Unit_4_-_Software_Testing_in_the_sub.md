### Structural Testing (White Box Testing)

Structural testing, also known as white box testing, is a method of software testing that tests the internal structure, logic, and code of the software system. The tester has access to the source code and can create test cases based on the code paths, branches, conditions, loops, and statements. The main objective of structural testing is to verify the quality, reliability, security, and performance of the software system.

Some of the advantages of structural testing are:

- It can detect errors and bugs in the early stages of development.
- It can improve the code quality, readability, and maintainability.
- It can measure the code coverage and identify the untested or dead code.
- It can help in debugging and optimizing the code.

Some of the disadvantages of structural testing are:

- It can be time-consuming and complex to design and execute the test cases.
- It can require skilled and experienced testers who can understand the code and logic.
- It can be difficult to test the user interface and the functionality of the software system.
- It can be incomplete or insufficient if the code is not well-structured or documented.

Some of the techniques and tools used for structural testing are:

- Statement coverage: It measures the percentage of statements that are executed by the test cases. It can be calculated by dividing the number of statements executed by the total number of statements in the code. A high statement coverage indicates that the code is well-tested, but it does not guarantee that all the possible scenarios and outcomes are covered.
- Branch coverage: It measures the percentage of branches or decision points that are executed by the test cases. It can be calculated by dividing the number of branches executed by the total number of branches in the code. A branch is a point where the control flow can diverge based on a condition. A high branch coverage indicates that the code is well-tested, but it does not guarantee that all the possible paths and outcomes are covered.
- Path coverage: It measures the percentage of paths that are executed by the test cases. It can be calculated by dividing the number of paths executed by the total number of paths in the code. A path is a sequence of statements and branches that are executed from the entry point to the exit point of the code. A high path coverage indicates that the code is well-tested, but it can be impractical or impossible to achieve 100% path coverage if the code has loops, recursion, or complex logic.
- Condition coverage: It measures the percentage of conditions that are evaluated to both true and false by the test cases. It can be calculated by dividing the number of conditions evaluated to both true and false by the total number of conditions in the code. A condition is a logical expression that determines the outcome of a branch. A high condition coverage indicates that the code is well-tested, but it does not guarantee that all the possible combinations and outcomes of the conditions are covered.
- Mutation testing: It is a technique that involves modifying the code by introducing small changes or errors (called mutants) and checking if the test cases can detect them. The mutants are created by applying operators such as changing a variable, operator, constant, or statement. The test cases are executed on the original code and the mutated code, and the results are compared. If the test cases fail on the mutated code but pass on the original code, then the mutant is killed. If the test cases pass on both the original and the mutated code, then the mutant is alive. The mutation score is the percentage of mutants that are killed by the test cases. A high mutation score indicates that the test cases are effective and can detect the faults in the code.

Some of the tools that can be used for structural testing are:

- JaCoCo: It is a tool that can measure the code coverage of Java applications. It can generate reports on statement, branch, and line coverage. It can also integrate with other tools such as Maven, Gradle, Eclipse, and SonarQube.
- Cobertura: It is a tool that can measure the code coverage of Java and Groovy applications. It can generate reports on statement, branch, and line coverage. It can also integrate with other tools such as Ant, Maven, and Jenkins.
- Istanbul: It is a tool that can measure the code coverage of JavaScript applications. It can generate reports on statement, branch, function, and line coverage. It can also integrate with other tools such as Mocha, Karma, and Grunt.
- GCC: It is a compiler that can measure the code coverage of C and C++ applications. It can generate reports on statement, branch, function, and line coverage. It can also