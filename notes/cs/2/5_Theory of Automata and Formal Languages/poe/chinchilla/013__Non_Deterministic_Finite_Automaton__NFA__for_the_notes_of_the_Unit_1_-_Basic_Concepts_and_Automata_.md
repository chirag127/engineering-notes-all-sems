### Non Deterministic Finite Automaton (NFA)

A Non-Deterministic Finite Automaton, or NFA, is a type of automaton used in automata theory to recognize regular languages. It is similar to a Deterministic Finite Automaton (DFA) but with some key differences:

- An NFA can have multiple transitions from a single state on the same input symbol. This allows for non-determinism in the machine, meaning that the machine can choose which path to take when there are multiple options.
- An NFA can have ε-transitions, or transitions on the empty string ε. This allows the machine to move from one state to another without consuming any input.

#### Formal Definition

An NFA is a 5-tuple (Q, Σ, δ, q0, F) where:

- Q is a finite set of states.
- Σ is a finite input alphabet.
- δ : Q × (Σ ∪ {ε}) → P(Q) is the transition function, where P(Q) is the power set of Q.
- q0 ∈ Q is the start state.
- F ⊆ Q is the set of accept states.

#### Example

Consider the following NFA:

![NFA Example](nfa-example.png)

This NFA recognizes the language {0,1}* where the last symbol is 1. The set of accepting states is {q2}. The transition function is defined as follows:

- δ(q0, 0) = {q0}
- δ(q0, 1) = {q0, q1}
- δ(q1, 0) = ∅
- δ(q1, 1) = {q2}
- δ(q2, 0) = ∅
- δ(q2, 1) = ∅

Note that there are multiple transitions from q0 on the input symbol 1, and that there is an ε-transition from q0 to q1.

#### Conversion to DFA

NFAs can be converted to DFAs using the subset construction algorithm. This algorithm constructs a DFA that simulates the behavior of the NFA by keeping track of all possible states that the NFA could be in at any given time.

#### Applications

NFAs are used in a variety of applications in computer science, including:

- Regular expression matching
- Lexical analysis in compilers
- Text search algorithms
- Network protocols