# Deterministic Finite Automaton (DFA)

- A deterministic finite automaton (DFA) is a type of finite state machine that accepts or rejects a given string of symbols by running through a unique sequence of states determined by the string.
- A DFA is defined by a 5-tuple M = (Q, Σ, δ, q0, F) where  :
  - Q is a finite set of states
  - Σ is a finite set of input symbols (alphabet)
  - δ is a transition function that maps Q x Σ to Q (δ: Q x Σ -> Q)
  - q0 is the initial state (q0 ∈ Q)
  - F is a set of final or accepting states (F ⊆ Q)
- A DFA can be represented by a state transition diagram, which is a directed graph with nodes as states and edges as transitions labeled by symbols from Σ.
- A DFA can also be represented by a state transition table, which is a tabular representation of the transition function δ.
- A DFA accepts a string w = a1a2...an if there exists a sequence of states r0, r1, ... rn such that:
  - r0 = q0
  - ri+1 = δ(ri, ai+1) for i = 0, 1, ... n-1
  - rn ∈ F
- A DFA rejects a string w if it does not accept it.
- A DFA recognizes a regular language, which is a language that can be expressed by a regular expression or a regular grammar.
- A DFA is deterministic because for each state and input symbol, there is exactly one transition to a next state.
- A DFA is finite because it has a finite number of states and a finite alphabet.