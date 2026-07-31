# Parsers for the notes of the Unit 2 - Basic Parsing Techniques in the subject of Compiler Design

- A parser is a program that is part of the compiler, and parsing is part of the compiling process.
- Parsing happens during the analysis stage of compilation. In parsing, code is taken from the preprocessor, broken into smaller pieces and analyzed so other software can understand it.
- The parser takes a token string as input and with the help of existing grammar, converts it into the corresponding Intermediate Representation (IR). The parser is also known as Syntax Analyzer.
- There are two main types of parsers: top-down parsers and bottom-up parsers.
- Top-down parsers start from the root of the parse tree and try to match the input with the grammar rules. They use a stack to store the intermediate results and predict the next production to apply.
- Bottom-up parsers start from the leaves of the parse tree and try to reduce the input to the start symbol of the grammar. They use a stack to store the intermediate results and apply the production that matches the top of the stack and the input.
- Top-down parsers can be further classified into recursive descent parsers and predictive parsers.
- Recursive descent parsers are a type of top-down parsers that use recursive functions to implement each non-terminal of the grammar. They may have more than one production to choose from for a single instance of input, which can lead to backtracking.
- Predictive parsers are a type of top-down parsers that use a parsing table to decide which production to apply based on the input and the stack element. They do not require backtracking, but they can only handle a subset of grammars called LL(1) grammars.
- Bottom-up parsers can be further classified into shift-reduce parsers and operator-precedence parsers.
- Shift-reduce parsers are a type of bottom-up parsers that use two operations: shift and reduce. Shift moves the next input symbol to the top of the stack, and reduce applies a production that matches the top of the stack and replaces it with the left-hand side of the production.
- Operator-precedence parsers are a type of bottom-up parsers that use a precedence table to determine the order of operations and operands. They can handle a subset of grammars called operator-precedence grammars, which have no ambiguity and no left recursion.