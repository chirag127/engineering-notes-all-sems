# Control Flow Graphs

- A control flow graph (CFG) is a graphical representation of the control flow or computation during the execution of a program or application .
- A CFG consists of nodes and edges, where nodes represent basic blocks and edges represent the possible transitions between them .
- A basic block is a maximal sequence of straight-line, or branch-free, code that always executes together, unless an exception occurs .
- A CFG can accurately represent the flow of control inside a program unit, such as a function, a method, or a module .
- A CFG can be used for various purposes, such as static analysis, compiler optimization, testing, debugging, and reverse engineering .

## Symbols and Example

- The symbols used in a CFG are:
  - A circle or an oval to represent a basic block
  - An arrow to represent the direction of control flow
  - A diamond to represent a conditional branch
  - A rectangle to represent the start or end of the program
- An example of a CFG for a simple program that calculates the factorial of a number is:

![CFG example](https://study.com/cimages/multimages/16/cfd.png)

- The CFG shows the following steps:
  - Start the program
  - Initialize the variables n, i, and f
  - Check if n is less than or equal to 1
  - If yes, set f to 1 and go to step 8
  - If no, multiply f by i and increment i by 1
  - Check if i is less than or equal to n
  - If yes, go back to step 5
  - If no, print f and end the program