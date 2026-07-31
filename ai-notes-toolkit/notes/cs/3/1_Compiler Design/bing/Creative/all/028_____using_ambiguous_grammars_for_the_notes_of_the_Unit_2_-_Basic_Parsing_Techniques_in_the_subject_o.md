# Using Ambiguous Grammars for the Notes of the Unit 2 - Basic Parsing Techniques in the Subject of Compiler Design

- A grammar is a set of rules that define the syntax of a language, i.e., how the symbols of the language can be combined to form valid sentences.
- A grammar is ambiguous if it can generate more than one parse tree (or leftmost/rightmost derivation) for the same sentence, i.e., if the sentence has more than one possible interpretation according to the grammar rules.
- Ambiguous grammars are undesirable for compiler design because they can lead to confusion and inconsistency in the meaning and behavior of the source code.
- Some examples of ambiguous grammars are:

  - The grammar for arithmetic expressions with + and * operators, without specifying the precedence and associativity of the operators. For example, the sentence `a+b*c` can have two parse trees, one where `+` has higher precedence than `*`, and one where `*` has higher precedence than `+`.
  - The grammar for if-then-else statements, without specifying the association of the else clause with the nearest or the farthest if clause. For example, the sentence `if a then if b then c else d` can have two parse trees, one where the else clause is associated with the inner if, and one where the else clause is associated with the outer if.

- There are different ways to handle ambiguous grammars in compiler design, such as:

  - Eliminating the ambiguity by modifying the grammar rules to make them unambiguous. For example, the grammar for arithmetic expressions can be modified by introducing different non-terminals for different levels of precedence, such as `E -> E+T | T`, `T -> T*F | F`, `F -> (E) | id`. The grammar for if-then-else statements can be modified by introducing a new non-terminal for the optional else clause, such as `Stmt -> if Expr then Stmt OptElse | OtherStmt`, `OptElse -> else Stmt | epsilon`.
  - Resolving the ambiguity by using additional information, such as the precedence and associativity of the operators, or the convention of associating the else clause with the nearest if clause. For example, the LR parser can use these information to resolve the conflicts (shift/reduce or reduce/reduce) in the parsing table of ambiguous grammars.
  - Accepting the ambiguity and generating all possible parse trees for the same sentence, and then choosing the most appropriate one based on some criteria, such as the semantic analysis or the optimization phase of the compiler. This approach is more complex and less efficient than the previous ones.