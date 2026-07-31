### Phases and passes for the notes of the Unit 1 - Introduction to Compiler in the subject of Compiler Design

- A compiler is a software that converts a source program written in a high-level language into a target program written in a low-level language.
- The compilation process involves several steps, which are called phases of the compiler.
- Each phase of the compiler takes input from the previous phase, performs some tasks, and produces output for the next phase.
- The phases of the compiler can be grouped into two main categories: analysis phase and synthesis phase.
- The analysis phase checks the syntax and semantics of the source program and creates an intermediate representation of the program.
- The synthesis phase generates the target program from the intermediate representation and performs some optimizations to improve the performance of the code.
- The phases of the compiler are:

  - Lexical analysis: It scans the source code and converts it into a sequence of tokens, which are the basic units of the language, such as keywords, identifiers, literals, operators, etc.
  - Syntax analysis: It parses the tokens and checks if they follow the grammar rules of the language. It also builds a parse tree or an abstract syntax tree, which represents the hierarchical structure of the program.
  - Semantic analysis: It performs type checking, scope checking, and other semantic checks to ensure the validity and meaning of the program. It also annotates the parse tree or the abstract syntax tree with additional information, such as types, values, etc.
  - Intermediate code generation: It translates the parse tree or the abstract syntax tree into an intermediate code, which is a low-level representation of the program, such as three-address code, quadruples, triples, etc.
  - Code optimization: It applies various techniques to improve the quality and efficiency of the intermediate code, such as eliminating dead code, reducing redundancy, simplifying expressions, etc.
  - Code generation: It converts the optimized intermediate code into the target code, which is the machine code or the assembly code for the target platform. It also performs some tasks, such as register allocation, instruction selection, etc.

- A pass of the compiler is the number of times the compiler scans the source program or the intermediate code.
- A pass can consist of one or more phases of the compiler.
- A single-pass compiler scans the source program only once and generates the target code directly, without producing any intermediate code. It is fast and simple, but it has some limitations, such as forward references, error detection, etc.
- A two-pass compiler scans the source program twice and generates the target code. The first pass collects some information, such as symbol table, labels, etc., and the second pass uses that information to generate the code. It can handle forward references and error detection better than a single-pass compiler, but it is slower and more complex.
- A multi-pass compiler scans the source program or the intermediate code more than twice and performs various transformations and optimizations on the code. It can produce high-quality and efficient code, but it is very slow and complicated.