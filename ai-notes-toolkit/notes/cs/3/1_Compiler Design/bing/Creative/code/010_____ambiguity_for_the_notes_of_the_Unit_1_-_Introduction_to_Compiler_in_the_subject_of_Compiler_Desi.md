# Ambiguity in Compiler Design

- Ambiguity in grammar is not good for a compiler construction.
- A grammar is ambiguous if it can produce more than one parse tree for the same sentence  .
- An ambiguous grammar or string can have multiple meanings.
- Ambiguity can cause confusion and errors in the syntax analysis phase of the compiler .
- No method can detect and remove ambiguity automatically, but it can be removed by either re-writing the whole grammar without ambiguity, or by setting and following associativity and precedence constraints  .
- Some common examples of ambiguity in grammar are:
  - Dangling-else ambiguity: The else clause can be associated with either the inner or the outer if statement.
  - Arithmetic expressions ambiguity: The order of evaluation of operators can be different depending on the precedence and associativity rules.
  - Operator overloading ambiguity: The same operator can have different meanings depending on the context and the operands.