# Estimation of Test Coverage Metrics and Structural Complexity

## Introduction

- Test coverage metrics are used to measure and monitor the testing activity of a software program.
- Test coverage metrics help to answer questions such as how many bugs are found, how much time is spent on testing, and how thorough the testing is.
- Test coverage metrics also help to improve the testing process and maximize efficiency by identifying the areas that need more attention or improvement.
- One way to measure test coverage is by using structural coverage metrics, which are based on the structure or flow of control of the program code.
- Structural coverage metrics use a graphical representation of the program code called a control flow graph (CFG), which shows the basic blocks and the possible paths of execution in the program.
- A basic block is a sequence of statements that has a single entry point and a single exit point, and does not contain any branching or looping statements.
- A path is a sequence of basic blocks that starts from the entry point and ends at the exit point of the program.
- A CFG helps to estimate the complexity of the program and the number of test cases required to test the program.
- In this topic, we will learn how to identify basic blocks and draw a CFG using them, and how to use structural coverage metrics such as cyclomatic complexity, statement coverage, branch coverage, and path coverage to measure test coverage.

## Cyclomatic Complexity

- Cyclomatic complexity is a metric that measures the complexity of a program based on the number of linearly independent paths in its CFG.
- A linearly independent path is a path that introduces at least one new edge or node that is not covered by any other path.
- Cyclomatic complexity can be calculated using the following formula:

    - `V(G) = E - N + 2`, where `V(G)` is the cyclomatic complexity, `E` is the number of edges, and `N` is the number of nodes in the CFG.
    - `V(G) = P + 1`, where `P` is the number of predicate nodes, which are nodes that have two or more outgoing edges, such as conditional or looping statements.
    - `V(G) = R`, where `R` is the number of regions in the CFG, which are areas enclosed by edges and nodes.

- Cyclomatic complexity indicates the minimum number of test cases required to achieve 100% path coverage, which means that every path in the CFG is executed at least once by the test cases.
- Cyclomatic complexity also indicates the upper bound of the number of errors that can be present in the program, as each path may contain a potential error.
- Cyclomatic complexity can be used to compare the complexity of different programs or modules, and to identify the modules that need more testing or refactoring.
- A general guideline is that cyclomatic complexity should not exceed 10, as higher values indicate high complexity and low maintainability.

## Statement Coverage

- Statement coverage is a metric that measures the percentage of statements in the program code that are executed by the test cases.
- Statement coverage can be calculated using the following formula:

    - `SC = (S / T) * 100`, where `SC` is the statement coverage, `S` is the number of statements executed by the test cases, and `T` is the total number of statements in the program code.

- Statement coverage can be used to assess the adequacy of the test cases and to identify the statements that are not covered by the test cases.
- Statement coverage can also be used to compare the coverage of different test cases or test suites, and to select the most effective test cases or test suites.
- A general guideline is that statement coverage should be at least 80%, as lower values indicate insufficient testing and high risk of errors.

## Branch Coverage

- Branch coverage is a metric that measures the percentage of branches in the program code that are executed by the test cases.
- A branch is a point in the program code where the control flow can diverge into two or more possible paths, such as a conditional or a looping statement.
- Branch coverage can be calculated using the following formula:

    - `BC = (B / D) * 100`, where `BC` is the branch coverage, `B` is the number of branches executed by the test cases, and `D` is the total number of branches in the program code.

- Branch coverage can be used to assess the adequacy of the test cases and to identify the branches that are not covered by the test cases.
- Branch coverage can also be used to compare the coverage of different test cases or test suites, and to select the