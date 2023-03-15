# Nondeterministic Pushdown Automata (NPDA)

- A nondeterministic pushdown automaton (NPDA), or just pushdown automaton (PDA), is a variation of the nondeterministic finite automaton (NFA) that can use a stack as an auxiliary memory  .
- A stack is a data structure that allows only two operations: push (adding an element to the top) and pop (removing an element from the top).
- A NPDA can push and pop symbols from the stack during the transitions, and use the top symbol of the stack as an additional input.
- A NPDA can also make nondeterministic choices, meaning that it can have multiple possible transitions from a given configuration (state, input, and stack).
- A NPDA is formally defined by a 7-tuple (Q, Σ, Γ, δ, q0, Z0, F), where :
  - Q is a finite set of states
  - Σ is a finite input alphabet
  - Γ is a finite stack alphabet
  - δ is a transition function that maps Q × (Σ ∪ {ε}) × (Γ ∪ {ε}) to a finite subset of Q × (Γ ∪ {ε})
  - q0 is the initial state
  - Z0 is the initial stack symbol
  - F is a set of final or accepting states
- A NPDA accepts an input string w if there exists a sequence of transitions that leads from the initial configuration (q0, w, Z0) to a final configuration (qf, ε, α), where qf ∈ F and α ∈ Γ*.
- The language accepted by a NPDA is called a context-free language (CFL), and it is a proper subset of the recursively enumerable languages (REL).
- A NPDA can be represented by a state diagram, where each transition is labeled by an input symbol, a stack symbol to be popped, and a stack symbol to be pushed (separated by commas).
- A NPDA can also be simulated by a nondeterministic Turing machine (NTM) with a single tape, where the left end of the tape is used as the stack and the right end of the tape is used as the input.