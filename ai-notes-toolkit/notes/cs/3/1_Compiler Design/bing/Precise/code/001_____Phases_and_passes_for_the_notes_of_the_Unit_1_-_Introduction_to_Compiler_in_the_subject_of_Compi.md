### Phases and passes for the notes of the Unit 1 - Introduction to Compiler in the subject of Compiler Design

A compiler is a program that translates source code written in a high-level programming language into machine code that can be executed by a computer. The process of compilation is divided into several phases and passes.

1. **Lexical Analysis:** The first phase of compilation is lexical analysis, also known as scanning. In this phase, the source code is divided into a sequence of tokens, which are the smallest units of the program that have meaning. Tokens include keywords, identifiers, literals, and operators.

2. **Syntax Analysis:** The second phase of compilation is syntax analysis, also known as parsing. In this phase, the sequence of tokens is checked to ensure that it follows the rules of the programming language's grammar. The result of this phase is a parse tree, which represents the structure of the program.

3. **Semantic Analysis:** The third phase of compilation is semantic analysis. In this phase, the compiler checks the program for semantic errors, such as type mismatches and undeclared variables. The result of this phase is an annotated parse tree, which includes information about the types of expressions and the declarations of variables.

4. **Intermediate Code Generation:** The fourth phase of compilation is intermediate code generation. In this phase, the compiler generates an intermediate representation of the program, which is a low-level, machine-independent representation of the program.

5. **Code Optimization:** The fifth phase of compilation is code optimization. In this phase, the compiler applies various techniques to improve the efficiency of the generated code.

6. **Code Generation:** The final phase of compilation is code generation. In this phase, the compiler generates machine code that can be executed by the target machine.

A pass is a single traversal of the source code by the compiler. A compiler may make multiple passes over the source code, with each pass performing one or more of the above phases. For example, a compiler may make one pass to perform lexical analysis and syntax analysis, and another pass to perform semantic analysis and intermediate code generation.