#### Structural Testing (White Box Testing) software testing strategy

- Structural testing, also known as white box testing, is a software testing strategy that focuses on the internal structure, design, and implementation of the software system.
- The main objective of structural testing is to verify that the software conforms to the specified design and coding standards, and that it has adequate coverage of all possible paths, branches, statements, and conditions in the code.
- Structural testing requires the tester to have access to the source code and detailed knowledge of the programming logic and techniques used in the software.
- Structural testing can be performed at different levels of testing, such as unit testing, integration testing, and system testing, depending on the scope and granularity of the code under test.
- Some of the common techniques and methods used in structural testing are:

  - Statement coverage: It measures the percentage of executable statements in the code that are executed by the test cases. It is the simplest and most basic form of structural testing. A statement coverage of 100% means that every statement in the code has been executed at least once by the test cases.
  - Branch coverage: It measures the percentage of decision points or branches in the code that are executed by the test cases. A branch is a point in the code where the control flow can take two or more different paths based on some condition. A branch coverage of 100% means that every branch in the code has been executed at least once by the test cases.
  - Path coverage: It measures the percentage of possible paths in the code that are executed by the test cases. A path is a sequence of statements and branches that starts from the entry point and ends at the exit point of the code. A path coverage of 100% means that every path in the code has been executed at least once by the test cases.
  - Condition coverage: It measures the percentage of logical conditions in the code that are evaluated to both true and false by the test cases. A condition is a boolean expression that determines the outcome of a branch. A condition coverage of 100% means that every condition in the code has been evaluated to both true and false by the test cases.
  - Decision coverage: It measures the percentage of decision outcomes in the code that are executed by the test cases. A decision is the result of evaluating a condition. A decision coverage of 100% means that every decision in the code has been executed by the test cases.
  - Loop coverage: It measures the percentage of loops in the code that are executed by the test cases. A loop is a structure that repeats a block of code until a termination condition is met. A loop coverage of 100% means that every loop in the code has been executed by the test cases with different iteration counts, including zero, one, and more than one.
  - Data flow coverage: It measures the percentage of data flow anomalies in the code that are detected by the test cases. A data flow anomaly is a situation where a variable is used before being defined, defined more than once, or defined but not used. A data flow coverage of 100% means that every data flow anomaly in the code has been detected by the test cases.

- Some of the advantages of structural testing are:

  - It helps to identify and eliminate errors, defects, and bugs in the code that may not be detected by functional testing.
  - It helps to improve the quality, reliability, and performance of the software by ensuring that the code is well-structured, optimized, and follows the best practices and standards.
  - It helps to measure the test coverage and effectiveness of the test cases by providing quantitative metrics and criteria.
  - It helps to facilitate the maintenance and debugging of the software by providing a clear and detailed view of the code structure and behavior.

- Some of the disadvantages of structural testing are:

  - It requires a high level of technical expertise and skill from the tester to understand and analyze the code logic and design.
  - It may not be feasible or practical to achieve 100% coverage of all the structural elements in the code, especially for large and complex software systems.
  - It may not be sufficient to ensure the functionality, usability, and security of the software from the user's perspective, as it does not consider the external inputs, outputs, and interactions of the software.
  - It may introduce bias and subjectivity in the test cases, as the tester may design the test cases based on the knowledge and assumptions of the code, rather than the requirements and specifications of the software.

- A mnemonic to remember the types of structural testing techniques is: **S**tatement, **B**ranch, **P**ath, **C**ondition, **D**ecision, **L**oop, and **D**ata flow. The first letters