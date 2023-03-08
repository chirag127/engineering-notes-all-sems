 Here is the content in markdown format for the given topic:

### Phases and passes for the notes of the Unit 1 - Introduction to Compiler in the subject of Compiler Design

The compilation process consists of the following phases:

1. Lexical Analysis phase:
- The input program is read and split into basic units called tokens.
- Tokens are classified into categories like identifiers, keywords, operators, literals, etc.
- A pattern matching technique called scanning is used.
- Examples of tokens: var, int, +, *, etc.
- Advantage: Reduces the complexity of the compiler by breaking up the input into meaningful symbols.

2. Syntax Analysis phase:
- The sequence of tokens is analyzed to check for the correctness of the structure as per the grammar of the language.
- A parse tree is created.
- Context-free grammars are used to define the syntax.
- Examples: Check for parantheses balance, matching operators and operands, etc.
- Advantage: Grammar errors are reported, making the compiler halt.

3. Semantic Analysis phase:
- Meaning is assigned to the syntax tree by checking for semantic errors like type mismatch, undeclared variables, etc.
- Types are associated with variables and expressions.
- Advantage: Logical errors are reported.

4. Code Generation phase:
- The intermediate representation is converted to machine language.
- Different code optimization techniques can be applied.
- Target code is platform dependent.
- Advantage: Increased efficiency and performance of the executable program.

The compilation process can consist of multiple passes where each pass performs one of the phases to detect and remove a specific type of error. The number of passes determines the type of compiler. A single-pass compiler performs all phases in one pass whereas a multi-pass compiler uses multiple passes.