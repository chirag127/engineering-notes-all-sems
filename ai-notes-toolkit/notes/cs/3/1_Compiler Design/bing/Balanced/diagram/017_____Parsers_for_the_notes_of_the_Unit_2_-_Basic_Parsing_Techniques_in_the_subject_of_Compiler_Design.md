### Parsers

A parser is a program that is part of the compiler, and parsing is part of the compiling process. Parsing happens during the analysis stage of compilation. In parsing, code is taken from the preprocessor, broken into smaller pieces and analyzed so other software can understand it.

The parser is also known as syntax analyzer. The parser takes a token string as input and with the help of existing grammar, converts it into the corresponding intermediate representation (IR).

There are different types of parsers in compiler design, such as:

- Top-down parsers: These parsers start from the root of the parse tree and try to match the input with the grammar rules. They use leftmost derivation to generate the parse tree. Examples of top-down parsers are recursive descent parser and predictive parser.
- Bottom-up parsers: These parsers start from the leaves of the parse tree and try to reduce the input to the start symbol of the grammar. They use rightmost derivation to generate the parse tree. Examples of bottom-up parsers are shift-reduce parser, operator-precedence parser, LR parser, etc.
- Hybrid parsers: These parsers combine the features of both top-down and bottom-up parsers. They use both leftmost and rightmost derivation to generate the parse tree. Examples of hybrid parsers are Earley parser, GLR parser, etc.

The following diagram shows the classification of parsers:

![Classification of parsers](https://media.geeksforgeeks.org/wp-content/uploads/20210607141718/Types-of-Parsers-in-Compiler-Design.png)