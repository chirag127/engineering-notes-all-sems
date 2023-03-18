### Non Deterministic Finite Automaton (NFA)

Non-Deterministic Finite Automaton (NFA) is a mathematical model used to recognize formal languages. It is a type of Finite Automata that accepts or rejects a string of symbols based on a set of rules. NFA is used in many applications such as compilers, natural language processing, and pattern recognition.

#### Definition

A Non-Deterministic Finite Automaton (NFA) is a 5-tuple (Q, Σ, δ, q0, F) where:

- Q is a finite set of states.
- Σ is a finite set of symbols called the alphabet.
- δ is a transition function that maps Q × Σ to a set of states.
- q0 is the initial state.
- F is a set of final states.

#### Working

NFA works by reading a string of symbols from its input alphabet and transitioning from one state to another based on the transition function δ. If the NFA reaches a final state after reading the entire input string, it accepts the string. Otherwise, it rejects the string.

#### Differences between NFA and DFA

- NFA can have multiple transitions for a given state and input symbol, while DFA has only one transition for each state and input symbol.
- NFA can have epsilon transitions, where it can transition from one state to another without consuming any input symbol, while DFA cannot have epsilon transitions.

#### Example

Consider the NFA (Q, Σ, δ, q0, F) where:

- Q = {q0, q1, q2}
- Σ = {0, 1}
- δ(q0, 0) = {q0, q1}
- δ(q0, 1) = {q0}
- δ(q1, 1) = {q2}
- F = {q2}

The NFA accepts the string "011" by transitioning from q0 to q1 after reading the symbol 0, staying in q1 after reading the symbol 1, and transitioning to q2 after reading the symbol 1 again. Since q2 is a final state, the NFA accepts the string "011".