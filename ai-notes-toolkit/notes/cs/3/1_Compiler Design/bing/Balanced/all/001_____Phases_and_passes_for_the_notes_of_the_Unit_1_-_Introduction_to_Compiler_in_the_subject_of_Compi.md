# Phases and Passes of Compiler

## Phases of Compiler

- A compiler is a software that converts a high-level language program into a low-level language program that can be executed by the computer.
- A compiler consists of several steps or phases, each of which performs a specific task on the source code.
- The phases of a compiler are:

  - **Lexical analysis**: This phase scans the source code and converts it into a sequence of tokens, which are the smallest meaningful units of the program. Tokens can be keywords, identifiers, literals, operators, etc.
  - **Syntax analysis**: This phase checks the syntactic structure of the program and verifies that it follows the rules of the grammar of the language. It also builds a parse tree, which is a hierarchical representation of the program.
  - **Semantic analysis**: This phase checks the meaning and logic of the program and performs tasks such as type checking, scope resolution, constant folding, etc. It also annotates the parse tree with semantic information.
  - **Intermediate code generation**: This phase translates the parse tree into an intermediate code, which is a low-level representation of the program that is independent of the target machine. Intermediate code can be in the form of quadruples, triples, or abstract syntax tree.
  - **Code optimization**: This phase improves the quality and efficiency of the intermediate code by applying various techniques such as dead code elimination, loop optimization, common subexpression elimination, etc.
  - **Code generation**: This phase generates the final executable code for the target machine by mapping the intermediate code to the machine instructions and registers. It also performs tasks such as register allocation, instruction scheduling, etc.

## Passes of Compiler

- A pass of a compiler is the number of times the compiler scans the entire source code or a part of it.
- A pass can consist of one or more phases of the compiler.
- The passes of a compiler are:

  - **Single pass compiler**: This compiler scans the source code only once and performs all the phases of the compiler in one pass. It is fast and simple, but it has some limitations such as forward references, error detection, etc.
  - **Two pass compiler**: This compiler scans the source code twice and performs some phases of the compiler in the first pass and the rest in the second pass. It can handle forward references and error detection better than a single pass compiler, but it is slower and more complex.
  - **Multi pass compiler**: This compiler scans the source code more than twice and performs each phase of the compiler in a separate pass. It can perform more sophisticated analysis and optimization than a single or two pass compiler, but it is slower and more complex.