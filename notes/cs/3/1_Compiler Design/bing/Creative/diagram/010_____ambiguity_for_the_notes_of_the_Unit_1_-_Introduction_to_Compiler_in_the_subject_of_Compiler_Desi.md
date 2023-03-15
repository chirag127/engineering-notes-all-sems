### Ambiguity

- Ambiguity in grammar is not good for a compiler construction.
- A grammar is ambiguous if it produces more than one parse tree for some sentence.
- An ambiguous grammar or string can have multiple meanings.
- Ambiguity can cause confusion and errors in the syntax analysis and code generation phases of a compiler.
- No method can detect and remove ambiguity automatically, but it can be removed by either re-writing the whole grammar without ambiguity, or by setting and following associativity and precedence constraints.
- Some common sources of ambiguity are:
  - Left recursion: A grammar is left recursive if it has a rule of the form A -> Aα, where A is a non-terminal and α is a string of terminals and non-terminals. Left recursion can cause infinite loops in top-down parsers.
  - Left factoring: A grammar is left factored if it has two or more rules with a common prefix. Left factoring can cause backtracking in top-down parsers.
  - Dangling else: A grammar is ambiguous if it has a rule of the form S -> if E then S else S, where E is an expression and S is a statement. Dangling else can cause ambiguity in the interpretation of nested if-else statements.
- Some methods to eliminate ambiguity are:
  - Removing left recursion: A left recursive grammar can be converted into an equivalent right recursive grammar by applying a transformation rule.
  - Left factoring: A left factored grammar can be converted into an equivalent grammar by extracting the common prefix and introducing a new non-terminal.
  - Adding parentheses: A grammar can be made unambiguous by adding parentheses to indicate the grouping and precedence of operators and operands.
  - Adding rules: A grammar can be made unambiguous by adding rules to specify the associativity and precedence of operators.