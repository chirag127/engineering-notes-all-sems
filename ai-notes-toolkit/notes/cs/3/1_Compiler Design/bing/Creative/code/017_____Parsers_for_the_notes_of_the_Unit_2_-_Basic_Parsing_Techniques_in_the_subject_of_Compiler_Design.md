### Parsers for the notes of the Unit 2 - Basic Parsing Techniques in the subject of Compiler Design

- A parser is a program that is part of the compiler, and parsing is part of the compiling process.
- Parsing happens during the analysis stage of compilation. In parsing, code is taken from the preprocessor, broken into smaller pieces and analyzed so other software can understand it.
- The parser takes a token string as input and with the help of existing grammar, converts it into the corresponding Intermediate Representation (IR). The parser is also known as Syntax Analyzer.
- The parser checks the syntax of the source program and reports any errors. It also constructs a parse tree or syntax tree, which is a hierarchical representation of the structure of the source program.
- There are two types of parsers: top-down parsers and bottom-up parsers.
- Top-down parsers start from the root of the parse tree and try to match the input with the grammar rules. They use a stack to store the intermediate results and predict the next production to apply.
- Bottom-up parsers start from the leaves of the parse tree and try to reduce the input to the start symbol of the grammar. They use a stack to store the intermediate results and apply the production that matches the top of the stack and the input.
- Examples of top-down parsers are recursive descent parser and predictive parser. Examples of bottom-up parsers are shift-reduce parser and operator precedence parser.
- Top-down parsers are easier to implement and understand, but they cannot handle left recursion and left factoring in the grammar. Bottom-up parsers can handle a larger class of grammars, but they are more complex and difficult to implement.
- The choice of the parser depends on the characteristics of the source language, the target language, the compiler design and the performance requirements.