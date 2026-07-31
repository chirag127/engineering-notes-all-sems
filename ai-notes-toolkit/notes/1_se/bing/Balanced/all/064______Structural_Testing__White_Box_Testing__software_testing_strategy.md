#### Structural Testing (White Box Testing) software testing strategy

- Structural testing is a software testing strategy that verifies the internal structure, design, and implementation of an application, rather than just its functionality.
- Structural testing is also known as white box testing, clear box testing, open box testing, glass box testing, transparent box testing, or code-based testing.
- Structural testing requires the testers to have access to the source code or binaries of the application, and to have knowledge of the devices and systems it is running on.
- Structural testing can be performed at different levels of testing, such as unit testing, integration testing, system testing, or acceptance testing, depending on the scope and complexity of the application.
- Structural testing can be done manually or automatically, using tools that can analyze the code and generate test cases based on various criteria, such as code coverage, data flow, control flow, logic, etc.
- Structural testing can help to improve the design, usability, security, and performance of the application, by identifying and fixing errors, bugs, vulnerabilities, and inefficiencies in the code.
- Structural testing can also help to measure the quality and complexity of the code, by using metrics such as cyclomatic complexity, lines of code, code coverage, etc.

Some of the common techniques and types of structural testing are:

- Statement coverage: This technique measures the percentage of executable statements in the code that are executed by the test cases. It aims to cover all the statements at least once.
- Branch coverage: This technique measures the percentage of branches or decision points in the code that are executed by the test cases. It aims to cover all the possible outcomes of each branch, such as true or false, yes or no, etc.
- Path coverage: This technique measures the percentage of paths or sequences of statements and branches in the code that are executed by the test cases. It aims to cover all the possible paths from the entry point to the exit point of the code.
- Condition coverage: This technique measures the percentage of conditions or logical expressions in the code that are evaluated to true or false by the test cases. It aims to cover all the possible values of each condition, such as AND, OR, NOT, etc.
- Loop coverage: This technique measures the percentage of loops or iterations in the code that are executed by the test cases. It aims to cover all the possible scenarios of each loop, such as zero, one, or more iterations, entry or exit conditions, etc.
- Data flow coverage: This technique measures the percentage of data flows or interactions between variables in the code that are executed by the test cases. It aims to cover all the possible states of each variable, such as definition, use, modification, etc.
- Mutation testing: This technique involves modifying or mutating the code in small ways, such as changing a variable, operator, or statement, and then running the test cases to see if they can detect the change. It aims to measure the effectiveness and robustness of the test cases.

Some of the advantages and disadvantages of structural testing are:

- Advantages:
  - It can help to find errors and bugs that are not visible or detectable by functional testing.
  - It can help to improve the quality and maintainability of the code by enforcing coding standards and best practices.
  - It can help to optimize the performance and security of the code by eliminating redundant or unnecessary code, and by detecting vulnerabilities and weaknesses.
  - It can help to measure the code coverage and complexity, and to provide feedback and suggestions for improvement.
- Disadvantages:
  - It can be time-consuming and costly, as it requires access to the source code or binaries, and knowledge of the internal structure and logic of the code.
  - It can be difficult and challenging, as it requires a high level of technical and analytical skills, and the use of specialized tools and techniques.
  - It can be incomplete and insufficient, as it cannot cover all the possible scenarios and inputs that the code may encounter in the real world.
  - It can be biased and subjective, as it depends on the perspective and assumptions of the testers, and may not reflect the expectations and requirements of the users or customers.

Some of the mnemonics and learning tricks for structural testing are:

- To remember the types of structural testing, you can use the acronym **SBCPCLDM**, which stands for **S**tatement, **B**ranch, **P**ath, **C**ondition, **L**oop, **D**ata flow, and **M**utation testing.
- To remember the difference between statement coverage and branch coverage, you can use the example of an if