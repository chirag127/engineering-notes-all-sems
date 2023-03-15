### Non Deterministic Finite Automaton (NFA)

A Non-Deterministic Finite Automaton (NFA) is a type of finite automaton that, unlike a Deterministic Finite Automaton (DFA), does not have a unique transition for each symbol of the alphabet for each state. In other words, an NFA can have multiple transitions for the same symbol from the same state, or even no transition at all.

Some key points to remember about NFA are:

1. An NFA can have multiple transitions for the same symbol from the same state.
2. An NFA can have no transition for a symbol from a state.
3. An NFA can have epsilon transitions, which allow the automaton to change states without consuming any input symbols.
4. The set of all strings accepted by an NFA is called the language recognized by the NFA.
5. Every NFA can be converted into an equivalent DFA.

An NFA is defined by a 5-tuple (Q, Σ, δ, q0, F) where:

- Q is a finite set of states.
- Σ is a finite set of input symbols (alphabet).
- δ is the transition function, which maps a state and an input symbol to a set of states.
- q0 is the initial state.
- F is the set of final (or accepting) states.

The transition function for an NFA is different from that of a DFA in that it returns a set of states instead of a single state. This allows for multiple transitions for the same symbol from the same state.
