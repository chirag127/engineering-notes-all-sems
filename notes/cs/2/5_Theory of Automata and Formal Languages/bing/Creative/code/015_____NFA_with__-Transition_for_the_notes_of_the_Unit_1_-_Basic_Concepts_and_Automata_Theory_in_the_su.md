### NFA with ε-Transition

- An NFA with ε-transition is a type of nondeterministic finite automaton (NFA) that allows the machine to change its state without consuming any input symbol. Such transitions are denoted by the symbol ε (epsilon) in the transition diagram and function .
- An NFA with ε-transition can have zero, one or more ε-transitions from any state. The ε-transitions can be used to model the empty string, optional parts, or choices in the input language .
- An NFA with ε-transition can be formally defined as a 5-tuple (Q, Σ, δ, q0, F), where :
  - Q is a finite set of states
  - Σ is a finite set of input symbols
  - δ is a transition function that maps Q × (Σ ∪ {ε}) to P(Q), where P(Q) is the power set of Q
  - q0 is the initial state
  - F is a set of final or accepting states
- The transition function δ can be extended to δ* that maps Q × Σ* to P(Q), where Σ* is the set of all strings over Σ, as follows :
  - δ*(q, ε) = ε-closure(q), where ε-closure(q) is the set of all states reachable from q by following only ε-transitions
  - δ*(q, xa) = ∪<sub>r ∈ δ*(q, x)</sub> ε-closure(δ(r, a)), where x ∈ Σ* and a ∈ Σ
- A string w ∈ Σ* is accepted by an NFA with ε-transition if and only if δ*(q0, w) ∩ F ≠ ∅, that is, there is at least one path from the initial state to a final state that consumes w .
- An NFA with ε-transition can be converted to an equivalent NFA without ε-transition by applying the following steps :
  - For each state q, compute ε-closure(q) and mark it on the state
  - For each state q and each input symbol a, compute ∪<sub>r ∈ ε-closure(q)</sub> ε-closure(δ(r, a)) and add a transition from q to this set with label a
  - Remove all ε-transitions from the diagram
  - For each state q that is in ε-closure(q0), add q to the set of initial states
  - For each state q that is in ε-closure(F), add q to the set of final states
- The following is an example of an NFA with ε-transition that accepts the language L = {a<sup>n</sup>b<sup>m</sup> | n ≥ 1, m ≥ 0}:

![NFA with ε-transition example](https://web.cecs.pdx.edu/~sheard/course/CS311/Fall2013/ppt/NfaEpsilonDefined_files/image002.gif)

- The following is the equivalent NFA without ε-transition obtained by applying the conversion steps:

![NFA without ε-transition example](https://web.cecs.pdx.edu/~sheard/course/CS311/Fall2013/ppt/NfaEpsilonDefined_files/image003.gif)