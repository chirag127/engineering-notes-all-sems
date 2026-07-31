#### CO 1 Identify patterns, tokens & regular expressions for lexical analysis. K2, K4

- Lexical analysis is the process of converting a sequence of characters from a source program into a sequence of tokens that can be used by a compiler or interpreter.
- A token is a meaningful unit of text, such as a keyword, identifier, constant, operator, or delimiter.
- A pattern is a rule that describes how to form a token from a sequence of characters. For example, a pattern for an identifier may be a letter followed by zero or more letters or digits.
- A regular expression is a notation for specifying patterns using symbols and operators. For example, the regular expression `[a-zA-Z][a-zA-Z0-9]*` specifies the pattern for an identifier.
- A regular expression can be converted into a finite automaton, which is a machine that can recognize tokens by reading characters one by one and changing states accordingly.
- A finite automaton can be represented by a transition diagram, which is a graph that shows the states and the transitions between them. For example, the following transition diagram represents the finite automaton for the regular expression `[a-zA-Z][a-zA-Z0-9]*`.

![Transition diagram for identifier](https://i.imgur.com/8lQyQ9u.png)

- A finite automaton can also be represented by a transition table, which is a matrix that shows the next state for each state and input symbol. For example, the following transition table represents the same finite automaton as the transition diagram above.

| State | a-z | A-Z | 0-9 | Other |
|-------|-----|-----|-----|-------|
| 0     | 1   | 1   | -   | -     |
| 1     | 1   | 1   | 1   | -     |

- A lexical analyzer can be implemented by using a finite automaton to scan the input text and generate tokens. For example, the following pseudocode shows a lexical analyzer for the regular expression `[a-zA-Z][a-zA-Z0-9]*`.

```
function get_token()
  state = 0
  token = ""
  while true
    c = get_next_char()
    case state
      when 0
        if c is a letter
          state = 1
          token = token + c
        else
          return error
      when 1
        if c is a letter or a digit
          state = 1
          token = token + c
        else
          return token
```