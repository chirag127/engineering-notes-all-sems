### NFA with ε-Transition

- An NFA with ε-transition is a type of nondeterministic finite automaton (NFA) that allows the machine to change its state without consuming any input symbol. Such transitions are labeled with ε in the state diagram .
- Formally, an NFA with ε-transition is a 5-tuple (Q, Σ, δ, q0, F), where:
  - Q is a finite set of states
  - Σ is a finite set of input symbols
  - δ: Q × (Σ ∪ {ε}) → P(Q) is the transition function, where P(Q) is the power set of Q
  - q0 ∈ Q is the initial state
  - F ⊆ Q is the set of final or accepting states
- The transition function δ can be extended to δ*: P(Q) × Σ* → P(Q) as follows:
  - δ*(R, ε) = ε-closure(R) for any R ⊆ Q, where ε-closure(R) is the set of states reachable from R by following only ε-transitions
  - δ*(R, aw) = δ*(δ*(R, a), w) for any R ⊆ Q, a ∈ Σ, and w ∈ Σ*, where δ*(R, a) = ε-closure(∪q∈Rδ(q, a))
- The language accepted by an NFA with ε-transition is L(N) = {w ∈ Σ* | δ*(q0, w) ∩ F ≠ ∅}, i.e., the set of strings that lead to at least one accepting state from the initial state.
- An NFA with ε-transition can be converted to an equivalent NFA without ε-transition by applying the following steps:
  - For each state q ∈ Q, compute ε-closure(q) and mark it on the state diagram
  - For each state q ∈ Q and each input symbol a ∈ Σ, compute δ*(q, a) by following all possible ε-transitions from q and then taking a transition on a. Add a new transition from q to δ*(q, a) on a and remove all ε-transitions from q.
  - For each state q ∈ Q, if ε-closure(q) contains an accepting state, then make q an accepting state as well.
  - The resulting NFA without ε-transition will have the same set of states, input symbols, initial state, and transition function as the original NFA with ε-transition, but the set of accepting states and the state diagram may be different.