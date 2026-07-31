###### Control Flow Graphs in software design

- A control flow graph (CFG) is a graphical representation of the possible paths of execution of a program or a function.  
- A CFG consists of nodes and edges. Nodes represent basic blocks, which are sequences of statements that are executed without any branching. Edges represent the flow of control between basic blocks, such as jumps, loops, or conditional statements.  
- A CFG can be used for various purposes in software engineering, such as static analysis, testing, optimization, debugging, and documentation.   
- A CFG can be constructed from the source code or the intermediate representation of a program or a function. There are different algorithms and tools for generating CFGs, such as Canva , which is a free online flowchart maker.
- A CFG can be represented in different ways, such as text, tables, or diagrams. A common way to draw a CFG is to use rectangles for nodes and arrows for edges. An example of a CFG for a simple function that calculates the factorial of a number is shown below:

```
  +-----------------+
  | n = input()     |
  | fact = 1        |
  +-----------------+
          |
          v
  +-----------------+
  | while n > 0:    |<-----------------+
  |   fact = fact*n |                  |
  |   n = n - 1     |                  |
  +-----------------+                  |
          |                            |
          v                            |
  +-----------------+                  |
  | print(fact)     |                  |
  +-----------------+                  |
          |                            |
          v                            |
  +-----------------+                  |
  | return          |------------------+
  +-----------------+
```

- A CFG can be analyzed to measure various properties of a program or a function, such as cyclomatic complexity, path coverage, data flow, and control dependencies.   
- A CFG can be modified to improve the performance, readability, or maintainability of a program or a function, such as by applying loop unrolling, dead code elimination, or code refactoring.  
- A CFG can be compared with other CFGs to detect similarities or differences between programs or functions, such as by using graph isomorphism, graph matching, or graph edit distance.  

- A possible mnemonic to remember the definition of a CFG is: **C**ontrol **F**low **G**raphs show the **C**hoices, **F**lows, and **G**oals of a program or a function.