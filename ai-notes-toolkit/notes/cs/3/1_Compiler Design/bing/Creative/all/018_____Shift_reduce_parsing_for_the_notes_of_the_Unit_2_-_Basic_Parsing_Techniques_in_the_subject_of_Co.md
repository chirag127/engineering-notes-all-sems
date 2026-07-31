# Shift Reduce Parsing

Shift reduce parsing is a type of bottom-up parsing that uses a stack and an input buffer to construct a parse tree for a given input string and a grammar. Shift reduce parsing performs two actions: shift and reduce .

- Shift: This involves moving symbols from the input buffer onto the stack.
- Reduce: This involves replacing a handle (a substring of the stack that matches the right-hand side of a production) with the corresponding left-hand side non-terminal.

The parsing process starts with an empty stack and the input string in the input buffer. The parser repeatedly applies shift or reduce actions until either the stack contains the start symbol of the grammar and the input buffer is empty, or no action is possible. In the former case, the parsing is successful and the parse tree can be obtained by tracing the reductions. In the latter case, the parsing fails and the input string is not accepted by the grammar .

Shift reduce parsing is efficient and table-driven, but it has some limitations. For example, it cannot handle left-recursive grammars, ambiguous grammars, or grammars that require more than one symbol of lookahead. To overcome these limitations, variations of shift reduce parsing, such as LR parsing, SLR parsing, LALR parsing, and CLR parsing, have been developed. These variations use different techniques to construct the parsing tables and resolve conflicts that may arise during parsing.