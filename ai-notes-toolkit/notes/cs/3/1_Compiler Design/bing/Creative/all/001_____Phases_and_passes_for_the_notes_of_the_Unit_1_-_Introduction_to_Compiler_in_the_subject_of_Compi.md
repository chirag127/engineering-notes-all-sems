# Phases and Passes of Compiler

## Phases of Compiler
- A phase of a compiler is a step in the compilation process that takes input from the previous stage, processes it and produces output that can be used as input for the next stage of the compiler .
- A phase of a compiler transforms the source code from one representation to another representation.
- The main phases of a compiler are:
  - Lexical analysis: It scans the source code and converts it into a sequence of tokens .
  - Syntax analysis: It checks the syntactic structure of the source code and builds a parse tree .
  - Semantic analysis: It checks the semantic meaning of the source code and performs type checking, scope checking, etc .
  - Intermediate code generation: It generates an intermediate representation of the source code that is independent of the source and target languages .
  - Code optimization: It improves the intermediate code by eliminating redundant or unnecessary code, applying various transformations, etc .
  - Code generation: It produces the final executable code for the target machine or platform .

## Passes of Compiler
- A pass of a compiler is the number of times the compiler traverses through the source code.
- A pass of a compiler can have more than one phase.
- The number of passes of a compiler depends on the complexity of the source and target languages, the design goals of the compiler, the available memory, etc.
- The types of passes of a compiler are:
  - Single pass compiler: It traverses through the source code only once and performs all the phases of compilation in one pass.
  - Two pass compiler: It traverses through the source code twice and performs some phases of compilation in the first pass and some phases in the second pass.
  - Multi pass compiler: It traverses through the source code more than twice and performs each phase of compilation in a separate pass.