### Top-Down Parsing for the Notes of the Unit 2 - Basic Parsing Techniques in the Subject of Compiler Design

- Top-down parsing is a method of parsing the input string provided by the lexical analyzer and generating the parse tree for it using leftmost derivation.
- The top-down parser starts from the root node (start symbol) and expands it using the grammar productions until it matches the input string.
- The top-down parser can be classified into two types: recursive descent parser and predictive parser.
- Recursive descent parser is a top-down parser that uses a procedure for each non-terminal symbol in the grammar. It recursively calls the procedures until it reaches the terminal symbols or fails to match the input string.
- Predictive parser is a top-down parser that does not require backtracking. It uses a stack and a parsing table to determine which production to apply next. It can only handle LL(1) grammars, which are a subset of context-free grammars.