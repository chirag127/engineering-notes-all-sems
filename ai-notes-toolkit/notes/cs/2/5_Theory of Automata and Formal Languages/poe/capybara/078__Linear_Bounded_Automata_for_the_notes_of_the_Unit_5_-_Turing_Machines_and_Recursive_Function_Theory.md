### Linear Bounded Automata

Linear Bounded Automata (LBA) is a type of Turing Machine that has a restricted tape length. The tape of LBA is bounded by a constant function of the input size. Here are some important points to understand LBA:

- LBA is a variation of Turing Machine that accepts context-sensitive languages. 
- The difference between a Turing Machine and an LBA is that an LBA has a tape of limited length. 
- The length of the tape in an LBA is proportional to the length of the input. In other words, the length of the tape is a function of the input size. 
- LBA can be represented as a 7-tuple (Q, Σ, Γ, δ, q0, B, F), where Q is the set of states, Σ is the input alphabet, Γ is the tape alphabet, δ is the transition function, q0 is the initial state, B is the blank symbol, and F is the set of final states.
- The transition function of LBA is defined as δ : Q × Γ → Q × Γ × {L, R}, where L and R represent the direction of the tape head movement.
- LBA can be simulated by a deterministic Turing Machine in polynomial time. 
- LBA can also be used to recognize non-context-free languages, which cannot be recognized by a pushdown automaton. 

In conclusion, LBA is a restricted version of the Turing Machine that has a bounded tape length. It allows us to recognize context-sensitive languages and can also be used to recognize non-context-free languages.