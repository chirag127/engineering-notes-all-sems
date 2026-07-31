### Control Flow Graphs

- A control flow graph (CFG) is a graphical representation of the control flow or computation during the execution of a program or application .
- A CFG consists of nodes and edges, where nodes represent basic blocks and edges represent the possible transitions between them .
- A basic block is a maximal sequence of straight-line, or branch-free, code that always executes together, unless an exception occurs .
- A CFG can accurately represent the flow of control inside a program unit, such as a function, a method, or a module .
- A CFG can be used for various purposes, such as static analysis, compiler optimization, testing, debugging, and reverse engineering .

#### Symbols and Example

- A CFG uses the following symbols:
  - A circle or an oval represents a basic block, which contains one or more statements or operations.
  - An arrow represents a control flow edge, which indicates the possible execution paths between basic blocks.
  - A diamond represents a decision node, which contains a conditional statement that branches the control flow based on the outcome of the condition.
  - A rectangle represents an input/output node, which contains a statement that reads or writes data from or to an external source.
  - A double circle represents an entry node, which marks the beginning of the program or the program unit.
  - A double square represents an exit node, which marks the end of the program or the program unit.
- An example of a CFG for a simple program that calculates the factorial of a given number is shown below:

![CFG example](https://study.com/cimages/multimages/16/control_flow_diagram.png)

- The CFG has six basic blocks, labeled as B1 to B6, and one decision node, labeled as D1.
- The entry node is B1, which contains the input statement that reads the number n from the user.
- The exit node is B6, which contains the output statement that prints the result of the factorial calculation.
- The decision node D1 contains the conditional statement that checks if n is equal to zero or one, and branches the control flow accordingly.
- The basic block B2 contains the initialization statement that sets the variable f to one.
- The basic block B3 contains the loop statement that decrements n by one.
- The basic block B4 contains the assignment statement that updates f by multiplying it with n.
- The basic block B5 contains the jump statement that returns the control flow to the decision node D1.
- The control flow edges show the possible execution paths between the basic blocks and the decision node, depending on the values of n and f.