### Two Stack Pushdown Automata

A two-stack pushdown automaton (2-PDA) is a variation of the pushdown automaton that has two stacks instead of one. It is a theoretical model of computation that is used to recognize context-free languages.

Here are some key points about 2-PDA:

1. A 2-PDA is a 7-tuple (Q, Σ, Γ, δ, q0, Z0, F) where:
    - Q is a finite set of states
    - Σ is the input alphabet
    - Γ is the stack alphabet
    - δ is the transition function
    - q0 is the initial state
    - Z0 is the initial stack symbol
    - F is the set of final states
2. The transition function δ takes the current state, the current input symbol, and the top symbols of both stacks, and returns a set of possible next states, along with the symbols to be pushed onto the stacks.
3. The computation of a 2-PDA proceeds in a similar manner to that of a standard pushdown automaton, with the difference being that the automaton has access to two stacks instead of one.
4. A 2-PDA can simulate a standard pushdown automaton by using one of its stacks and ignoring the other.
5. A 2-PDA can recognize a strictly larger set of languages than a standard pushdown automaton. In particular, it can recognize all context-free languages, as well as some non-context-free languages.
