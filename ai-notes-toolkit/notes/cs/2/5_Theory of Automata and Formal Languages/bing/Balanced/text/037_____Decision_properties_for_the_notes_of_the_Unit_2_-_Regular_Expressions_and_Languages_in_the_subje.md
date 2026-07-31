### Decision properties for the notes of the Unit 2 - Regular Expressions and Languages in the subject of Theory of Automata and Formal Languages

- Decision properties are the questions that can be answered yes or no for a given language or a class of languages.
- Regular languages are the languages that can be defined by regular expressions or finite automata.
- Some of the common decision properties for regular languages are:

  - Emptiness: Given a regular expression or a finite automaton, is the language defined by it empty?
  - Non-emptiness: Given a regular expression or a finite automaton, is the language defined by it non-empty?
  - Finiteness: Given a regular expression or a finite automaton, is the language defined by it finite?
  - Infiniteness: Given a regular expression or a finite automaton, is the language defined by it infinite?
  - Membership: Given a regular expression or a finite automaton and a string, does the string belong to the language defined by it?
  - Equality: Given two regular expressions or two finite automata, do they define the same language?
  - Containment: Given two regular expressions or two finite automata, is the language defined by one contained in the language defined by the other?
  - Equivalence: Given two regular expressions or two finite automata, are they equivalent, i.e., can they be transformed into each other by applying some rules?

- All these decision properties are decidable for regular languages, i.e., there exist algorithms that can answer them in a finite amount of time.
- Some of the algorithms that can be used to decide these properties are:

  - Emptiness: Convert the regular expression or the finite automaton into a minimal deterministic finite automaton and check if it has any final state. If yes, the language is non-empty; otherwise, it is empty.
  - Non-emptiness: The opposite of emptiness.
  - Finiteness: Convert the regular expression or the finite automaton into a minimal deterministic finite automaton and check if it has any cycle. If yes, the language is infinite; otherwise, it is finite.
  - Infiniteness: The opposite of finiteness.
  - Membership: Convert the regular expression into a finite automaton and run the string on it. If it reaches a final state, the string belongs to the language; otherwise, it does not.
  - Equality: Convert the two regular expressions or the two finite automata into minimal deterministic finite automata and check if they are isomorphic, i.e., if they have the same number of states and transitions and the same final states. If yes, the languages are equal; otherwise, they are not.
  - Containment: Convert the two regular expressions or the two finite automata into minimal deterministic finite automata and check if the language defined by one is a subset of the language defined by the other, i.e., if every string accepted by one is also accepted by the other. If yes, the language is contained; otherwise, it is not.
  - Equivalence: Convert the two regular expressions into finite automata and check if they are equivalent, i.e., if they accept the same language. This can be done by applying some rules to simplify the regular expressions or by using the equality algorithm.