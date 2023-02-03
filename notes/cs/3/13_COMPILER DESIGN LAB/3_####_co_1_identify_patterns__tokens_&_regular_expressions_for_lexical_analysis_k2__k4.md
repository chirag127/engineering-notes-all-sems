#### CO 1 Identify patterns, tokens & regular expressions for lexical analysis. K2, K4

CO 1:
- Lexical analysis is the process of breaking down input into its smallest meaningful units, called tokens.
- Tokens are sequences of characters with a specific meaning.
- Patterns are used to identify tokens in the input.
- Regular expressions are a way to describe patterns in a compact and expressive way.

K2:
- In lexical analysis, regular expressions are used to define patterns that match specific tokens.
- Tokens can include keywords, identifiers, literals, operators, and punctuation.
- The lexer uses the regular expressions to recognize these tokens from the input stream.

K4:
- Regular expressions can describe patterns such as sequences of characters, repetitions, alternations, and optional elements.
- The lexer uses a finite automaton to match the input against the regular expressions and produce the corresponding tokens.
- The lexer outputs a stream of tokens that can be processed by the next phase of the compiler or interpreter.
