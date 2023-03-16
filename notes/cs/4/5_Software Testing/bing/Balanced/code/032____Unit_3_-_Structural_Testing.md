## Unit 3 - Structural Testing

Structural testing is a type of software testing that focuses on the internal structure, design, and implementation of the software system. It is also known as white-box testing, glass-box testing, or logic-driven testing.

The main objectives of structural testing are:

- To verify that the software conforms to the specified design and coding standards.
- To measure the code quality, complexity, and coverage of the software.
- To identify and eliminate errors, defects, and vulnerabilities in the code.
- To improve the maintainability, reliability, and security of the software.

The main techniques of structural testing are:

- Statement coverage: It measures the percentage of executable statements in the code that are executed by the test cases.
- Branch coverage: It measures the percentage of decision outcomes (such as if-then-else, switch-case, etc.) in the code that are executed by the test cases.
- Path coverage: It measures the percentage of independent paths in the code that are executed by the test cases. A path is a sequence of statements from the entry point to the exit point of the code.
- Condition coverage: It measures the percentage of logical conditions (such as AND, OR, NOT, etc.) in the code that are evaluated to both true and false by the test cases.
- Data flow coverage: It measures the percentage of data flow anomalies (such as definition-use, use-definition, etc.) in the code that are detected by the test cases. A data flow anomaly is a situation where a variable is used before it is defined, or defined more than once without being used, or never used after being defined.
- Mutation coverage: It measures the percentage of mutants (modified versions of the code) that are killed (caused to fail) by the test cases. A mutant is created by applying a small syntactic change to the code, such as changing a variable name, operator, constant, etc.

The main tools of structural testing are:

- Code analyzers: They are software tools that analyze the source code and generate metrics, reports, and diagrams that show the structure, complexity, and quality of the code.
- Code coverage tools: They are software tools that instrument the source code and measure the coverage of the code by the test cases. They can also generate coverage reports and highlight the covered and uncovered parts of the code.
- Mutation testing tools: They are software tools that generate and execute mutants of the code and compare the results with the original code. They can also generate mutation reports and show the killed and survived mutants of the code.