### Generation of Graph from Program for the notes of the Unit 3 - Structural Testing in the subject of Software Testing

- Generation of graph from program is a technique of structural testing that uses the program's control flow as a model to design test cases.
- Control flow is the sequence of execution of statements or instructions in a program.
- A graph is a visual representation of the control flow of a program, where nodes represent statements or blocks of code, and edges represent the possible transitions between nodes.
- A graph can be generated from a program by following these steps:
  - Identify the entry and exit points of the program and mark them as nodes.
  - Identify the decision points (such as if, switch, while, for, etc.) and mark them as nodes.
  - Identify the possible outcomes of each decision point and mark them as edges.
  - Identify the statements or blocks of code that are executed between decision points and mark them as nodes.
  - Connect the nodes and edges according to the program logic and flow.
- For example, consider the following pseudocode of a program that calculates the factorial of a number:

```
read n
if n < 0 then
  print "Invalid input"
else
  f = 1
  i = 1
  while i <= n do
    f = f * i
    i = i + 1
  end while
  print f
end if
```

- The graph generated from this program is:

```
  +-----+       +-----+       +-----+
  |read |------>| n<0 |------>|print|
  |  n  |       +-----+       |"Inv"|
  +-----+          |          +-----+
                   |
                   v
                +-----+       +-----+       +-----+
                | f=1 |------>| i=1 |------>| i<=n|<----+
                +-----+       +-----+       +-----+     |
                   |             |             |         |
                   |             |             v         |
                   |             |          +-----+      |
                   |             +--------->| f=f |----->+
                   |                        | * i |
                   |                        +-----+
                   |                           |
                   |                           v
                   |                        +-----+
                   +----------------------->| i=i |
                                            | + 1 |
                                            +-----+
                                               |
                                               v
                                            +-----+
                                            |print|
                                            |  f  |
                                            +-----+
```

- The advantages of generating a graph from a program are:
  - It helps to visualize the program structure and logic.
  - It helps to identify the independent paths and branches in the program.
  - It helps to measure the complexity of the program using metrics such as cyclomatic complexity.
  - It helps to design test cases that can cover all the paths and branches in the program.
- The disadvantages of generating a graph from a program are:
  - It requires access to the source code and knowledge of the programming language.
  - It can be time-consuming and tedious for large and complex programs.
  - It may not capture all the aspects of the program behavior, such as data flow, input/output, exceptions, etc.
- A mnemonic to remember the steps of generating a graph from a program is: **E.D.D.S.C**
  - **E**ntry and exit points
  - **D**ecision points
  - **D**ecision outcomes
  - **S**tatements or blocks
  - **C**onnect nodes and edges