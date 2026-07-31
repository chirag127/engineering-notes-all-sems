### Ambiguity

- Ambiguity in grammar is not good for a compiler construction.
- A grammar is ambiguous if it produces more than one parse tree for some sentence.
- An ambiguous grammar or string can have multiple meanings.
- Ambiguity can cause confusion and errors in the syntax analysis and code generation phases of a compiler.
- No method can detect and remove ambiguity automatically, but it can be removed by either re-writing the whole grammar without ambiguity, or by setting and following associativity and precedence constraints.
- Some common sources of ambiguity are:
  - Left recursion: A grammar is left recursive if it has a non-terminal that derives to itself on the left. For example, `A -> Aa | b` is left recursive. Left recursion can cause infinite loops in top-down parsers.
  - Dangling else: A grammar is ambiguous if it has an `if-then-else` statement that can be associated with more than one `if` statement. For example, `if E1 then if E2 then S1 else S2` is ambiguous because the `else` can be matched with either `if`. Dangling else can cause incorrect interpretation of the conditional statements.
- Some methods to eliminate ambiguity are:
  - Removing left recursion: A left recursive grammar can be converted to a right recursive grammar by applying a transformation rule. For example, `A -> Aa | b` can be transformed to `A -> bA'` and `A' -> aA' | ε` where `ε` is the empty string. This eliminates the possibility of infinite loops in top-down parsers.
  - Adding brackets: A grammar can be made unambiguous by adding brackets to indicate the scope of the statements. For example, `if E1 then if E2 then S1 else S2` can be written as `if E1 then { if E2 then S1 else S2 }` or `if E1 then { if E2 then S1 } else S2` depending on the intended meaning. This eliminates the confusion of the dangling else.
  - Using precedence and associativity rules: A grammar can be made unambiguous by defining the order and direction of the operators. For example, `E -> E + E | E * E | id` is ambiguous because it can produce different parse trees for `id + id * id`. This can be resolved by specifying that `*` has higher precedence than `+` and both are left associative. This means that `id + id * id` is equivalent to `id + (id * id)`. This eliminates the ambiguity of the expression.