
### Deterministic Finite Automaton (DFA)

1. A **Deterministic Finite Automaton (DFA)** is a finite state machine that accepts/rejects finite strings of symbols and only produces a unique computation (or run) of the machine for each input string.

2. A DFA consists of:
   * A finite set of states
   * A set of input symbols called the alphabet
   * A transition function that takes as argument a state and an input symbol and returns a state
   * A start state
   * A set of accept states

3. The transition function of a DFA is a mapping from a set of (state, input symbol) pairs to a state.

4. A DFA is said to accept an input string if a computation of the DFA ends in an accept state. Otherwise, the DFA is said to reject the string.

5. A DFA can be represented graphically as a directed graph, where the nodes represent the states, the edges represent the transitions, and the labels on the edges represent the input symbols that trigger the transitions.