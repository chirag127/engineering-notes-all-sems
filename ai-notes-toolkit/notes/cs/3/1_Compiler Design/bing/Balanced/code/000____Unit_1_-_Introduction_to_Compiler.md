## Unit 1 - Introduction to Compiler

A compiler is a program that translates a source program written in a high-level language into a target program written in a low-level language. The process of compilation involves several phases, each of which performs a specific task.

Some of the phases of a compiler are:

- Lexical analysis: This phase scans the source program and converts it into a sequence of tokens, each of which represents a meaningful symbol, such as a keyword, an identifier, a constant, or an operator.
- Syntax analysis: This phase checks the syntactic structure of the source program and builds a parse tree, which represents the hierarchical relationship among the tokens. This phase also reports any syntax errors in the source program.
- Semantic analysis: This phase performs type checking, scope checking, and other semantic checks on the source program and annotates the parse tree with additional information, such as data types, symbol tables, and intermediate code.
- Intermediate code generation: This phase translates the annotated parse tree into an intermediate representation, such as three-address code, quadruples, or triples, which is easier to manipulate and optimize than the source code.
- Code optimization: This phase applies various techniques to improve the performance and efficiency of the intermediate code, such as eliminating dead code, reducing loop overhead, and performing constant folding and propagation.
- Code generation: This phase converts the optimized intermediate code into the target code, which is usually machine code or assembly code. This phase also performs tasks such as register allocation, instruction selection, and code scheduling.
- Symbol table management: This phase maintains a data structure called a symbol table, which stores information about the identifiers used in the source program, such as their names, types, scopes, and addresses.
- Error handling: This phase detects and reports any errors that occur during the compilation process, such as lexical, syntactic, semantic, or runtime errors. This phase also provides meaningful error messages and recovery mechanisms to the user.