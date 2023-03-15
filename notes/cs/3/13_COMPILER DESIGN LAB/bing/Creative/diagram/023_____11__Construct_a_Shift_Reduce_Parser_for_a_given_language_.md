### 11. Construct a Shift Reduce Parser for a given language.

A shift reduce parser is a type of bottom-up parser that uses a stack and an input buffer to parse a given string of symbols. The parser performs two types of actions: shift and reduce.

- A shift action moves the next symbol from the input buffer to the top of the stack.
- A reduce action applies a production rule to match a string of symbols at the top of the stack and replaces them with the left-hand side of the rule.

The parser follows a parsing table that specifies which action to take for each state of the stack and input buffer. The parsing table is constructed from the grammar of the language using an algorithm such as LR(0), SLR(1), LR(1), or LALR(1).

The parser starts with an empty stack and the entire input string in the buffer. It repeats the following steps until either the input is accepted or an error is detected:

- If the parsing table indicates a shift action for the current state, the parser performs a shift and updates the state.
- If the parsing table indicates a reduce action for the current state, the parser performs a reduce and updates the state.
- If the parsing table indicates an accept action for the current state, the parser accepts the input and terminates.
- If the parsing table indicates an error for the current state, the parser reports an error and terminates.

An example of a shift reduce parser for the language L = {a^n b^n | n >= 1} with the grammar G = {S -> aSb | ab} is shown below:

| Stack | Input | Action |
| ----- | ----- | ------ |
| $     | aabb$ | Shift  |
| $a    | abb$  | Shift  |
| $aa   | bb$   | Shift  |
| $aab  | b$    | Reduce by S -> aSb |
| $aS   | b$    | Shift  |
| $aSb  | $     | Reduce by S -> aSb |
| $S    | $     | Accept |