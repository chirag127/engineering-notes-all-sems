### Control Flow Graphs

- A control flow graph (CFG) is a graphical representation of the control flow or computation during the execution of a program or application .
- A CFG consists of nodes and edges, where nodes represent basic blocks and edges represent the possible paths of execution .
- A basic block is a maximal sequence of straight-line, or branch-free, code that always executes together, unless an exception occurs .
- A CFG can be used for various purposes, such as static analysis, compiler optimization, testing, debugging, and program slicing .

#### Symbols and Example

- The symbols used in a CFG are:
  - A circle or rectangle for a basic block
  - An arrow for an edge
  - A diamond for a conditional branch
  - A double circle for the entry point
  - A double square for the exit point
- An example of a CFG for a simple program that calculates the factorial of a number is:

![CFG example](https://study.com/cimages/multimages/16/cfd.png)

- The CFG shows the possible paths of execution depending on the value of the input variable n.
- The entry point is the double circle labeled Start, and the exit point is the double square labeled End.
- The basic blocks are the circles labeled 1 to 6, where each block contains one or more statements.
- The edges are the arrows that connect the basic blocks, indicating the flow of control.
- The diamond labeled 2 is a conditional branch that checks if n is equal to zero or not, and branches to either block 3 or block 4 accordingly.
- The loop is formed by the edges from block 4 to block 5 and from block 5 to block 2, which repeat until n becomes zero.
- The final result is stored in the variable f, which is printed in block 6 before exiting the program.