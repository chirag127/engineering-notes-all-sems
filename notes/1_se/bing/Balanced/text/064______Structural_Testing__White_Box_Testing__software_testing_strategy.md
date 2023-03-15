#### Structural Testing (White Box Testing) software testing strategy

- Structural testing, also known as white box testing, is a software testing strategy that focuses on the internal structure, design, and implementation of the software system.
- The main objective of structural testing is to verify that the software conforms to the specified design and coding standards, and that it has adequate coverage of all possible paths, branches, statements, and conditions in the code.
- Structural testing requires the tester to have access to the source code and detailed knowledge of the programming logic and techniques used in the software development.
- Structural testing can be performed at different levels of testing, such as unit testing, integration testing, and system testing, depending on the scope and complexity of the software system.
- Structural testing can be done manually or with the help of automated tools that can generate test cases, execute them, and measure the code coverage and quality metrics.
- Some of the common techniques and methods used in structural testing are:

  - Statement coverage: It measures the percentage of executable statements in the code that are executed by the test cases.
  - Branch coverage: It measures the percentage of decision points (such as if-else, switch-case, etc.) in the code that are executed by the test cases.
  - Path coverage: It measures the percentage of possible paths (sequences of statements and branches) in the code that are executed by the test cases.
  - Condition coverage: It measures the percentage of logical conditions (such as AND, OR, NOT, etc.) in the code that are evaluated to both true and false by the test cases.
  - Data flow coverage: It measures the percentage of data flow dependencies (such as definition, use, and kill) in the code that are covered by the test cases.
  - Mutation testing: It involves creating and executing modified versions of the code (called mutants) that have one or more faults introduced in them, and checking if the test cases can detect the faults.
  - Cyclomatic complexity: It is a metric that indicates the number of independent paths in the code, and thus the complexity and maintainability of the code. It can be calculated by using the formula: `C = E - N + 2P`, where C is the cyclomatic complexity, E is the number of edges, N is the number of nodes, and P is the number of connected components in the control flow graph of the code.