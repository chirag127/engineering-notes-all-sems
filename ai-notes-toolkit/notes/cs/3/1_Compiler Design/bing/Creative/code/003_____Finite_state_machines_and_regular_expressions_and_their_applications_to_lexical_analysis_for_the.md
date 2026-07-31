### Finite state machines and regular expressions and their applications to lexical analysis

- Finite state machines (FSMs) are abstract models of computation that can process a sequence of inputs and change their state accordingly.
- Regular expressions (REs) are algebraic notations that can describe a set of strings that belong to a regular language.
- Lexical analysis is the process of scanning the source code of a program and converting it into a sequence of tokens that represent the lexical units of the language.
- Lexical analysis is an application of FSMs and REs, as they can be used to specify and recognize the tokens of a language.
- The steps involved in lexical analysis using FSMs and REs are:

  - Define the tokens of the language using REs. For example, an identifier can be defined as a letter followed by zero or more letters or digits: `[a-zA-Z][a-zA-Z0-9]*`.
  - Convert the REs into equivalent FSMs using algorithms such as Thompson's construction or Kleene's theorem. For example, the FSM for the identifier RE can be:

    ```
    q0 --[a-zA-Z]--> q1
    q1 --[a-zA-Z0-9]--> q1
    q1 --[other]--> q2
    ```

    where `q1` is the accepting state and `q2` is the error state.

  - Combine the FSMs for all the tokens into a single FSM using algorithms such as the subset construction or the union operation. For example, the FSM for the tokens `if`, `else`, `id`, and `num` can be:

    ```
    q0 --[i]--> q1 --[f]--> q2 --[other]--> q3
    q0 --[e]--> q4 --[l]--> q5 --[s]--> q6 --[e]--> q7 --[other]--> q3
    q0 --[a-zA-Z]--> q8 --[a-zA-Z0-9]--> q8 --[other]--> q3
    q0 --[0-9]--> q9 --[0-9]--> q9 --[other]--> q3
    q0 --[other]--> q10
    ```

    where `q2`, `q7`, `q8`, and `q9` are the accepting states for `if`, `else`, `id`, and `num` respectively, `q3` is the end-of-token state, and `q10` is the error state.

  - Implement the FSM using a data structure such as a transition table or a switch statement. For example, the transition table for the above FSM can be:

    | State | i | f | e | l | s | a-z | 0-9 | other |
    | ----- | - | - | - | - | - | --- | --- | ----- |
    | q0    | q1| q10|q4| q10|q10| q8 | q9 | q10   |
    | q1    | q10|q2| q10|q10|q10| q10| q10| q10   |
    | q2    | q10|q10|q10|q10|q10| q10| q10| q3    |
    | q3    | q1| q10|q4| q10|q10| q8 | q9 | q10   |
    | q4    | q10|q10|q10|q5| q10| q10| q10| q10   |
    | q5    | q10|q10|q10|q10|q6| q10| q10| q10   |
    | q6    | q10|q10|q10|q10|q10| q10| q10| q7    |
    | q7    | q10|q10|q10|q10|q10| q10| q10| q3    |
    | q8    | q8| q8| q8| q8| q8| q8 | q8 | q3    |
    | q9    | q10|q10|q10|q10|q10| q10| q9 | q3    |
    | q10   | q10|q10|q10|q10|q10| q10