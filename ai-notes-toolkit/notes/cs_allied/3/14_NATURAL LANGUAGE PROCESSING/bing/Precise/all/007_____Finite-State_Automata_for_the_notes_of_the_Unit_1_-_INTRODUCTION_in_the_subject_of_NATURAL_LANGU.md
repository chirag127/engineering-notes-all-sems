# Finite-State Automata

Finite-state automata (FSA) are computational models used to recognize patterns within input taken from some character set (or alphabet). They are used in various fields, including natural language processing, to model and analyze the behavior of systems.

- An FSA is defined by a set of states, an input alphabet, a transition function, an initial state, and a set of final states.
- The transition function takes a state and an input symbol and returns a new state.
- The FSA starts in the initial state and reads the input symbols one by one, transitioning between states according to the transition function.
- If, after reading the entire input, the FSA is in one of the final states, the input is accepted; otherwise, it is rejected.
- There are two types of FSA: deterministic finite-state automata (DFA) and nondeterministic finite-state automata (NFA).
- In a DFA, for each state and input symbol, there is exactly one transition to a new state.
- In an NFA, for each state and input symbol, there can be multiple transitions to new states, or even no transition at all.
- NFAs can be converted to equivalent DFAs using the powerset construction.
- FSA can be used to recognize regular languages, which are defined by regular expressions.
- Regular expressions are a concise and powerful way to represent regular languages and can be used to specify search patterns in text processing.
