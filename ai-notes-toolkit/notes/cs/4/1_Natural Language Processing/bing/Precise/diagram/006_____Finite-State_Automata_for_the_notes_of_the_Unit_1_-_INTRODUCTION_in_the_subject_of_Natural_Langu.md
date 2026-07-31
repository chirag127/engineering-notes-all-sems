### Finite-State Automata

Finite-state automata (FSA) are computational models used to recognize patterns within input taken from some character set (or alphabet). They are used in various fields, including natural language processing, to model and analyze the behavior of systems.

- **Definition**: A finite-state automaton is a 5-tuple (Q, Σ, δ, q0, F), where:
  - Q is a finite set of states.
  - Σ is a finite input alphabet.
  - δ: Q × Σ → Q is the transition function.
  - q0 ∈ Q is the initial state.
  - F ⊆ Q is the set of final (or accepting) states.

- **Deterministic Finite Automata (DFA)**: A DFA is a type of FSA where for each state and input symbol, there is exactly one transition to a next state. In other words, the transition function is deterministic.

- **Nondeterministic Finite Automata (NFA)**: An NFA is a type of FSA where for each state and input symbol, there can be zero, one, or more transitions to next states. In other words, the transition function is nondeterministic.

- **Equivalence of DFA and NFA**: It can be shown that for any NFA, there exists an equivalent DFA that recognizes the same language. This is known as the powerset construction.

- **Regular Languages**: A language is regular if and only if there exists a finite-state automaton that recognizes it. This is known as the Kleene's theorem.

- **Closure Properties**: Regular languages are closed under union, intersection, complementation, concatenation, and Kleene star.

- **Limitations**: Finite-state automata are not capable of recognizing all languages. For example, they cannot recognize context-free languages, which require a more powerful computational model such as a pushdown automaton.

Finite-state automata are a fundamental concept in natural language processing and are used in various tasks such as tokenization, morphological analysis, and named entity recognition. They provide a simple yet powerful way to model and analyze the behavior of systems.