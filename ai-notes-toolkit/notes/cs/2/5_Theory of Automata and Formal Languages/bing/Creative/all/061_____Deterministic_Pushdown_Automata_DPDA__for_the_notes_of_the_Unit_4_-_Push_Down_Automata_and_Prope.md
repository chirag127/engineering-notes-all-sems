# Deterministic Pushdown Automata (DPDA)

- A deterministic pushdown automaton (DPDA) is a variation of the pushdown automaton (PDA) that accepts the deterministic context-free languages (DCFL), a proper subset of context-free languages (CFL) .
- A DPDA has a single computation from the initial configuration until an accepting one for all strings belonging to the language it accepts .
- A DPDA can be defined as a 7-tuple (Q, Σ, Γ, δ, q0, Z, F) where :
  - Q is the set of states
  - Σ is the set of input symbols
  - Γ is the set of pushdown symbols (which can be pushed and popped from the stack)
  - δ is the transition function that maps Q × (Σ ∪ {ε}) × Γ to Q × Γ*
  - q0 is the initial state
  - Z is the initial pushdown symbol (which is initially present in the stack)
  - F is the set of final states
- A DPDA is different from a PDA in that the transition function δ is a function and not a relation, meaning that for each state, input symbol and stack symbol, there is at most one possible transition .
- A DPDA can accept a language by two modes: final state and empty stack. In the final state mode, the DPDA accepts a string if it reaches a final state after reading the entire input. In the empty stack mode, the DPDA accepts a string if it empties the stack after reading the entire input .
- A DPDA can simulate a deterministic finite automaton (DFA) by using an empty stack and a single state. However, a DPDA cannot simulate a nondeterministic finite automaton (NFA) or a nondeterministic pushdown automaton (NPDA) in general, as there are some CFLs that are not DCFLs .
- Some examples of DCFLs that can be accepted by DPDAs are:
  - The language of balanced parentheses: {w ∈ { (, ) }* | w is well-formed}
  - The language of palindromes over a binary alphabet: {w ∈ {0, 1}* | w = wR}
  - The language of arithmetic expressions with matching parentheses: {w ∈ { (, ), +, -, *, /, a, b, c }* | w is a valid expression}