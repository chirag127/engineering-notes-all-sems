### Control Flow Testing for the notes of the Unit 3 - Structural Testing in the subject of Software Testing

- Control flow testing is a type of software testing that uses the program's control flow as a model.
- Control flow testing is a structural testing strategy that comes under white box testing.
- Control flow testing is used to develop test cases of a program, where the tester selects a large portion of the program to test and to set the testing path.
- Control flow testing is implemented with the intention to test the logic of the code so that the user requirements can be fulfilled.
- Control flow testing can be performed manually or automated as the control flow graph that is used can be made by hand or by using software.

#### Control Flow Testing Process

The following are the steps involved in the process of control flow testing:

1. Control Flow Graph Creation: From the given source code, a control flow graph is created either manually or by using software. A control flow graph is a graphical representation of the control flow or computation that is done during the execution of the program.
2. Coverage Target: A coverage target is defined over the control flow graph that includes nodes, edges, paths, branches, etc. The coverage target specifies the criteria for selecting test cases that cover the control flow graph.
3. Test Case Creation: Test cases are created using the control flow graph to cover the defined coverage target. Test cases are designed to exercise the paths, branches, or nodes of the control flow graph.
4. Test Case Execution: After the creation of test cases over the coverage target, the test cases are executed. The test cases are run on the program and the actual outputs are compared with the expected outputs.
5. Analysis: The results of the test case execution are analyzed and the defects or errors in the program are identified and reported.

#### Control Flow Graph

A control flow graph is a graphical representation of the control flow or computation that is done during the execution of the program. Control flow graphs are mostly used in static analysis as well as compiler applications, as they can accurately represent the flow inside of a program unit.

A control flow graph consists of the following elements:

- Nodes: Nodes represent the basic blocks of the program, which are sequences of statements or instructions that are executed in order. Nodes can be classified into five types: entry node, exit node, decision node, junction node, and process node.
- Edges: Edges represent the transitions or connections between the nodes. Edges indicate the direction of the control flow from one node to another. Edges can be classified into two types: true edge and false edge.
- Paths: Paths represent the sequences of nodes and edges that are traversed during the execution of the program. Paths can be classified into two types: simple path and complete path.

An example of a control flow graph is shown below:

```
    +-----+       +-----+       +-----+       +-----+
    |     |       |     |       |     |       |     |
    |Start|------>| n=5 |------>| n>0 |------>|Stop |
    |     |       |     |       |     |       |     |
    +-----+       +-----+       +-----+       +-----+
                        |           |
                        |           |
                        |           |
                        |           |
                        |           |
                        |           |
                        |           |
                        |           |
                        |           |
                        |           |
                        |           |
                        |           |
                        |           |
                        |           |
                        |           |
                        +-----+     |
                              |     |
                              |     |
                              |     |
                              |     |
                              |     |
                              |     |
                              |     |
                              |     |
                              |     |
                              |     |
                              |     |
                              |     |
                              |     |
                              |     |
                              |     |
                              |     |
                              |     |
                              |     |
                              +-----+
                              |     |
                              | n-- |
                              |     |
                              +-----+
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |