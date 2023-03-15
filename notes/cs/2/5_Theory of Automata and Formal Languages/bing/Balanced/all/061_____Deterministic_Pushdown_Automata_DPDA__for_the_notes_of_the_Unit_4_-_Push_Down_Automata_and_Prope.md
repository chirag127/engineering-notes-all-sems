# Deterministic Pushdown Automata (DPDA)

- A deterministic pushdown automaton (DPDA) is a variation of the pushdown automaton (PDA) that accepts the deterministic context-free languages (DCFL), a proper subset of context-free languages (CFL) .
- A DPDA has a single computation from the initial configuration to an accepting one for all strings belonging to the language it accepts .
- A DPDA can be formally defined as a 6-tuple (Q, Σ, Γ, δ, q0, F), where :
  - Q is a finite set of states
  - Σ is a finite set of input symbols
  - Γ is a finite set of pushdown symbols (which can be pushed and popped from the stack)
  - δ is a transition function that maps Q × (Σ ∪ {ε}) × Γ to Q × Γ*
  - q0 is the initial state
  - F is a set of final states
- A DPDA is deterministic if for every state q, input symbol a, and stack symbol X, there is at most one transition of the form (q, a, X) → (p, γ) in δ .
- A DPDA can accept a string by two modes: final state and empty stack .
  - In the final state mode, a DPDA accepts a string if it reaches a final state after reading the entire input and possibly modifying the stack.
  - In the empty stack mode, a DPDA accepts a string if it empties the stack after reading the entire input and possibly changing the state.
- A DPDA can be converted to an equivalent context-free grammar (CFG) and vice versa .
- A DPDA can simulate a deterministic finite automaton (DFA) by using an empty stack, but not all CFLs can be accepted by a DPDA .
- A DPDA can be represented by a state diagram, where each transition is labeled by an input symbol, a stack symbol to be popped, and a stack symbol (or string) to be pushed . For example, the following state diagram shows a DPDA that accepts the language {a^n b^n | n ≥ 0} by empty stack :

![DPDA example](https://learningmonkey.in/wp-content/uploads/2020/04/DPDA-1.png)