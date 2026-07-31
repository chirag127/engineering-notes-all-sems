### Using ambiguous grammars for the notes of the Unit 2 - Basic Parsing Techniques in the subject of Compiler Design

- An ambiguous grammar is a grammar that can generate more than one leftmost derivation or more than one rightmost derivation for the same sentence .
- An ambiguous grammar can produce more than one parse tree for the same sentence, which implies more than one meaning or structure for the sentence.
- Ambiguous grammars are undesirable for programming languages, because they can cause confusion and ambiguity in the interpretation and execution of programs.
- Some examples of ambiguous grammars are:

  - The grammar for arithmetic expressions with + and * operators, without specifying the precedence and associativity of the operators  .
  - The grammar for if-then-else statements, without specifying the association of the else with the nearest or the farthest if .
  - The grammar for dangling else problem, which is a special case of the if-then-else ambiguity .

- Some methods to handle or remove ambiguity in grammars are:

  - Rewriting the grammar rules to eliminate the sources of ambiguity  .
  - Using precedence and associativity rules to resolve the conflicts in the parsing table of ambiguous grammars .
  - Using parentheses or brackets to explicitly indicate the grouping or nesting of expressions or statements .
  - Using unambiguous grammar constructs, such as if-then-elif-else or case statements, to avoid the dangling else problem .