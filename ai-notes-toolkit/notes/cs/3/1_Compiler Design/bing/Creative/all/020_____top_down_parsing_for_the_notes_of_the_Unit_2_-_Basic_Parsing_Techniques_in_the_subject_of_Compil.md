# Top-Down Parsing

- Top-down parsing is a method of parsing the input string provided by the lexical analyzer.
- The top-down parser parses the input string and then generates the parse tree for it.
- Construction of the parse tree starts from the root node i.e. the start symbol of the grammar.
- The parser expands the non-terminals using the grammar productions and matches the terminals with the input symbols.
- The parser uses leftmost derivation to generate the parse tree.
- The parser stops when the input string is consumed and the parse tree is complete.

## Types of Top-Down Parsers

- There are two types of top-down parsers: recursive descent parser and predictive parser.
- Recursive descent parser is a top-down parser that uses a set of recursive procedures to process the input string.
- Each procedure corresponds to a non-terminal symbol in the grammar.
- The parser calls the procedure for the start symbol and then recursively calls the procedures for the non-terminals in the right-hand side of the production.
- The parser backtracks if a procedure fails to match the input string.
- Predictive parser is a top-down parser that does not use backtracking.
- It predicts the next production to be used based on the current input symbol and the top of the stack.
- It uses a parsing table to store the predictions for each non-terminal and input symbol pair.
- The parser is also known as LL(1) parser, where L stands for left-to-right scanning of the input, L stands for leftmost derivation, and 1 stands for one symbol lookahead.