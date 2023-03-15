### Equivalence of DFA and NFA

- A DFA (deterministic finite automaton) is a finite state machine that accepts or rejects a given string of symbols, where each move from a state to another state is uniquely determined by the current state and the input symbol.
- An NFA (nondeterministic finite automaton) is a finite state machine that accepts or rejects a given string of symbols, where each move from a state to another state is not uniquely determined by the current state and the input symbol. An NFA can have zero, one or more than one move from a given state on a given input symbol, and can also have null moves (moves without input symbol).
- A DFA and an NFA are called equivalent if they recognize the same language, that is, if they accept the same set of strings.
- Theorem: For any language L, there is a DFA D and an NFA N such that L(D) = L(N) = L, where L(D) and L(N) are the languages accepted by D and N, respectively.
- Proof: The proof consists of two parts: (1) showing that for any DFA D, there is an equivalent NFA N, and (2) showing that for any NFA N, there is an equivalent DFA D.

(1) For any DFA D, there is an equivalent NFA N. This is trivial, since we can construct N by copying the states, transitions, initial state and final states of D, and adding no null moves. Since D has exactly one move from each state on each input symbol, N will also have exactly one move from each state on each input symbol, and no null moves. Therefore, N will behave exactly like D on any input string, and accept the same language as D.

(2) For any NFA N, there is an equivalent DFA D. This is more involved, and requires the subset construction, an important example of how an automaton B can be generically constructed from another automaton A. The idea is to construct D by simulating the behavior of N on any input string, and keeping track of all the possible states that N can be in after reading each symbol. The states of D will be subsets of the states of N, and the transitions of D will be determined by the transitions and null moves of N. The initial state of D will be the set of all states that N can reach from its initial state by following zero or more null moves. The final states of D will be the sets that contain at least one final state of N. The formal algorithm is as follows:

- Let N = (Q, Σ, δ, q0, F) be an NFA that recognizes a language L.
- Construct a DFA D = (Q', Σ, δ', q0', F') that recognizes L as follows:
  - Q' = 2^Q, the power set of Q, that is, the set of all subsets of Q.
  - q0' = E(q0), the set of all states that N can reach from q0 by following zero or more null moves. E(q) is defined as the smallest set that satisfies the following conditions:
    - q ∈ E(q)
    - If p ∈ E(q) and δ(p, ε) = r, then r ∈ E(q), where ε is the null symbol.
  - F' = {S ∈ Q' | S ∩ F ≠ ∅}, the set of all subsets of Q that contain at least one final state of N.
  - δ'(S, a) = E(U), where U = ∪{δ(p, a) | p ∈ S}, for any S ∈ Q' and a ∈ Σ. That is, δ'(S, a) is the set of all states that N can reach from any state in S by reading the symbol a and following zero or more null moves.

- The DFA D is equivalent to the NFA N, because for any input string w, D will end up in a state S ∈ Q' such that S is exactly the set of all states that N can be in after reading w. Therefore, D will accept w if and only if N accepts w, and L(D) = L(N) = L.