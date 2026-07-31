### NFA with ε-Transition

- A **non-deterministic finite automaton (NFA)** is a type of finite state machine that can have multiple possible transitions for a given input symbol and state. This means that the NFA can be in more than one state at a time.
- An **ε-transition** is a special kind of transition that allows the NFA to change its state without consuming any input symbol. This means that the NFA can move from one state to another without reading the input symbol.
- An **NFA with ε-transition** is an NFA that can have ε-transitions in addition to the regular transitions. In diagrams, such transitions are depicted by labeling the appropriate arcs with ε .
- An NFA with ε-transition is defined by a five-tuple {Q, q0, Σ, δ, F}, where:
  - Q is a finite set of states
  - q0 is the initial state
  - Σ is a finite set of input symbols
  - δ is a transition function that maps Q × (Σ ∪ {ε}) to P(Q), where P(Q) is the power set of Q
  - F is a set of final or accepting states
- An NFA with ε-transition accepts an input string if there is a sequence of transitions from the initial state to a final state that matches the input string, possibly with some ε-transitions in between .
- An example of an NFA with ε-transition that accepts the regular language L = (0+1)(00+11) is shown below:

![NFA with ε-transition example](https://web.cecs.pdx.edu/~sheard/course/CS311/Fall2013/ppt/NfaEpsilonDefined_files/image002.gif)

- The NFA with ε-transition can be converted to an equivalent NFA without ε-transition by using the following algorithm:
  - For each state q in Q, compute ε-closure(q), which is the set of states that can be reached from q by following only ε-transitions.
  - For each state q in Q and each symbol a in Σ, compute δ'(q, a), which is the union of ε-closure(r) for all r in δ(q, a).
  - Construct a new NFA without ε-transition with the same set of states Q, initial state q0, input symbols Σ, and final states F, but with the new transition function δ'.
  - The new NFA without ε-transition accepts the same language as the original NFA with ε-transition.