### Decidability

- Decidability is a property of a problem that indicates whether it can be solved by an algorithm in a finite number of steps.
- A problem is said to be decidable if there exists a Turing machine that halts on every input and gives a correct answer (yes or no) for the problem.
- A problem is said to be undecidable if there is no Turing machine that can solve it for all possible inputs, or if there is a Turing machine that never halts on some inputs.
- A language is said to be decidable or recursive if there is a Turing machine that accepts and halts on every string in the language, and rejects and halts on every string not in the language.
- A language is said to be undecidable or non-recursive if there is no Turing machine that can decide it, or if there is a Turing machine that accepts some strings in the language but does not halt on some strings not in the language.
- Decidability is an important concept in the theory of computation, as it helps to classify the problems and languages according to their computational complexity and solvability.
- Some examples of decidable problems are:
  - Acceptance problem for DFA: Given a deterministic finite automaton (DFA) and a string, does the DFA accept the string?
  - Emptiness problem for DFA: Given a DFA, does it accept any string?
  - Equivalence problem for DFA: Given two DFAs, do they accept the same language?
- Some examples of undecidable problems are:
  - Halting problem: Given a Turing machine and a string, does the Turing machine halt on the string?
  - Entailment problem: Given two logical formulas, does the first one imply the second one?