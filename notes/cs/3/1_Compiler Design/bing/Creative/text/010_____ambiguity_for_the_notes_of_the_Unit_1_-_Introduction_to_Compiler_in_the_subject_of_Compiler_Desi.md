### Ambiguity

- Ambiguity in grammar is not good for a compiler construction.
- A grammar is ambiguous if it can produce more than one parse tree for the same sentence  .
- An ambiguous grammar or string can have multiple meanings.
- Ambiguity can cause confusion and errors in the syntax analysis phase of the compiler .
- No method can detect and remove ambiguity automatically, but it can be removed by either re-writing the whole grammar without ambiguity, or by setting and following associativity and precedence constraints  .
- Some common sources of ambiguity are:
  - Left recursion: A grammar is left recursive if it has a rule of the form A -> Aα, where A is a non-terminal and α is a string of terminals and non-terminals. Left recursion can cause infinite loops in top-down parsers.
  - Dangling else: A grammar is ambiguous if it has a rule of the form S -> if E then S else S | if E then S | other, where E is an expression and S is a statement. Dangling else can cause ambiguity in the interpretation of nested if-else statements.
  - Operator precedence and associativity: A grammar is ambiguous if it has rules of the form E -> E + E | E * E | id, where E is an expression and id is an identifier. Operator precedence and associativity can cause ambiguity in the evaluation of arithmetic expressions .