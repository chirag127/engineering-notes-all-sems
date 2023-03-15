### Decidability

- Decidability is a property of a problem that indicates whether it can be solved by an algorithm in a finite number of steps.
- A problem is decidable if there exists a Turing machine that halts on every input and gives a correct answer (yes or no) for the problem.
- A language is decidable if there exists a Turing machine that accepts and halts on every string in the language, and rejects and halts on every string not in the language.
- Decidable problems and languages are also called recursive or effectively solvable.
- Examples of decidable problems are:
  - Given a deterministic finite automaton (DFA), does it accept a given string?
  - Given a DFA, is its language empty?
  - Given a DFA, is its language finite?
  - Given two DFAs, are their languages equal?
- Decidable problems and languages can be verified by algorithms, but not necessarily by finite automata, since some decidable problems are not regular.