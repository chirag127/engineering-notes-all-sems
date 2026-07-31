# Top-Down Parsing for Compiler Design

- Top-down parsing is a method of parsing the input string provided by the lexical analyzer and generating a parse tree for it using leftmost derivation.
- The parse tree is constructed from the top (root) to the bottom (leaves) by expanding the non-terminals according to the grammar rules .
- The top-down parser tries to match the input string with the leftmost symbol of the grammar and then replaces it with the right-hand side of the production.
- The top-down parser can be classified into two types: recursive descent parser and predictive parser.
- Recursive descent parser is a top-down parser that uses a set of recursive procedures for each non-terminal in the grammar .
- Predictive parser is a top-down parser that does not require backtracking and uses a stack and a parsing table to guide the parsing process.
- The advantages of top-down parsing are that it is easy to implement, intuitive to understand, and suitable for LL grammars.
- The disadvantages of top-down parsing are that it may require backtracking, which is inefficient and may cause ambiguity, and that it cannot handle left recursion in the grammar .