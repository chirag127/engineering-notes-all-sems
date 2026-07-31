# Shift Reduce Parsing

Shift reduce parsing is a bottom-up parsing technique that builds the parse tree from the leaves (bottom) to the root (up) by applying two actions: shift and reduce.   

- Shift: This involves moving symbols from the input buffer onto the stack.   
- Reduce: This involves replacing a handle (a substring of the stack that matches the right-hand side of a production rule) with the corresponding left-hand side symbol.   

Shift reduce parsing requires two data structures for its implementation: a stack and an input buffer.  

The algorithm for shift reduce parsing is as follows:   

- Initialize the stack with a special symbol $ and the input buffer with the input string followed by $.
- Repeat until the stack contains only the start symbol and the input buffer is empty:
  - If the top of the stack contains a handle, apply the reduce action by popping the handle from the stack and pushing the left-hand side symbol of the production rule that matches the handle.
  - Otherwise, apply the shift action by moving the next symbol from the input buffer to the top of the stack.
- If the parsing is successful, the parse tree can be constructed by tracing the sequence of reduce actions and attaching the subtrees corresponding to the handles.

Shift reduce parsing can be ambiguous or have conflicts when there are multiple possible actions for the same stack and input buffer configuration. There are two types of conflicts:  

- Shift-reduce conflict: This occurs when both shift and reduce actions are possible for the same configuration. This can be resolved by using precedence and associativity rules for the operators involved.
- Reduce-reduce conflict: This occurs when more than one reduce action is possible for the same configuration. This can be resolved by using the most specific production rule or by eliminating the ambiguity in the grammar.

Shift reduce parsing is efficient and can handle a large class of grammars, but it is not suitable for left-recursive grammars or grammars that require backtracking.   

Some variations of shift reduce parsing are:  

- LR parsing: This is a more general and powerful shift reduce parsing technique that uses a deterministic finite automaton to guide the parsing actions based on the stack and the input buffer.
- SLR parsing: This is a simplified version of LR parsing that uses the follow sets of the non-terminals to construct the parsing table.
- LALR parsing: This is a variation of LR parsing that combines the states with the same core items to reduce the size of the parsing table.