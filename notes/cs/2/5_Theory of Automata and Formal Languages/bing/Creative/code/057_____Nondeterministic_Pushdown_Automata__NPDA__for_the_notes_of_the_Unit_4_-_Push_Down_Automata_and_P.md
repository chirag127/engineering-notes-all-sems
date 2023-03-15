### Nondeterministic Pushdown Automata (NPDA)

- A nondeterministic pushdown automaton (NPDA) is a variation of a nondeterministic finite automaton (NFA) that has access to a stack, which is a data structure that allows adding and removing elements from one end only .
- A stack can store an unbounded amount of information, which gives NPDA more power than NFA.
- A NPDA can be formally defined as a 7-tuple (Q, Σ, Γ, δ, q0, Z0, F), where :
  - Q is a finite set of states
  - Σ is an input alphabet
  - Γ is a stack alphabet
  - δ is a transition function that maps Q × Σε × Γε to a finite subset of Q × Γε, where ε denotes the empty string
  - q0 is the initial state
  - Z0 is the initial stack symbol
  - F is a set of final states
- A NPDA can make transitions based on the current state, the input symbol, and the top of the stack. It can also push or pop symbols from the stack, or leave it unchanged.
- A NPDA accepts an input string if there exists a sequence of transitions that leads from the initial configuration to a final configuration, where the input string is consumed and the current state is in F.
- A NPDA can accept a language by final state or by empty stack. The two acceptance criteria are equivalent, meaning that for any NPDA that accepts by final state, there exists an equivalent NPDA that accepts by empty stack, and vice versa.
- A NPDA can generate a language that a deterministic PDA (DPDA) cannot generate, such as {a^n b^n c^n | n ≥ 0}, which is not context-free. Therefore, NPDA is more expressive than DPDA.