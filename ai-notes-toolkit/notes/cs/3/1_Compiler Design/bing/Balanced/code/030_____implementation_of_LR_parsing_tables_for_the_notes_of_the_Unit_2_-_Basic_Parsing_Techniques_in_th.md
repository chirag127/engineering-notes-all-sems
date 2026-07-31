### Implementation of LR Parsing Tables

LR parsing tables are a two-dimensional array in which each entry represents an action or a goto entry. LR parsing tables are used to guide the LR parser in recognizing the input string and applying the appropriate production rules. LR parsing tables are constructed from the LR(0) items and the DFA of the grammar.

The LR parsing table has two parts: the action part and the goto part. The action part has columns for lookahead terminal symbols, and the goto part has columns for non-terminal symbols. The rows of the table correspond to the states of the DFA.

The action part of the table specifies what action the parser should take when it encounters a terminal symbol in the input buffer. There are three possible actions: shift, reduce, and accept.

- Shift: The parser shifts the terminal symbol from the input buffer to the top of the stack, and moves to the next state as indicated by the table entry.
- Reduce: The parser reduces the top symbols of the stack by applying a production rule, and pops the symbols from the stack. The parser then pushes the left-hand side of the production rule to the stack, and consults the goto part of the table to determine the next state.
- Accept: The parser accepts the input string as valid and terminates the parsing process.

The goto part of the table specifies what state the parser should move to after reducing a non-terminal symbol. The parser looks up the table entry based on the current state and the non-terminal symbol on the top of the stack.

The LR parsing table can be constructed by following these steps:

- Generate the LR(0) items and the DFA of the grammar.
- Label each state of the DFA with a unique number.
- For each state of the DFA, fill in the action part of the table as follows:
  - If the state contains an item of the form A -> α•aβ, where a is a terminal symbol, then set action[state, a] to shift s, where s is the state that can be reached by following the transition labeled a from the current state.
  - If the state contains an item of the form A -> α•, where A is not the start symbol, then set action[state, a] to reduce A -> α for all terminal symbols a in the follow set of A.
  - If the state contains an item of the form S' -> S•, where S is the start symbol, then set action[state, $] to accept, where $ is the end-of-input marker.
- For each state of the DFA, fill in the goto part of the table as follows:
  - If the state contains an item of the form A -> α•Bβ, where B is a non-terminal symbol, then set goto[state, B] to t, where t is the state that can be reached by following the transition labeled B from the current state.

Here is an example of an LR parsing table for the grammar:

S -> CC
C -> cC | d

| State | c | d | $ | S | C |
| ----- | - | - | - | - | - |
| 0     | s3 | s4 |   | 1 | 2 |
| 1     |    |    | acc |   |   |
| 2     | s3 | s4 | r1 |   | 5 |
| 3     | s3 | s4 | r3 |   | 6 |
| 4     |    |    | r4 |   |   |
| 5     |    |    | r1 |   |   |
| 6     |    |    | r2 |   |   |