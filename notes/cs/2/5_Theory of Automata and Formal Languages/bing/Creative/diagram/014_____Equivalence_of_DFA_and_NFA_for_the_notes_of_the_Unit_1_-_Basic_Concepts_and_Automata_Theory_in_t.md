### Equivalence of DFA and NFA

- A DFA (deterministic finite automaton) is a finite state machine that accepts or rejects a given string of symbols, where each move from a state to another state is uniquely determined by the current state and the input symbol.
- An NFA (nondeterministic finite automaton) is a finite state machine that accepts or rejects a given string of symbols, where each move from a state to another state is not uniquely determined by the current state and the input symbol. An NFA can have zero, one or more than one move from a given state on a given input symbol, and can also have null moves (moves without input symbol).
- A language L is recognized by a DFA if and only if there is an NFA N such that L(N) = L, and vice versa. This means that for any language that can be recognized by a DFA, there is an equivalent NFA that recognizes the same language, and for any language that can be recognized by an NFA, there is an equivalent DFA that recognizes the same language.
- The equivalence of DFA and NFA can be proved by showing that for any DFA D, there is an NFA N such that L(N) = L(D), and for any NFA N, there is a DFA D such that L(D) = L(N).
- To show that for any DFA D, there is an NFA N such that L(N) = L(D), we can simply take N to be the same as D, since every DFA is also an NFA by definition. Therefore, L(N) = L(D) trivially holds.
- To show that for any NFA N, there is a DFA D such that L(D) = L(N), we can use the subset construction, an algorithm that converts an NFA to a DFA by simulating all possible moves of the NFA on a given input symbol. The algorithm works as follows:

  - Let N = (Q, Σ, δ, q0, F) be the NFA that recognizes a language L.
  - Let D = (Q', Σ, δ', q0', F') be the DFA that we want to construct such that L(D) = L(N).
  - Q' is the set of all subsets of Q, i.e., Q' = 2^Q. Each state in Q' represents a set of states that the NFA can be in after reading some input string.
  - q0' is the initial state of D, and it is the set of states that the NFA can be in after reading the empty string, i.e., q0' = ε-closure(q0), where ε-closure(q) is the set of states that can be reached from q by following only null moves.
  - F' is the set of final states of D, and it is the set of subsets of Q that contain at least one final state of N, i.e., F' = {S ⊆ Q | S ∩ F ≠ ∅}.
  - δ' is the transition function of D, and it is defined as follows: for any S ⊆ Q and a ∈ Σ, δ'(S, a) = ε-closure(∪q∈Sδ(q, a)), where δ(q, a) is the set of states that the NFA can move to from q on input symbol a, and ε-closure(∪q∈Sδ(q, a)) is the set of states that can be reached from any state in ∪q∈Sδ(q, a) by following only null moves.
  - The DFA D is complete, i.e., for any state S and any input symbol a, δ'(S, a) is defined. If ∪q∈Sδ(q, a) is empty, then δ'(S, a) is the empty set, which is also a state in Q'.
  - The DFA D is deterministic, i.e., for any state S and any input symbol a, δ'(S, a) is a single state in Q'.
  - The DFA D recognizes the same language as the NFA N, i.e., L(D) = L(N). This can be proved by showing that for any string w ∈ Σ*, w is accepted by D if and only if w is accepted by N.

    - If w is accepted by D, then there is a sequence of states S0, S1, ..., Sn in Q' such that S0 = q0', Sn ∈ F', and