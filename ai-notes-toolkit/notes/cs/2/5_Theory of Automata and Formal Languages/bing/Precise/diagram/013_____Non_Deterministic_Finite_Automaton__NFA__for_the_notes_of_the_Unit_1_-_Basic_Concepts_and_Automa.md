### Non Deterministic Finite Automaton (NFA)

- A Non-Deterministic Finite Automaton (NFA) is a type of finite automaton that allows multiple transitions from a single state for the same input symbol.
- Unlike a Deterministic Finite Automaton (DFA), an NFA can have multiple possible next states for a given state and input symbol.
- An NFA can also have transitions that do not consume any input symbols, known as epsilon (ε) transitions.
- An NFA can be represented using a state transition diagram or a state transition table.
- The formal definition of an NFA is a 5-tuple (Q, Σ, δ, q0, F) where:
  - Q is a finite set of states.
  - Σ is a finite set of input symbols.
  - δ is the transition function, which maps a state and an input symbol to a set of next states.
  - q0 is the initial state.
  - F is the set of final or accepting states.
- The language accepted by an NFA is the set of all strings that can be processed by the NFA, starting from the initial state, and ending in an accepting state.
- An NFA can be converted to an equivalent DFA using the powerset construction method.
- The powerset construction method involves creating a new DFA state for each possible subset of NFA states, and defining the transitions between these new DFA states based on the transitions of the NFA states.
- The time complexity of the powerset construction method is exponential in the number of states of the NFA, making it impractical for large NFAs.
- However, for many practical applications, the number of states in the resulting DFA is much smaller than the worst-case bound, making the conversion from NFA to DFA feasible.