### Decidability

- Decidability is a property of a problem that indicates whether it can be solved by an algorithm in a finite number of steps.
- A problem is said to be decidable if there exists a Turing machine that halts on every input and gives a correct answer (yes or no) for the problem.
- A language is said to be decidable or recursive if there exists a Turing machine that accepts and halts on every string in the language, and rejects and halts on every string not in the language.
- A decision problem is a problem that asks a yes-no question about some input. For example, given a deterministic finite automaton (DFA) and a string, does the DFA accept the string?
- A decision problem is decidable if the language of all yes instances to the problem is decidable. For example, the acceptance problem for DFA is decidable, because there is an algorithm that simulates the DFA on the input string and halts with yes or no.
- A decision problem is undecidable if the language of all yes instances to the problem is not decidable. For example, the halting problem for Turing machines is undecidable, because there is no algorithm that can determine whether a given Turing machine halts on a given input or not.
- Decidability is an important concept in the theory of computation, because it helps us to classify problems and languages according to their computational complexity and solvability.