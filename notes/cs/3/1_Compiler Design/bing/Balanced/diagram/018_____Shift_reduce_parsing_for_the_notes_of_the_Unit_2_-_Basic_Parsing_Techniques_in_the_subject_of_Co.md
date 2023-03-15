### Shift reduce parsing

- Shift reduce parsing is a class of efficient, table-driven bottom-up parsing methods for computer languages and other notations formally defined by a grammar.
- Shift reduce parsing uses a stack to hold the grammar symbols and an input buffer to hold the input string.
- Shift reduce parsing performs two actions: shift and reduce.
  - Shift: This involves moving the current symbol from the input buffer onto the stack .
  - Reduce: This involves replacing a handle (a substring of the stack that matches the right-hand side of a production rule) by the corresponding non-terminal symbol on the stack .
- The goal of shift reduce parsing is to reduce the input string to the start symbol of the grammar.
- Shift reduce parsing can be implemented using a finite state automaton with a stack, called a pushdown automaton.
- Shift reduce parsing can handle various classes of grammars, such as LR(k), SLR(k), LALR(k), and CLR(k) grammars.
- Shift reduce parsing can detect and report syntax errors in the input string by using error recovery strategies.
- Shift reduce parsing can generate a parse tree from the leaves (bottom) to the root (up) by recording the sequence of reductions applied.