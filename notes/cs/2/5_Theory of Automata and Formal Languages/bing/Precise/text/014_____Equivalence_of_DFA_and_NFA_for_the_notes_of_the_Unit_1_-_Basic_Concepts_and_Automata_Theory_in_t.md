### Equivalence of DFA and NFA

1. A **DFA** (Deterministic Finite Automaton) is a finite state machine where, for each state, there is exactly one transition for each symbol of the alphabet.
2. An **NFA** (Nondeterministic Finite Automaton) is a finite state machine where, for each state, there can be zero, one, or more transitions for each symbol of the alphabet.
3. Both DFAs and NFAs are used to recognize regular languages.
4. Every NFA can be converted into an equivalent DFA using the **subset construction** algorithm.
5. The subset construction algorithm constructs a DFA that simulates the behavior of the NFA by keeping track of all possible states the NFA can be in after reading a given input.
6. The resulting DFA has a state for each subset of the states of the NFA, and transitions are defined based on the transitions of the NFA.
7. The resulting DFA recognizes the same language as the NFA.
8. Therefore, DFAs and NFAs are equivalent in their expressive power, meaning that they can recognize the same set of languages.
