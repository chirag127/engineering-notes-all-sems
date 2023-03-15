#### CO 1 Identify patterns, tokens & regular expressions for lexical analysis. K2, K4

- Lexical analysis is the process of converting a sequence of characters (such as in a program or a document) into a sequence of tokens (strings with an assigned and thus identified meaning).
- A token is a pair consisting of a token name and an optional token value. For example, in the statement `int x = 10;`, the tokens are: `int` (keyword), `x` (identifier), `=` (operator), `10` (integer literal), `;` (punctuation).
- A pattern is a description of the form that the lexemes of a token may take. For example, the pattern for an identifier may be a letter followed by zero or more letters or digits, and the pattern for an integer literal may be one or more digits.
- A regular expression is a notation for specifying patterns using predefined symbols and operators. For example, the regular expression `[a-zA-Z][a-zA-Z0-9]*` specifies the pattern for an identifier, and the regular expression `[0-9]+` specifies the pattern for an integer literal.
- A regular expression can be converted into a finite automaton, which is a machine that can recognize the tokens that match the pattern. A finite automaton consists of a set of states, a set of input symbols, a transition function that maps a state and an input symbol to a new state, a start state, and a set of final states. For example, the following finite automaton can recognize identifiers:

![Finite automaton for identifiers](https://i.imgur.com/8xX9X6U.png)

- A lexical analyzer is a program that implements a finite automaton to scan the input and produce the tokens. A lexical analyzer can be written manually or generated automatically using a tool such as Lex or Flex.