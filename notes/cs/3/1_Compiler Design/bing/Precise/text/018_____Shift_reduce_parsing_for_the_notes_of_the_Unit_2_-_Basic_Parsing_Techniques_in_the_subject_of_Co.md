### Shift Reduce Parsing

Shift reduce parsing is a process of reducing a string to the start symbol of a grammar. It is a class of efficient, table-driven bottom-up parsing methods for computer languages and other notations formally defined by a grammar. The parsing methods most commonly used for parsing programming languages, LR parsing and its variations, are shift-reduce methods.

Shift reduce parsing uses a stack to hold the grammar and an input tape to hold the string. It performs two actions: shift and reduce. At the shift action, the current symbol in the input string is pushed to a stack. At each reduction, the symbols will be replaced by the non-terminals.

The parser scans and parses the input text in one forward pass over the text, without backing up. It builds up the parse tree incrementally, bottom up, and left to right, without guessing or backtracking.