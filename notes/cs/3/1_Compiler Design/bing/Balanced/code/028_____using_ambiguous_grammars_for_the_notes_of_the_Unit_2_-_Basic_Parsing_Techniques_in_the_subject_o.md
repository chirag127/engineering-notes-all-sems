### Using ambiguous grammars for the notes of the Unit 2 - Basic Parsing Techniques in the subject of Compiler Design

- An ambiguous grammar is a grammar that can generate more than one parse tree (or leftmost/rightmost derivation) for the same input string .
- Ambiguous grammars are undesirable for programming languages because they can lead to different interpretations and meanings of the same program.
- Ambiguous grammars can cause conflicts in parsing methods such as top-down or bottom-up parsing. Conflicts occur when there is more than one possible action for a given input symbol and parser state.
- Some common sources of ambiguity in grammars are:
  - Dangling else problem: The else clause can be associated with either the nearest or the farthest if statement.
  - Operator precedence and associativity: The order of evaluation of operators can be unclear without parentheses or explicit rules.
  - Left recursion: A production rule has the same non-terminal symbol on both sides, such as A -> Aa.
- Some possible ways to handle or remove ambiguity in grammars are:
  - Rewrite the grammar to eliminate the ambiguity . For example, use different non-terminals for different levels of precedence, or use parentheses to group expressions.
  - Use precedence and associativity rules to resolve conflicts in the parsing table. For example, give higher precedence to * than +, or use left associativity for + and *.
  - Use a parser that can handle ambiguity, such as Earley parser or GLR parser. These parsers can generate multiple parse trees or a single parse forest for an ambiguous input.