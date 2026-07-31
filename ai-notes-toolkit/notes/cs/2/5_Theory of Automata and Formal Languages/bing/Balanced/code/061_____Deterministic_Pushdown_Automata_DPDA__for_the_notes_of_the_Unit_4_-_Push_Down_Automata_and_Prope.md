# Deterministic Pushdown Automata (DPDA)

- A deterministic pushdown automaton (DPDA) is a variation of the pushdown automaton (PDA) that accepts the deterministic context-free languages (DCFL), a proper subset of context-free languages (CFL).
- A DPDA has a single computation from the initial configuration until an accepting one for all strings belonging to the language it accepts.
- A DPDA can be formally defined as a 7-tuple (Q, Σ, Γ, δ, q0, Z, F), where
  - Q is a finite set of states
  - Σ is a finite set of input symbols
  - Γ is a finite set of pushdown symbols (stack symbols)
  - δ is a transition function that maps Q × (Σ ∪ {ε}) × Γ to Q × Γ*
  - q0 is the initial state
  - Z is the initial pushdown symbol
  - F is a set of final states
- A DPDA differs from a PDA in that the transition function δ is a partial function, meaning that it is not defined for some combinations of state, input symbol, and stack symbol. This ensures that there is at most one possible move for any configuration of the DPDA.
- A DPDA can accept a string by two modes: final state and empty stack. In the final state mode, the DPDA accepts a string if it reaches a final state after reading the whole input. In the empty stack mode, the DPDA accepts a string if it empties the stack after reading the whole input. These two modes are equivalent, meaning that for any DPDA that accepts by one mode, there is an equivalent DPDA that accepts by the other mode.
- A DPDA can recognize a DCFL, but not all CFLs. For example, the language {a^n b^n c^n | n ≥ 0} is a CFL, but not a DCFL, because it cannot be recognized by a DPDA. This is because a DPDA cannot keep track of three levels of nesting using only one stack.