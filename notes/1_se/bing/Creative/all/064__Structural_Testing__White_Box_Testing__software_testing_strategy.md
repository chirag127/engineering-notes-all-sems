#### Structural Testing (White Box Testing) software testing strategy

- Structural testing, also known as white box testing, is a software testing strategy that focuses on the internal structure, design, and implementation of the software system.
- The main objective of structural testing is to verify that the software conforms to the specified design and coding standards, and that it has adequate coverage of all possible paths, branches, statements, and conditions in the code.
- Structural testing requires the tester to have access to the source code and detailed knowledge of the programming logic and techniques used in the software development.
- Structural testing can be performed at different levels of testing, such as unit testing, integration testing, and system testing, depending on the scope and complexity of the software system.
- Some of the common techniques and methods used in structural testing are:

  - **Statement coverage**: This technique measures the percentage of executable statements in the code that are executed by the test cases. It ensures that every statement in the code is tested at least once. The formula for statement coverage is:

    `Statement coverage = (Number of statements executed / Total number of statements) * 100`

  - **Branch coverage**: This technique measures the percentage of branches or decision points in the code that are executed by the test cases. It ensures that every possible outcome of a branch is tested at least once. The formula for branch coverage is:

    `Branch coverage = (Number of branches executed / Total number of branches) * 100`

  - **Path coverage**: This technique measures the percentage of paths in the code that are executed by the test cases. A path is a sequence of statements or branches from the entry point to the exit point of the code. Path coverage ensures that every possible path in the code is tested at least once. The formula for path coverage is:

    `Path coverage = (Number of paths executed / Total number of paths) * 100`

  - **Condition coverage**: This technique measures the percentage of conditions or logical expressions in the code that are evaluated to both true and false by the test cases. It ensures that every condition in the code is tested for both outcomes. The formula for condition coverage is:

    `Condition coverage = (Number of conditions evaluated to both true and false / Total number of conditions) * 100`

  - **Data flow testing**: This technique analyzes the flow of data values through the variables, parameters, and return values in the code. It ensures that the data values are defined, used, and modified correctly and consistently throughout the code. Data flow testing uses four types of coverage criteria:

    - **Definition-use (DU) coverage**: This criterion ensures that every variable in the code is defined before it is used, and that every definition of a variable is used by some statement.
    - **All-definitions (AD) coverage**: This criterion ensures that every definition of a variable in the code is executed by at least one test case.
    - **All-uses (AU) coverage**: This criterion ensures that every use of a variable in the code is executed by at least one test case that covers the corresponding definition of the variable.
    - **All-du-paths (ADUP) coverage**: This criterion ensures that every path in the code that contains a definition and a use of a variable is executed by at least one test case.

  - **Control flow testing**: This technique analyzes the flow of control or execution through the statements, branches, loops, and subroutines in the code. It ensures that the control flow is correct and consistent throughout the code. Control flow testing uses four types of coverage criteria:

    - **Basic block coverage**: This criterion ensures that every basic block in the code is executed by at least one test case. A basic block is a sequence of statements that has a single entry point and a single exit point.
    - **Edge coverage**: This criterion ensures that every edge or transition between two basic blocks in the code is executed by at least one test case.
    - **Node coverage**: This criterion ensures that every node or junction point between two or more edges in the code is executed by at least one test case.
    - **Loop coverage**: This criterion ensures that every loop in the code is executed by at least one test case that covers the following scenarios:

      - The loop is executed zero times (skipped).
      - The loop is executed exactly once (minimum iteration).
      - The loop is executed more than once (multiple iterations).
      - The loop is executed with its maximum possible value (maximum iteration).

- Some of the advantages of structural testing are:

  - It helps to detect errors and bugs in the code that may not be visible or obvious from the functional or behavioral aspects of the software.
  - It helps to improve the quality, reliability, and maintainability of the software by