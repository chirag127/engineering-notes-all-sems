# Nondeterministic Pushdown Automata (NPDA)

- A nondeterministic pushdown automaton (NPDA) is a variation of the nondeterministic finite automaton (NDFA) that has access to a stack (hence the name pushdown)   .
- A stack is a data structure that allows only two operations: push (adding an element to the top) and pop (removing an element from the top).
- A NPDA can use the stack to store and retrieve information during the computation, which gives it more power than a NDFA.
- A NPDA is formally defined by a 7-tuple (Q, Σ, Γ, δ, q0, Z0, F), where  :
  - Q is a finite set of states
  - Σ is an input alphabet
  - Γ is a stack alphabet
  - δ is a transition function that maps Q x (Σ ∪ {ε}) x (Γ ∪ {ε}) to a finite subset of Q x (Γ ∪ {ε})
  - q0 is the initial state
  - Z0 is the initial stack symbol
  - F is a set of final states
- A NPDA can make transitions based on the current state, the input symbol, and the top of the stack. It can also change the state and the stack by popping and pushing symbols.
- A NPDA can have multiple possible transitions from a given configuration, or no transitions at all. Any of these transitions can be chosen in a computation. A NPDA accepts an input if there exists a computation that leads to a final state.
- The class of languages accepted by NPDA is called the context-free languages (CFL), which is a proper superset of the regular languages. A CFL can also be defined by a context-free grammar (CFG). There is an algorithm to convert a CFG to a NPDA and vice versa.