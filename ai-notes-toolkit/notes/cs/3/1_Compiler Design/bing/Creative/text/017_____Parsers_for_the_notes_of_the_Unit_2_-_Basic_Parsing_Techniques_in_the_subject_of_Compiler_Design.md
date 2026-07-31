### Parsers for the notes of the Unit 2 - Basic Parsing Techniques in the subject of Compiler Design

- A parser is a program that is part of the compiler, and parsing is part of the compiling process.
- Parsing happens during the analysis stage of compilation. In parsing, code is taken from the preprocessor, broken into smaller pieces and analyzed so other software can understand it.
- The parser takes a token string as input and with the help of existing grammar, converts it into the corresponding Intermediate Representation (IR). The parser is also known as Syntax Analyzer.
- There are two main types of parsers: top-down parsers and bottom-up parsers.
- Top-down parsers start from the root of the parse tree and try to match the input with the grammar rules. They use a stack to store the intermediate results and backtrack when a mismatch occurs.
- Bottom-up parsers start from the leaves of the parse tree and try to reduce the input to the start symbol of the grammar. They use a stack to store the intermediate results and shift or reduce the input according to the parsing table.
- Some examples of top-down parsers are recursive descent parser, predictive parser, and LL parser.
- Some examples of bottom-up parsers are shift-reduce parser, operator precedence parser, LR parser, and LALR parser.
- The advantages of top-down parsers are that they are easy to implement, can handle left recursion, and can report errors early.
- The disadvantages of top-down parsers are that they are inefficient, cannot handle left factoring, and may require backtracking.
- The advantages of bottom-up parsers are that they are efficient, can handle a larger class of grammars, and can detect errors at the end.
- The disadvantages of bottom-up parsers are that they are difficult to implement, cannot handle ambiguous grammars, and may report errors late.