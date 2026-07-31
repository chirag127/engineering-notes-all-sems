### Shift Reduce Parsing

Shift reduce parsing is a type of bottom-up parsing that uses a stack and an input buffer to construct a parse tree for a given input string and a grammar. Shift reduce parsing performs two actions: shift and reduce.

- Shift: This involves moving symbols from the input buffer onto the stack.
- Reduce: This involves replacing a handle (a substring of the stack that matches the right-hand side of a production) with the corresponding left-hand side non-terminal.

The goal of shift reduce parsing is to reduce the input string to the start symbol of the grammar by applying shift and reduce actions until either the input is accepted or an error is detected.

Shift reduce parsing is efficient and table-driven, but it has some limitations:

- It cannot handle left-recursive grammars, as they may cause infinite loops of shifting and reducing.
- It may encounter conflicts, such as shift-reduce conflict (when both shift and reduce actions are possible for the same input) or reduce-reduce conflict (when more than one reduce action is possible for the same input).
- It may not be able to parse some ambiguous grammars, as they may have more than one possible parse tree for the same input.

To overcome these limitations, some variations of shift reduce parsing have been developed, such as LR parsing, SLR parsing, LALR parsing, and CLR parsing. These methods use different techniques to construct the parsing table and resolve the conflicts.