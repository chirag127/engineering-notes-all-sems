### Decidability

- Decidability is a property of a problem that indicates whether it can be solved by an algorithm in a finite number of steps.
- A problem is said to be decidable if there exists a Turing machine that halts on every input and accepts or rejects it correctly.
- A language is said to be decidable or recursive if there exists a Turing machine that accepts and halts on every string in the language, and rejects and halts on every string not in the language.
- A decision problem is said to be decidable if the language of all yes instances to the problem is decidable.
- Examples of decidable problems are:
  - Acceptance problem for DFA: Given a DFA and a string, does the DFA accept the string?
  - Emptiness problem for DFA: Given a DFA, does it accept any string?
  - Equivalence problem for DFA: Given two DFAs, do they accept the same language?
- Decidable problems can be solved by constructing algorithms that simulate the corresponding Turing machines and check their halting and accepting behaviors.
- Decidable languages are closed under union, intersection, complement, concatenation, Kleene star, and reversal operations.