### Deterministic Pushdown Automata (DPDA)

- A deterministic pushdown automaton (DPDA) is a variation of the pushdown automaton (PDA) that accepts the deterministic context-free languages (DCFL), a proper subset of context-free languages (CFL).
- A DPDA has a single computation from the initial configuration until an accepting one for all strings belonging to the language it accepts.
- A DPDA is defined by a 7-tuple (Q, Σ, Γ, δ, q0, Z0, F) where
  - Q is a finite set of states
  - Σ is a finite set of input symbols
  - Γ is a finite set of stack symbols
  - δ is a transition function that maps Q × (Σ ∪ {ε}) × Γ to Q × Γ*
  - q0 is the initial state
  - Z0 is the initial stack symbol
  - F is a set of final states
- A DPDA is deterministic if for every state q, input symbol a, and stack symbol X, there is at most one transition of the form (q, a, X) → (p, α) in δ.
- A DPDA can accept a string by two modes: final state and empty stack.
  - In the final state mode, a DPDA accepts a string if it reaches a final state after reading the whole input and the stack may or may not be empty.
  - In the empty stack mode, a DPDA accepts a string if it empties the stack after reading the whole input and the state may or may not be final.
- A DPDA can be represented by a state diagram, where the transitions are labeled by a, X/α, meaning that the DPDA reads an input symbol a, pops a stack symbol X, and pushes a string α.
- A DPDA can be converted to an equivalent context-free grammar (CFG) and vice versa.
- A DPDA can simulate a deterministic finite automaton (DFA) by using an empty stack, but it cannot simulate a nondeterministic finite automaton (NFA) or a nondeterministic pushdown automaton (NPDA).
- A DPDA is less powerful than a NPDA, as there are some CFLs that are not DCFLs, such as {a^n b^n c^n | n ≥ 0} and {w w^R | w ∈ {a, b}*}.