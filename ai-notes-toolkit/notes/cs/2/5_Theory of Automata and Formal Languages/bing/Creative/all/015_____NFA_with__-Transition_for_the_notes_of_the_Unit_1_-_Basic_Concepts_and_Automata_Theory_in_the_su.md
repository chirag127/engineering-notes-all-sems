# NFA with ε-Transition

- An NFA with ε-transition is a type of nondeterministic finite automaton (NFA) that allows the machine to change its state without consuming any input symbol. Such transitions are labeled with ε in the state diagram.
- Formally, an NFA with ε-transition is a 5-tuple (Q, Σ, δ, q0, F), where:
  - Q is a finite set of states
  - Σ is a finite set of input symbols
  - δ is a transition function that maps Q × (Σ ∪ {ε}) to 2^Q, the power set of Q
  - q0 is the initial state
  - F is a set of final or accepting states
- The transition function δ can be extended to δ*: 2^Q × Σ* → 2^Q, where Σ* is the set of all strings over Σ, as follows:
  - δ*(R, ε) = ε-closure(R), where ε-closure(R) is the set of all states reachable from R by following only ε-transitions
  - δ*(R, aw) = δ*(δ*(R, a), w), where a ∈ Σ and w ∈ Σ*
- The language accepted by an NFA with ε-transition is L(N) = {w ∈ Σ* | δ*(q0, w) ∩ F ≠ ∅}, i.e., the set of all strings that lead to at least one accepting state from the initial state.
- An NFA with ε-transition can be converted to an equivalent NFA without ε-transition by applying the following steps:
  - For each state q ∈ Q, compute ε-closure(q) and store it in a table
  - For each state q ∈ Q and each symbol a ∈ Σ, compute δ'(q, a) = ε-closure(δ(ε-closure(q), a)) and store it in a table
  - Construct a new NFA (Q, Σ, δ', q0, F'), where F' = {q ∈ Q | ε-closure(q) ∩ F ≠ ∅}
- An NFA with ε-transition can also be converted to an equivalent deterministic finite automaton (DFA) by applying the subset construction algorithm, which uses the extended transition function δ* to construct a new DFA (Q', Σ, δ'', q0', F''), where:
  - Q' = 2^Q, i.e., the set of all subsets of Q
  - q0' = ε-closure(q0), i.e., the initial state of the new DFA is the ε-closure of the initial state of the NFA
  - F'' = {R ∈ Q' | R ∩ F ≠ ∅}, i.e., the set of all subsets of Q that contain at least one accepting state of the NFA
  - δ''(R, a) = δ*(R, a), i.e., the transition function of the new DFA is the same as the extended transition function of the NFA
- An example of an NFA with ε-transition that accepts the language L = {a^n b^n | n ≥ 0} is shown below:

![NFA with ε-transition example](https://web.cecs.pdx.edu/~sheard/course/CS311/Fall2013/ppt/NfaEpsilonDefined_files/image002.gif)

- The equivalent NFA without ε-transition is shown below:

![NFA without ε-transition example](https://web.cecs.pdx.edu/~sheard/course/CS311/Fall2013/ppt/NfaEpsilonDefined_files/image004.gif)

- The equivalent DFA is shown below:

![DFA example](https://web.cecs.pdx.edu/~sheard/course/CS311/Fall2013/ppt/NfaEpsilonDefined_files/image006.gif)