### Two stack Pushdown Automata

A two-stack pushdown automaton (2-PDA) is a variation of the pushdown automaton that has two stacks instead of one. It is a theoretical model of computation that is used to recognize context-free languages.

A 2-PDA is defined by a 7-tuple (Q, Σ, Γ, δ, q0, Z0, F) where:
- Q is a finite set of states
- Σ is the input alphabet
- Γ is the stack alphabet
- δ is the transition function
- q0 is the initial state
- Z0 is the initial stack symbol
- F is the set of final states

The transition function δ is defined as δ: Q × (Σ ∪ {ε}) × Γ × Γ → P(Q × Γ × Γ × {L, R, S} × {L, R, S}), where L, R, and S represent the operations of moving the input head left, right, or staying in place, respectively.

In a 2-PDA, the transition from one configuration to another is determined by the current state, the current input symbol, and the top symbols of both stacks. The transition function specifies the new state, the symbols to be pushed onto the stacks, and the direction in which the input head should move.

A 2-PDA accepts an input string if, starting from the initial configuration, it reaches a configuration where the input string has been completely read and the current state is a final state.

It can be shown that 2-PDAs are strictly more powerful than pushdown automata with a single stack, and that they are equivalent in computational power to Turing machines. This means that 2-PDAs can recognize a larger class of languages than pushdown automata with a single stack, including some non-context-free languages.