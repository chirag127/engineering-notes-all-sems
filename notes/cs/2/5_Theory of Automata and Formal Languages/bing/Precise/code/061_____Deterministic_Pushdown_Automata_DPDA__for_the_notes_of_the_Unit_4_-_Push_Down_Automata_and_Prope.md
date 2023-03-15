### Deterministic Pushdown Automata (DPDA)

A deterministic pushdown automaton (DPDA) is a variation of the pushdown automaton (PDA) that is more restrictive in its definition. A DPDA is defined as a 6-tuple (Q, Σ, Γ, δ, q0, F) where:

1. Q is a finite set of states.
2. Σ is a finite input alphabet.
3. Γ is a finite stack alphabet.
4. δ is a transition function: δ: Q × (Σ ∪ {ε}) × Γ → Q × Γ*.
5. q0 ∈ Q is the initial state.
6. F ⊆ Q is the set of accepting states.

The main difference between a DPDA and a PDA is that the transition function of a DPDA is deterministic. This means that for any given state, input symbol, and stack symbol, there is at most one transition defined. In contrast, a PDA can have multiple transitions defined for the same state, input symbol, and stack symbol.

A DPDA can be used to recognize context-free languages, but not all context-free languages can be recognized by a DPDA. A language is said to be deterministic context-free if it can be recognized by a DPDA.

Some properties of deterministic context-free languages include:

1. The class of deterministic context-free languages is closed under intersection with regular languages.
2. The class of deterministic context-free languages is not closed under union, concatenation, or Kleene star.
3. The class of deterministic context-free languages is a proper subset of the class of context-free languages.