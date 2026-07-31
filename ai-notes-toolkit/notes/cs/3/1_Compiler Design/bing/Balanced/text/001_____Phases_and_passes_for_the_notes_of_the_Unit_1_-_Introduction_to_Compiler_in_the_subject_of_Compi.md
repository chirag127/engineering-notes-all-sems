### Phases and Passes of Compiler

- A compiler is a software that converts a source program written in a high-level language into a target program written in a low-level language.
- The compilation process involves several steps, which are called phases of the compiler.
- Each phase of the compiler takes input from the previous phase, performs some tasks, and produces output for the next phase.
- The number of times the compiler scans the source program is called the number of passes of the compiler.
- A pass can consist of one or more phases, depending on the design of the compiler.
- The main phases of a compiler are:

  - Lexical analysis: This phase scans the source program and converts it into a sequence of tokens, which are the basic units of the language, such as keywords, identifiers, literals, operators, etc.
  - Syntax analysis: This phase checks the syntactic structure of the source program and builds a parse tree, which represents the hierarchical relationship among the tokens.
  - Semantic analysis: This phase checks the semantic meaning of the source program and performs tasks such as type checking, scope checking, declaration checking, etc. It also annotates the parse tree with additional information, such as types, values, addresses, etc.
  - Intermediate code generation: This phase translates the parse tree into an intermediate representation, which is independent of the source and target languages. The intermediate representation can be in the form of an abstract syntax tree, a three-address code, a quadruple, etc.
  - Code optimization: This phase improves the quality of the intermediate code by applying various techniques, such as constant folding, dead code elimination, loop optimization, etc. The goal is to reduce the execution time and space requirements of the target program.
  - Code generation: This phase converts the optimized intermediate code into the target code, which is specific to the target machine. The target code can be in the form of assembly language, machine code, or bytecode.

- The following diagram shows the phases and passes of a compiler:

![Phases and passes of a compiler](https://t4tutorials.com/wp-content/uploads/2018/04/Phases-of-compiler-design.png)

- Source: [Passes and Phases of Compiler Design | T4Tutorials.com](https://t4tutorials.com/passes-and-phases-of-compiler-design/)