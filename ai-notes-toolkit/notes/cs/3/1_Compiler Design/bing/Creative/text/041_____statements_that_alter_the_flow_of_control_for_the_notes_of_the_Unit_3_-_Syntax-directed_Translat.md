### Statements that alter the flow of control

- Statements that alter the flow of control are the statements that change the flow of execution of statements based on some conditions or iterations.
- Examples of statements that alter the flow of control are if, if-else, switch-case, while-do, for, break, continue, goto, etc .
- Statements that alter the flow of control can be classified into two categories: selection statements and iteration statements.
  - Selection statements are the statements that choose one of the alternative paths of execution based on a Boolean expression. Examples are if, if-else, switch-case, etc.
  - Iteration statements are the statements that repeat a block of statements until a Boolean expression becomes false. Examples are while-do, for, do-while, etc.
- Statements that alter the flow of control can be represented by a control flow graph (CFG), which is a directed graph that shows the possible paths of execution of a program.
  - A CFG consists of nodes and edges, where each node represents a basic block and each edge represents a possible transfer of control.
  - A basic block is a sequence of statements such that it can be entered only at the beginning and exited only at the end.
  - A CFG can be used to perform data flow analysis, which is a technique to determine the information that is available at each point of a program.
- Statements that alter the flow of control can be translated into intermediate code using syntax-directed translation, which is a method to attach semantic actions to the grammar rules of a language.
  - Syntax-directed translation can use either a bottom-up or a top-down approach, depending on the order of applying the semantic actions.
  - Syntax-directed translation can use either a syntax tree or a translation scheme, depending on the representation of the semantic actions.
  - Syntax-directed translation can use either a static or a dynamic scope, depending on the visibility of the variables in the program.