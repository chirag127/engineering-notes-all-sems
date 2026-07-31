### Statements that alter the flow of control

- Control statements are the statements that change the flow of execution of statements.
- For example, if, if-else, switch-case, while-do, for, break, continue, goto, etc.
- Control statements can be classified into two categories: selection statements and iteration statements.
- Selection statements are the statements that choose one of the alternative paths based on a condition. For example, if, if-else, switch-case, etc.
- Iteration statements are the statements that repeat a block of statements until a condition is satisfied. For example, while-do, for, etc.
- Control statements can also be nested, meaning that one control statement can be inside another control statement. For example, if (x > 0) { while (y < 10) { y++; } }
- Control statements can be represented by a control flow graph (CFG), which is a directed graph that shows the possible paths of execution of a program.
- A CFG consists of nodes and edges, where each node represents a basic block and each edge represents a possible transfer of control between basic blocks.
- A basic block is a sequence of statements such that it can be entered only at the beginning of the block and it can be exited only at the end of the block.
- A CFG can be used to perform data flow analysis, which is a technique to determine the information that is available at each point of a program, such as the values of variables, the definitions of variables, the uses of variables, etc.
- Data flow analysis can help to optimize the code, detect errors, and verify properties of the program.