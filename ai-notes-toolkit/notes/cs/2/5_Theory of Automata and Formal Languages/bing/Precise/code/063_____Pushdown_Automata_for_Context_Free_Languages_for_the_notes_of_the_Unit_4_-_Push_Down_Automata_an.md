### Pushdown Automata for Context Free Languages

A pushdown automaton (PDA) is a type of automaton that is used to recognize context-free languages. It is similar to a finite automaton, but with the addition of a stack, which provides additional memory.

Here are some key points to remember about pushdown automata:

1. A PDA is defined by a 7-tuple (Q, Σ, Γ, δ, q0, Z, F) where:
    - Q is a finite set of states
    - Σ is the input alphabet
    - Γ is the stack alphabet
    - δ is the transition function
    - q0 is the initial state
    - Z is the initial stack symbol
    - F is the set of final states
2. The transition function δ takes a state, an input symbol, and a stack symbol as arguments and returns a set of state-stack symbol pairs.
3. A PDA can be either deterministic or nondeterministic.
4. A PDA can be used to recognize a context-free language by either final state or empty stack acceptance.
5. The language recognized by a PDA is the set of all strings that can be accepted by the PDA.
