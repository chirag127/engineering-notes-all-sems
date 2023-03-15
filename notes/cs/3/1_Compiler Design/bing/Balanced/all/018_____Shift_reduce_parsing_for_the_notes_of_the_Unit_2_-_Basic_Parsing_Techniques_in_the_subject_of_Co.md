# Shift Reduce Parsing

Shift reduce parsing is a bottom-up parsing technique that builds the parse tree from the leaves (bottom) to the root (up) by applying two actions: shift and reduce  .

- Shift: This involves moving symbols from the input buffer onto the stack.
- Reduce: This involves replacing a handle (a substring that matches the right-hand side of a production rule) on the top of the stack with the corresponding left-hand side symbol.

Shift reduce parsing requires two data structures for its implementation: a stack and an input buffer .

The steps of shift reduce parsing are as follows  :

1. Initialize the stack with a special symbol $ and the input buffer with the input string followed by $.
2. Repeat the following steps until either an error or acceptance occurs:
   - If the top of the stack contains the start symbol of the grammar and the input buffer contains only $, then accept the input and stop.
   - If the top of the stack contains a handle, then apply a reduce action by popping the handle from the stack and pushing the corresponding left-hand side symbol onto the stack.
   - If the top of the stack does not contain a handle and the input buffer is not empty, then apply a shift action by moving the next symbol from the input buffer onto the stack.
   - If none of the above conditions apply, then report an error and stop.

Shift reduce parsing can be implemented using different algorithms, such as LR parsing, SLR parsing, LALR parsing, and CLR parsing  . These algorithms differ in how they resolve conflicts that may arise during parsing, such as shift/reduce conflicts and reduce/reduce conflicts .

Shift/reduce conflict: This occurs when the parser has to choose between shifting the next input symbol onto the stack or reducing the handle on the top of the stack .

Reduce/reduce conflict: This occurs when the parser has to choose between reducing the handle on the top of the stack by two or more different production rules.

Shift reduce parsing is an efficient and powerful method for parsing programming languages and other notations formally defined by a grammar. However, it also has some limitations, such as requiring the grammar to be unambiguous and free of left recursion .