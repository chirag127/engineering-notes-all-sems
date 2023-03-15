### 8. Develop an operator precedence parser for a given language.

- An operator precedence parser is a bottom-up parser that can handle a subset of context-free grammars, namely those that are operator grammars.
- An operator grammar is a grammar that has no epsilon productions, no unit productions, and no two adjacent non-terminals in the right-hand side of any production.
- An operator precedence parser uses a precedence table to determine the order of operations and resolve ambiguities in expressions involving operators.
- A precedence table is a matrix that specifies the relative precedence and associativity of each pair of operators in the grammar.
- The precedence table can be constructed from the grammar by using the following rules:
  - If `A -> α B β` is a production, where `B` is a terminal, then `B` has higher precedence than any terminal in `α` or `β`.
  - If `A -> α B` or `A -> B α` is a production, where `B` is a terminal, then `B` has the same precedence as the end-of-input marker `$`.
  - If `A -> α B C β` is a production, where `B` and `C` are terminals, then `B` and `C` have the same precedence and are associative.
- An operator precedence parser uses a stack and an input buffer to parse an input string. The stack initially contains the end-of-input marker `$`. The parser repeatedly performs one of the following actions:
  - If the top of the stack is `$` and the input buffer is empty, the parser accepts the input and terminates.
  - If the top of the stack is a non-terminal, the parser pops it and pushes the right-hand side of a production that has the non-terminal as the left-hand side.
  - If the top of the stack is a terminal and the input buffer is not empty, the parser compares the precedence of the terminal and the next input symbol using the precedence table. There are three possible cases:
    - If the terminal has lower precedence than the input symbol, the parser shifts the input symbol onto the stack and advances the input buffer.
    - If the terminal has higher precedence than the input symbol, the parser reduces the stack by popping the terminal and replacing it with a non-terminal that has a production with the terminal as the right-hand side.
    - If the terminal has the same precedence as the input symbol, the parser checks the associativity of the terminal. If the terminal is left-associative, the parser reduces the stack as in the previous case. If the terminal is right-associative, the parser shifts the input symbol as in the previous case. If the terminal is non-associative, the parser reports an error and terminates.
- An example of an operator grammar and its precedence table is given below:

```
E -> E + T | T
T -> T * F | F
F -> ( E ) | id
```

|   | + | * | ( | ) | id | $ |
|---|---|---|---|---|----|---|
| + | < | < | < | > | <  | > |
| * | > | < | < | > | <  | > |
| ( | < | < | < | = | <  |   |
| ) | > | > |   | > |    | > |
| id| > | > |   | > |    | > |
| $ | < | < | < |   | <  |   |

- An example of parsing the input string `id + id * id` using an operator precedence parser is shown below:

| Stack | Input | Action |
|-------|-------|--------|
| $     | id + id * id | Shift id |
| $ id  | + id * id    | Reduce F -> id |
| $ F   | + id * id    | Reduce T -> F |
| $ T   | + id * id    | Reduce E -> T |
| $ E   | + id * id    | Shift + |
| $ E + | id * id      | Shift id |
| $ E + id | * id      | Reduce F -> id |
| $ E + F | * id       | Reduce T -> F |
| $ E + T | * id       | Shift * |
| $ E + T * | id       | Shift id |
| $ E + T * id |       | Reduce F -> id |
| $ E + T * F |        | Reduce T -> T * F |
| $ E + T |            | Reduce E -> E + T |
| $ E |                | Accept |