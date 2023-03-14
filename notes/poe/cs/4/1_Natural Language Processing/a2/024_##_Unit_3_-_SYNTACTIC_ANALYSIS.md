 Here is the content in markdown format for ## Unit 3 - SYNTACTIC ANALYSIS:

## Unit 3 - SYNTACTIC ANALYSIS

### Introduction
- Syntactic analysis is the process of analyzing the source code of a program and verifying that it conforms to the syntax of the programming language.
- It is also known as parsing.
- The syntax of a programming language defines the set of rules that govern the structure of the statements in that language.
- The syntactic analysis is performed by a component called a parser. The parser reads the input characters or tokens and groups them into meaningful syntactic units called phrases or statements.
- The goal is to determine if the code is structurally correct (if it adheres to the syntax of the language) or incorrect (if it violates the syntax rules).

### Phases of Syntactic Analysis
1. Tokenization - The input characters are converted into tokens (lexical analysis).
2. Phrase building - The tokens are combined to form phrases.
3. Parsing - The phrases are combined and the syntactic structure of the input is analyzed.
- During parsing, the parser verifies if the syntactic structure conforms to the rules of the language grammar. If yes, the input is syntactically correct. If no, a syntax error is reported.

### Top-down Parsing
- Reads the input from left to right.
- Starts with the start symbol of the grammar and attempts to replace it with the right-hand side of the production rules.
- The parse tree is built top-down.
- Examples: LL(1) parsing, recursive descent parsing.

### Bottom-up Parsing
- Reads the input from right to left.
- Starts with the tokens and attempts to combine them into higher-level syntactic units.
- The parse tree is built bottom-up.
- Examples: LR parsing, GLR parsing.

[Further details, examples and diagrams can be added here as required to explain the concepts thoroughly]