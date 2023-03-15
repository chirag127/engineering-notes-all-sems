### Semantic errors

- Semantic errors are errors that arise when a statement used in a program is not meaningful, that is, it does not correspond to the set of rules (semantics) for that language being used.
- Some of the semantic errors (the static semantic errors) are detected by the compiler, which generates a message indicating the type of error and the position in the source file where the error occurred.
- However, in most cases, the compiler will not be able to catch most of these types of problems, because the compiler is designed to enforce grammar, not intent.
- Semantic errors can be classified into the following categories:
  - Type mismatch: This occurs when the data types of two operands are not compatible, such as adding a string and an integer.
  - Undeclared variables: This occurs when a variable is used without being declared in the scope, such as using x before declaring int x.
  - Reserved identifier misuse: This occurs when a keyword or a predefined identifier is used as a user-defined identifier, such as using int as a variable name.
- Semantic errors can be recovered by using a symbol table for the corresponding identifier and if data types of two operands are not compatible, automatically type conversion is done by the compiler.
- Semantic analysis is the phase of compiler design that performs semantic checks and generates intermediate code for the source program. It uses the syntax tree and the symbol table as inputs and outputs a directed acyclic graph (DAG) or a three-address code (TAC) as intermediate representation .