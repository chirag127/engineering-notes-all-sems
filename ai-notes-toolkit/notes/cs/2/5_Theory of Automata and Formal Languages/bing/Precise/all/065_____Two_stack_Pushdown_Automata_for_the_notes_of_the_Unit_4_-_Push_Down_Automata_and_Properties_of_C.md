### Two Stack Pushdown Automata

A two-stack pushdown automaton (2-PDA) is a variation of the pushdown automaton that has two stacks instead of one. It is a non-deterministic machine and is more powerful than a standard pushdown automaton.

The formal definition of a 2-PDA is a 7-tuple (Q, Σ, Γ, δ, q0, Z0, F) where:
- Q is a finite set of states
- Σ is the input alphabet
- Γ is the stack alphabet
- δ is the transition function: δ: Q × (Σ ∪ {ε}) × Γ × Γ → P(Q × Γ × Γ)
- q0 ∈ Q is the initial state
- Z0 ∈ Γ is the initial stack symbol
- F ⊆ Q is the set of accepting states

The computation of a 2-PDA is similar to that of a standard pushdown automaton, with the difference being that the transition function can manipulate two stacks instead of one. The transition function takes as input the current state, the current input symbol (or ε), and the top symbols of both stacks, and outputs a set of possible next states and the symbols to be pushed onto both stacks.

A 2-PDA accepts an input string if there exists a computation that ends in an accepting state with both stacks empty.

It is important to note that a 2-PDA is strictly more powerful than a standard pushdown automaton, as it can recognize a larger class of languages. In fact, it can be shown that a 2-PDA is equivalent in power to a Turing machine, meaning that it can recognize any language that is recognizable by a Turing machine.

In the context of the study of context-free languages, a 2-PDA can be used to prove properties of context-free languages and to provide algorithms for parsing context-free languages. For example, the Cocke-Younger-Kasami (CYK) algorithm for parsing context-free languages can be implemented using a 2-PDA.