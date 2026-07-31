# Simulation of DFA and NFA

- A **deterministic finite automaton (DFA)** is a finite state machine that accepts or rejects a given string of symbols, by running through a state sequence uniquely determined by the string.
- A **nondeterministic finite automaton (NFA)** is a finite state machine where, from each state, there can be more than one possible next state for a given input symbol, or no next state at all.
- Both DFA and NFA can be used to recognize the same set of regular languages, but they may differ in the number of states and transitions they require.
- To simulate a DFA, we need to keep track of the current state and the input string, and follow the transition function for each input symbol until we reach the end of the string or a state with no outgoing transition. Then we check if the final state is an accepting state or not.
- To simulate an NFA, we need to keep track of all the possible current states and the input string, and follow all the possible transitions for each input symbol until we reach the end of the string or no more transitions are possible. Then we check if any of the final states is an accepting state or not.
- To convert an NFA to an equivalent DFA, we can use the **subset construction** algorithm, which creates a new state in the DFA for each subset of states in the NFA, and defines the transition function based on the union of the transitions of the NFA states in each subset.
- To convert a DFA to an equivalent NFA, we can simply copy the states, transitions, and accepting states of the DFA, since every DFA is also an NFA.