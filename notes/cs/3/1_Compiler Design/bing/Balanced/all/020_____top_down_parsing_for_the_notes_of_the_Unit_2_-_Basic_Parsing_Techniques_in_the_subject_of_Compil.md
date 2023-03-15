# Top-Down Parsing

- Top-down parsing is a method of parsing the input string provided by the lexical analyzer.
- The top-down parser parses the input string and then generates the parse tree for it.
- Construction of the parse tree starts from the root node i.e. the start symbol of the grammar.
- The parser expands the non-terminals in the leftmost derivation until all the leaves are terminals that match the input string.
- Top-down parsing can be done with or without backtracking.
- Backtracking means that the parser may try multiple rules or productions to identify the match for the input string, and may undo some steps if the match fails.
- Top-down parsing can be implemented using recursive or non-recursive techniques.
- Recursive descent parsing is a top-down parsing technique that uses recursive functions to match the input string with the grammar rules.
- Non-recursive parsing is a top-down parsing technique that uses a stack to store the intermediate results and avoid recursion.
- Predictive parsing is a type of non-recursive parsing that does not require backtracking. It uses a parsing table to determine which production to apply based on the current input symbol and the top of the stack.
- LL parsing is a type of predictive parsing that scans the input string from left to right and constructs a leftmost derivation. LL stands for Left to right scan and Leftmost derivation.
- LL(1) parsing is a special case of LL parsing that requires only one symbol of lookahead to decide which production to apply. LL(1) grammars are a subset of context-free grammars that are suitable for top-down parsing.