### Automata

Automata theory is the study of abstract machines and automata, as well as the computational problems that can be solved using them. It is a theory in theoretical computer science and discrete mathematics. The word automata (the plural of automaton) comes from the Greek word αὐτόματα, which means "self-acting".

1. An automaton is an abstract self-propelled computing device which follows a predetermined sequence of operations automatically.
2. An automaton with a finite number of states is called a Finite Automaton.
3. A finite automaton can be represented by a 5-tuple (Q, Σ, δ, q0, F) where:
    - Q is a finite set of states.
    - Σ is a finite set of symbols, called the alphabet of the automaton.
    - δ is the transition function where δ: Q × Σ → Q
    - q0 is the initial state from where any input is processed (q0 ∈ Q).
    - F is a set of final state/states of Q (F ⊆ Q).
4. There are two types of finite automata: Deterministic Finite Automata (DFA) and Non-deterministic Finite Automata (NFA).
5. DFA can be constructed equivalent to an NFA.
6. Regular languages are recognized by finite automata.
7. Finite automata are used in text processing, compilers, and hardware design.
