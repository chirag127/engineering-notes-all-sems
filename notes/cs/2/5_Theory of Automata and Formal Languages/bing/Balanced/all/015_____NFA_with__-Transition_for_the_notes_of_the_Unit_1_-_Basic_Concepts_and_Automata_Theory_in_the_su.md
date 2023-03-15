# NFA with ε-Transition

- An NFA with ε-transition is a type of non-deterministic finite automaton (NFA) that allows transitions from one state to another without consuming any input symbol. These transitions are labeled with ε, which denotes the empty string.
- An NFA with ε-transition can be formally defined as a 5-tuple (Q, Σ, δ, q0, F), where:
  - Q is a finite set of states
  - Σ is a finite set of input symbols
  - δ is a transition function that maps Q × (Σ ∪ {ε}) to 2^Q, the power set of Q
  - q0 is the initial state
  - F is a subset of Q that contains the final or accepting states
- An NFA with ε-transition accepts an input string x if there exists a sequence of states q0, q1, ..., qn such that:
  - q0 is the initial state
  - qn is a final state
  - For each i (0 ≤ i < n), either qi+1 ∈ δ(qi, xi+1) or qi+1 ∈ δ(qi, ε)
- The ε-closure of a state q, denoted by ε-closure(q), is the set of all states that can be reached from q by following only ε-transitions. The ε-closure of a set of states S, denoted by ε-closure(S), is the union of the ε-closures of all states in S.
- The language accepted by an NFA with ε-transition is the set of all strings that are accepted by the automaton. It can be shown that any NFA with ε-transition can be converted to an equivalent NFA without ε-transition, and vice versa. Therefore, NFAs with ε-transition are equivalent in expressive power to NFAs without ε-transition, and to regular expressions and regular grammars.