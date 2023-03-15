### Finite Automata and Regular Expression

Unit 2 - Regular Expressions and Languages

Theory of Automata and Formal Languages

1. **Finite Automata** is a mathematical model used to recognize patterns within input taken from some character set (or alphabet).
2. It is a 5-tuple (Q, Σ, δ, q0, F) where:
    - Q is a finite set of states.
    - Σ is a finite set of input symbols.
    - δ is the transition function (δ: Q × Σ → Q).
    - q0 ∈ Q is the initial state.
    - F ⊆ Q is the set of final or accepting states.
3. There are two types of finite automata: **Deterministic Finite Automata (DFA)** and **Nondeterministic Finite Automata (NFA)**.
4. **Regular Expression** is a sequence of characters that defines a search pattern. These patterns are used by string-searching algorithms for "find" or "find and replace" operations on strings.
5. Regular expressions can be used to describe regular languages, which are the languages that can be recognized by a finite automaton.
6. The relationship between finite automata and regular expressions is that for every regular expression, there exists a finite automaton that recognizes the language described by the regular expression, and vice versa.
7. Regular expressions can be converted to finite automata and finite automata can be converted to regular expressions using various algorithms.
