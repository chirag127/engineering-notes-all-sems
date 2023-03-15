### Nondeterministic Pushdown Automata (NPDA)

- A nondeterministic pushdown automaton (NPDA) is a variation of the nondeterministic finite automaton (NDFA) that has an additional component called a stack  .
- A stack is a data structure that allows only two operations: push and pop. Push adds a symbol to the top of the stack, and pop removes the symbol from the top of the stack  .
- A NPDA can use the stack to store and retrieve information during the computation. The stack can have unlimited size, unlike the finite memory of a NDFA  .
- A NPDA is formally defined by a 7-tuple (Q, Σ, Γ, δ, q0, Z0, F), where :
  - Q is a finite set of states
  - Σ is an input alphabet
  - Γ is a stack alphabet
  - δ is a transition function that maps Q × Σε × Γε to a finite subset of Q × Γε, where ε denotes the empty string
  - q0 is the initial state
  - Z0 is the initial stack symbol
  - F is a set of final or accepting states
- A NPDA can make transitions based on the current state, the input symbol, and the stack symbol. It can also change the state and the stack symbol in the process .
- A NPDA can have multiple possible transitions from a given configuration, or no transitions at all. It can also make ε-transitions, which do not consume any input symbol .
- A NPDA accepts an input string if there exists a sequence of transitions that leads to a final state and consumes the entire input string. The stack can be empty or nonempty at the end of the computation .
- A NPDA can recognize a class of languages called context-free languages, which are more expressive than regular languages. However, not all context-free languages are deterministic, meaning that there may not exist a deterministic pushdown automaton (DPDA) that can recognize them  .