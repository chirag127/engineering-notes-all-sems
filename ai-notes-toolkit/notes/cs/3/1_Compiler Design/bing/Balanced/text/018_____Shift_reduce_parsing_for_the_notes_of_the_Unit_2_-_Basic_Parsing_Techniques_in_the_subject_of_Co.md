### Shift reduce parsing

- Shift reduce parsing is a class of efficient, table-driven bottom-up parsing methods for computer languages and other notations formally defined by a grammar.
- The parsing methods most commonly used for parsing programming languages, LR parsing and its variations, are shift-reduce methods.
- Shift reduce parsing uses a stack to hold the grammar and an input tape to hold the string.
- Shift reduce parsing performs the two actions: shift and reduce.
  - Shift: This involves moving symbols from the input buffer onto the stack.
  - Reduce: This involves replacing a handle (a substring that matches the right-hand side of a production rule) on the top of the stack with the corresponding non-terminal symbol (the left-hand side of the production rule).
- The goal of shift reduce parsing is to reduce the input string to the start symbol of the grammar.
- Shift reduce parsing is a type of bottom-up parsing as it generates a parse tree from the leaves (bottom) to the root (up).
- Shift reduce parsing can handle left-recursive grammars, but not right-recursive grammars.
- Shift reduce parsing can detect syntax errors as soon as they occur, but it may not report them until later.
- Shift reduce parsing can be implemented using a finite state machine with a stack.
- Shift reduce parsing can be classified into different types based on the way the parsing table is constructed, such as SLR, LALR, LR, and CLR.