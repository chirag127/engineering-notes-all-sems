 Here is the content in Markdown format without any emojis or external links:

### Bootstrapping for the notes of the Unit 1 - Introduction to Compiler in the subject of Compiler Design.

1. Compiler: A compiler is a computer program that transforms source code written in a programming language into another computer language (often having a binary form known as object code). The name "compiler" is primarily used for programs that translate source code from a high-level programming language to a lower level language (e.g., assembly language or machine code).

2. bootstrapping: The process of applying a compiler to itself to generate a new version of the compiler is called bootstrapping. This is done to upgrade the compiler to a new version. The result is a self-hosting compiler - a compiler that is capable of compiling its own source code.

3. Phases of compilation: The compilation process has 3 main phases:

(a) Lexical analysis: The input character stream is read and grouped into tokens (like identifiers, keywords, operators, and delimiters).
(b) Syntax analysis: The tokens are analysed to form a parse tree or syntax tree that represents the structure of the program.
(c) Semantic analysis: The parse tree is analysed to check for semantic errors and generate intermediate code.

4. Applications of compiler: Compilers are fundamental to modern computing and are used to convert high-level programming languages into low-level languages that a computer's processor can execute. Some applications are:

(a) System software: Operating systems, firmware, and system utilities are often written in languages such as C and C++ and compiled for specific computer architectures.
(b) Application software: Almost all commercial software is compiled before distribution. This includes complex applications such as databases, word processors, and browsers as well as simpler applications such as mobile apps.
(c) Programming tools: Compilers are often self-hosted and some parser generators use compiled parsers to analyze input and generate code.