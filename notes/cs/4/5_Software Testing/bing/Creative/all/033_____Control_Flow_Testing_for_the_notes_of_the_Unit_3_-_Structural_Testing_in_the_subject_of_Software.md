# Control Flow Testing

Control flow testing is a type of software testing that uses the program's control flow as a model. Control flow testing is a structural testing strategy that comes under white box testing. Control flow testing is used to develop test cases of a program, where the tester selects a large portion of the program to test and to set the testing path.

## Objectives of Control Flow Testing

- To identify the execution paths through a module of program code and then create and execute test cases to cover those paths.
- To detect errors in the logic and structure of the program, such as missing or incorrect branches, loops, conditions, etc.
- To measure the coverage of the test cases based on the number of paths, branches, statements, or conditions executed.

## Steps of Control Flow Testing

- Draw a control flow graph (CFG) of the program, which is a graphical representation of the program's structure and logic. A CFG consists of nodes and edges, where nodes represent basic blocks of code and edges represent the flow of control between them.
- Identify the independent paths in the CFG, which are paths that do not share any node or edge with other paths. Independent paths can be found using techniques such as cyclomatic complexity, basis path testing, or path sensitizing.
- Design test cases for each independent path, using input values and expected outputs that exercise the path. Test cases can be derived using techniques such as boundary value analysis, equivalence partitioning, or error guessing.
- Execute the test cases and compare the actual outputs with the expected outputs. Report any discrepancies or failures as defects.
- Calculate the coverage of the test cases based on the number of paths, branches, statements, or conditions executed. Coverage can be measured using metrics such as path coverage, branch coverage, statement coverage, or condition coverage.

## Advantages of Control Flow Testing

- It detects almost half of the defects that are determined during the unit testing. It also determines almost one-third of the defects of the whole program.
- It can be performed manually or automated as the control flow graph that is used can be made by hand or by tools.
- It helps to improve the quality and reliability of the software by ensuring that all the possible paths and scenarios are tested.
- It helps to identify the dead code or unreachable code that can be removed or optimized.

## Disadvantages of Control Flow Testing

- It can be time-consuming and complex to draw the control flow graph and identify the independent paths for large and complex programs.
- It can be difficult to design test cases that cover all the paths, especially if there are many conditional statements or loops in the program.
- It can be costly and impractical to achieve 100% coverage, as some paths may be rarely or never executed in real scenarios.
- It does not test the functionality or the data flow of the program, only the structure and logic. It may miss some errors that are related to the input or output data or the specifications of the program.