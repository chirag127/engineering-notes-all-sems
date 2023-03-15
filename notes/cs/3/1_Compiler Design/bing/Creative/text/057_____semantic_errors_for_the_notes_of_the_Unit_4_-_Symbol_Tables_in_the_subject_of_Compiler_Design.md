### Semantic errors

- Semantic errors are errors that arise when a statement used in a program is not meaningful, that is, it does not correspond to the set of rules (semantics) for that language being used.
- Semantic errors can be detected by the compiler (static semantic errors) or by the runtime system (dynamic semantic errors).
- Some examples of semantic errors are :
  - Type mismatch: when the data types of two operands are not compatible, such as adding a string and a number.
  - Undeclared variables: when a variable is used without being declared in the current scope, such as using x before declaring it.
  - Reserved identifier misuse: when a keyword or a predefined name is used as a variable name, such as using int as a variable name.
- Semantic errors can be recovered by using a symbol table for the corresponding identifier and by performing automatic type conversion by the compiler.
- Semantic errors can cause unexpected results, crashes, or exceptions in the program execution.