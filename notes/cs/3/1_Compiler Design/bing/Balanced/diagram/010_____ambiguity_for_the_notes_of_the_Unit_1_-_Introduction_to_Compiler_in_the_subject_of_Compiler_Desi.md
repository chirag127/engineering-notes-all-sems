### Ambiguity

- Ambiguity in grammar is not good for a compiler construction.
- A grammar is ambiguous if it produces more than one parse tree for some sentence.
- An ambiguous grammar or string can have multiple meanings.
- Ambiguity can cause confusion and errors in the syntax analysis phase of the compiler.
- No method can detect and remove ambiguity automatically, but it can be removed by either re-writing the whole grammar without ambiguity, or by setting and following associativity and precedence constraints.
- Some common sources of ambiguity are:
  - Left recursion: A grammar is left recursive if it has a non-terminal that derives to itself on the left. For example, `A -> Aa | b`.
  - Dangling else: A grammar is ambiguous if it has an `if-then-else` statement that can be associated with more than one `if` statement. For example, `if E1 then if E2 then S1 else S2`.
  - Operator precedence: A grammar is ambiguous if it has operators that can be interpreted in more than one way depending on their order or grouping. For example, `E -> E + E | E * E | id`.
- Some methods to eliminate ambiguity are:
  - Removing left recursion: A left recursive grammar can be converted to a right recursive grammar by applying a transformation rule. For example, `A -> Aa | b` can be rewritten as `A -> bA'` and `A' -> aA' | ɛ`.
  - Adding brackets: A grammar can be made unambiguous by using brackets to explicitly indicate the grouping or nesting of statements or expressions. For example, `if E1 then (if E2 then S1 else S2)` or `E -> E + E | E * E | (E) | id`.
  - Introducing precedence rules: A grammar can be made unambiguous by defining the order of evaluation of operators and using different non-terminals for different levels of precedence. For example, `E -> E + T | T` and `T -> T * F | F` and `F -> (E) | id`.