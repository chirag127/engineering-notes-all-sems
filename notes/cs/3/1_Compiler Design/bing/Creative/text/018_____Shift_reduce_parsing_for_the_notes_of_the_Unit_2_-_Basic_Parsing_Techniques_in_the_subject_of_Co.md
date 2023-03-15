### Shift reduce parsing

- Shift reduce parsing is a process of reducing a string to the start symbol of a grammar  .
- Shift reduce parsing is a class of efficient, table-driven bottom-up parsing methods for computer languages and other notations formally defined by a grammar.
- The parsing methods most commonly used for parsing programming languages, LR parsing and its variations, are shift-reduce methods.
- Shift reduce parsing uses a stack to hold the grammar and an input tape to hold the string.
- Shift reduce parsing performs the two actions: shift and reduce .
  - Shift: This involves moving symbols from the input buffer onto the stack .
  - Reduce: This involves replacing a handle (a substring that matches the right-hand side of a production) on the top of the stack by the non-terminal on the left-hand side of the production .
- Shift reduce parsing generates a parse tree from the leaves (bottom) to the root (up), which is a type of bottom-up parsing.
- Shift reduce parsing can be achieved by directly handling the rightmost derivation from the starting symbol to the input string.
- Shift reduce parsing can handle a large class of context-free grammars, but not all of them.
- Shift reduce parsing can be ambiguous, meaning that there can be more than one way to reduce a string to the start symbol.
- Shift reduce parsing can be implemented using a finite state machine with a stack, which is called a pushdown automaton.