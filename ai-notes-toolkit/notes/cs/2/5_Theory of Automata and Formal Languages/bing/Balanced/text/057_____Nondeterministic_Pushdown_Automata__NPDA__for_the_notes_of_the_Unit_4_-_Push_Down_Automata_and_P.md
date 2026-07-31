### Nondeterministic Pushdown Automata (NPDA)

- A nondeterministic pushdown automaton (NPDA) is a variation of the nondeterministic finite automaton (NDFA) that has an additional component called a stack .
- A stack is a data structure that allows only two operations: push and pop. Push adds a symbol to the top of the stack, and pop removes the symbol from the top of the stack .
- A NPDA can use the stack to store and retrieve information that is not available in the input or the state .
- A NPDA is formally defined by a 7-tuple (Q, Σ, Γ, δ, q0, Z0, F), where:
  - Q is a finite set of states
  - Σ is an input alphabet
  - Γ is a stack alphabet
  - δ is a transition function that maps Q × Σε × Γε to a finite subset of Q × Γε, where ε denotes the empty string
  - q0 is the initial state
  - Z0 is the initial stack symbol
  - F is a set of final or accepting states
- A NPDA can make a transition from one configuration to another by reading an input symbol, popping a stack symbol, and pushing zero or more stack symbols, according to the transition function  .
- A NPDA can also make ε-transitions, which do not consume any input symbol or stack symbol  .
- A NPDA accepts an input string if there exists a sequence of transitions that leads to a configuration where the input is exhausted and the state is in F  .
- A NPDA can be represented by a state diagram, where each transition is labeled by the input symbol, the stack symbol to be popped, and the stack symbols to be pushed, separated by commas  .
- A NPDA can recognize a class of languages called context-free languages, which are more expressive than regular languages   .
- A NPDA is more powerful than a deterministic pushdown automaton (DPDA), which can only make one transition for each configuration  .
- A NPDA can be converted to an equivalent context-free grammar, and vice versa, by using standard algorithms  .