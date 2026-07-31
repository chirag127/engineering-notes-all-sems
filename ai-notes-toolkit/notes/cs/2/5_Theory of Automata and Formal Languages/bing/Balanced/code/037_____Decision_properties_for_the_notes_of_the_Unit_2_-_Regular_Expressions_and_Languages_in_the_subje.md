### Decision properties for the notes of the Unit 2 - Regular Expressions and Languages in the subject of Theory of Automata and Formal Languages

- Decision properties are questions that can be answered yes or no for a given language or a class of languages.
- Regular languages are a class of languages that can be defined by regular expressions or finite automata.
- Some common decision properties for regular languages are:

  - Emptiness: Given a regular expression or a finite automaton, is the language it defines empty?
  - Non-emptiness: Given a regular expression or a finite automaton, is the language it defines non-empty?
  - Finiteness: Given a regular expression or a finite automaton, is the language it defines finite?
  - Infiniteness: Given a regular expression or a finite automaton, is the language it defines infinite?
  - Membership: Given a regular expression or a finite automaton and a string, does the string belong to the language it defines?
  - Equality: Given two regular expressions or two finite automata, do they define the same language?
  - Containment: Given two regular expressions or two finite automata, is the language defined by one contained in the language defined by the other?
  - Equivalence: Given two regular expressions or two finite automata, are they equivalent, i.e., can they be transformed into each other by applying some rules?

- All these decision properties are decidable for regular languages, i.e., there exist algorithms that can answer them in a finite amount of time and space.
- Some examples of algorithms for these decision properties are:

  - Emptiness: Convert the regular expression or the finite automaton into a deterministic finite automaton (DFA) and check if the set of final states is empty.
  - Non-emptiness: Convert the regular expression or the finite automaton into a DFA and check if the set of final states is non-empty.
  - Finiteness: Convert the regular expression or the finite automaton into a DFA and check if it has any cycles, i.e., paths that can be repeated infinitely. If there are no cycles, the language is finite; otherwise, it is infinite.
  - Infiniteness: Convert the regular expression or the finite automaton into a DFA and check if it has any cycles. If there are cycles, the language is infinite; otherwise, it is finite.
  - Membership: Convert the regular expression or the finite automaton into a DFA and simulate the input string on it. If the simulation ends in a final state, the string belongs to the language; otherwise, it does not.
  - Equality: Convert the two regular expressions or the two finite automata into DFAs and construct their complement and intersection. If the intersection is empty, the languages are equal; otherwise, they are not.
  - Containment: Convert the two regular expressions or the two finite automata into DFAs and construct their complement and intersection. If the intersection is equal to the complement of the first language, the first language is contained in the second; otherwise, it is not.
  - Equivalence: Convert the two regular expressions or the two finite automata into DFAs and apply some minimization algorithm to obtain the smallest equivalent DFAs. If the minimized DFAs are identical, the regular expressions or the finite automata are equivalent; otherwise, they are not.