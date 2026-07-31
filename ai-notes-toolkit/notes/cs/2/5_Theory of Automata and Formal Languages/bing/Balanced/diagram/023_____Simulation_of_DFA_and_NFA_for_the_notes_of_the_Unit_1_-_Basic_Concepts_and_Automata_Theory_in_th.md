### Simulation of DFA and NFA

- A deterministic finite automaton (DFA) is a finite state machine that accepts or rejects a given string of symbols, by running through a state sequence uniquely determined by the string.
- A non-deterministic finite automaton (NFA) is a finite state machine that may have multiple possible transitions for a given symbol and state.
- Both DFA and NFA can be used to recognize the same set of regular languages, but they may differ in the number of states and transitions.
- To simulate a DFA, we can use a single variable to store the current state, and update it according to the transition function for each input symbol. If the final state is an accepting state, we accept the input; otherwise, we reject it.
- To simulate an NFA, we can use a set of variables to store the current states, and update them according to the transition function for each input symbol. We also need to consider the epsilon transitions, which are transitions that do not consume any input symbol. If any of the final states is an accepting state, we accept the input; otherwise, we reject it.
- Alternatively, we can convert an NFA to an equivalent DFA using the subset construction algorithm, which creates a new state for each subset of states in the NFA. The new transition function maps each subset and symbol to the union of the subsets reachable by that symbol from the original NFA. The new accepting states are the subsets that contain at least one accepting state from the original NFA .
- The following diagram illustrates the simulation of a DFA and an NFA for the input string `ab`:

```
DFA:                         NFA:

    a     b                     a     b
--> (q0) -> (q1) -> (q2)    --> (q0) -> (q1) -> (q2)
               |                    |  /  |  /
               V                    V /   V /
              (q3)                 (q3)  (q4)

Current state: q0            Current states: {q0}
Input symbol: a              Input symbol: a
Next state: q1               Next states: {q1, q3}
Current state: q1            Current states: {q1, q3}
Input symbol: b              Input symbol: b
Next state: q2               Next states: {q2, q4}
Current state: q2            Current states: {q2, q4}
Input symbol: none           Input symbol: none
Final state: q2              Final states: {q2, q4}
Output: accept               Output: accept
```