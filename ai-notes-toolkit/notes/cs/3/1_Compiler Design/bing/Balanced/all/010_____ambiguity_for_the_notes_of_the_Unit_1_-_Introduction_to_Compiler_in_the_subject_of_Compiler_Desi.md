# Ambiguity in Compiler Design

- Ambiguity in grammar is not good for a compiler construction.
- A grammar is ambiguous if it can produce more than one parse tree for the same sentence  .
- An ambiguous grammar or string can have multiple meanings.
- Ambiguity can cause problems in syntax analysis and semantic analysis of the source code.
- No method can detect and remove ambiguity automatically, but it can be removed by either re-writing the whole grammar without ambiguity, or by setting and following associativity and precedence constraints.
- Some common examples of ambiguity in grammar are:
  - Dangling-else ambiguity: The else clause can be associated with either the innermost or the outermost if statement.
  - Arithmetic expressions ambiguity: The order of evaluation of operators can be different depending on the precedence and associativity rules.
  - Operator overloading ambiguity: The same operator can have different meanings depending on the context and the operands.
- Some common methods to eliminate ambiguity are:
  - Introducing extra symbols or parentheses to clarify the intended meaning .
  - Modifying the production rules to avoid left recursion or common prefixes .
  - Using attributes or semantic actions to resolve the ambiguity at run time .