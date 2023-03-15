### Using ambiguous grammars for the notes of the Unit 2 - Basic Parsing Techniques in the subject of Compiler Design

- A grammar is a set of rules that define the syntax of a language, i.e., how the symbols of the language can be combined to form valid sentences.
- A grammar is ambiguous if it can generate more than one parse tree (or leftmost/rightmost derivation) for the same sentence, i.e., if the sentence has more than one possible interpretation according to the grammar rules.
- Ambiguous grammars are undesirable for compiler design because they can cause conflicts in the parsing process and lead to different meanings for the same program.
- Some examples of ambiguous grammars are:

  - The grammar for arithmetic expressions with + and * operators, where both operators have the same precedence and associativity. For example, the sentence `a+b*c` can be parsed as `(a+b)*c` or `a+(b*c)`.
  - The grammar for if-then-else statements, where the else clause can be associated with the nearest or the farthest if statement. For example, the sentence `if a then if b then c else d` can be parsed as `if a then (if b then c else d)` or `if a then (if b then c) else d`.
  - The grammar for dangling else problem, where the else clause can be associated with any unmatched if statement. For example, the sentence `if a then if b then c; else d;` can be parsed as `if a then (if b then c; else d;)` or `if a then (if b then c;); else d;`.

- To handle ambiguous grammars, we can use one of the following methods:

  - Modify the grammar to make it unambiguous, i.e., to ensure that each sentence has a unique parse tree. For example, we can introduce parentheses to disambiguate arithmetic expressions, or use end-if markers to disambiguate if-then-else statements.
  - Use a parser that can resolve the ambiguity based on some rules, such as precedence and associativity of operators, or the nearest-else rule. For example, we can use an LR parser that can handle shift/reduce or reduce/reduce conflicts in the parsing table of ambiguous grammars.