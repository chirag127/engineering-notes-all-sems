### Context Free Grammars for Pushdown Automata

- A **context-free grammar (CFG)** is a formal grammar in which every production rule is of the form `V → w`, where `V` is a single nonterminal symbol, and `w` is a string of terminals and/or nonterminals.
- A **pushdown automaton (PDA)** is a type of automaton that employs a stack to process context-free languages.
- A PDA can be formally defined as a 7-tuple `(Q, Σ, Γ, δ, q0, Z, F)` where:
  - `Q` is a finite set of states
  - `Σ` is a finite set of input symbols
  - `Γ` is a finite set of stack symbols
  - `δ` is a transition function: `δ: Q × (Σ ∪ {ε}) × Γ → P(Q × Γ*)`
  - `q0` is the initial state
  - `Z` is the initial stack symbol
  - `F` is the set of accepting states
- A PDA can be used to recognize context-free languages by reading the input string and using the stack to keep track of the current state of the derivation.
- A context-free grammar can be converted into an equivalent PDA by constructing a PDA that simulates the leftmost derivation of the grammar.
- The construction of a PDA from a CFG involves creating a state for each production rule in the grammar, and transitions that correspond to the application of the production rules.
- The PDA pushes the right-hand side of the production rule onto the stack, and pops the left-hand side of the production rule from the stack.
- The PDA accepts the input string if it reaches an accepting state with an empty stack.
