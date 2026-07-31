### Simulation of DFA and NFA

- A **deterministic finite automaton (DFA)** is a finite state machine that accepts or rejects a given string of symbols, by running through a state sequence uniquely determined by the string.
- A **nondeterministic finite automaton (NFA)** is a finite state machine where, from each state, there can be more than one possible next state for a given input symbol.
- Both DFA and NFA can be used to recognize the same set of regular languages, but they may differ in the number of states and transitions.
- To simulate a DFA, we can use a single variable to store the current state, and update it according to the transition function for each input symbol. If the final state is an accepting state, we accept the input; otherwise, we reject it.
- To simulate an NFA, we can use a set of variables to store the current states, and update them according to the transition function for each input symbol. We also need to consider the epsilon transitions, which are transitions that do not consume any input symbol. If any of the final states is an accepting state, we accept the input; otherwise, we reject it .
- Alternatively, we can convert an NFA to an equivalent DFA using the subset construction algorithm, which creates a new state in the DFA for each subset of states in the NFA. Then, we can simulate the DFA as before.
- The advantage of simulating a DFA is that it is more efficient and deterministic, as it only needs to keep track of one state at a time.
- The advantage of simulating an NFA is that it is more expressive and compact, as it can have fewer states and transitions than the equivalent DFA. However, it may also have exponential blowup in the worst case.
- The following diagram shows an example of a DFA and an NFA that recognize the same language, which is the set of strings over {a, b} that end with ab.

![DFA and NFA example](https://jflap.org/tutorial/fa/createfa/images/dfa_nfa.png)