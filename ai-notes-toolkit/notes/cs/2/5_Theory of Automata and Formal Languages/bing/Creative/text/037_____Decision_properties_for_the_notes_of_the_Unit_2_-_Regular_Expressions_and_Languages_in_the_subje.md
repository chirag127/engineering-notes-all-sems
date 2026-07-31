### Decision properties for the notes of the Unit 2 - Regular Expressions and Languages in the subject of Theory of Automata and Formal Languages

- Decision properties are questions that can be answered yes or no for a given language or a class of languages.
- For regular languages, there are several decision properties that are decidable, meaning that there exists an algorithm that can answer them in finite time.
- Some of the decision properties of regular languages are:

  - Emptiness: Given a regular expression or a finite automaton, is the language it defines empty?
  - Non-emptiness: Given a regular expression or a finite automaton, is the language it defines non-empty?
  - Finiteness: Given a regular expression or a finite automaton, is the language it defines finite?
  - Infiniteness: Given a regular expression or a finite automaton, is the language it defines infinite?
  - Membership: Given a regular expression or a finite automaton and a string, does the string belong to the language it defines?
  - Equality: Given two regular expressions or two finite automata, do they define the same language?
  - Containment: Given two regular expressions or two finite automata, is the language defined by one contained in the language defined by the other?
  - Equivalence: Given two regular expressions or two finite automata, are they equivalent, meaning that they define the same language and have the same number of states?
  - Minimality: Given a regular expression or a finite automaton, is it minimal, meaning that it has the smallest number of states among all the equivalent ones?

- The algorithms for deciding these properties are based on the following facts:

  - Regular expressions can be converted to finite automata and vice versa.
  - Finite automata can be converted to deterministic finite automata and vice versa.
  - Deterministic finite automata can be minimized using a partitioning algorithm.
  - Two deterministic finite automata are equivalent if and only if they have the same number of states and the same transition function.
  - Two languages are equal if and only if their difference is empty.
  - A language is empty if and only if its finite automaton has no accepting state or no path from the initial state to an accepting state.
  - A language is finite if and only if its finite automaton has no cycle or loop in the transition graph.
  - A language is infinite if and only if its finite automaton has a cycle or loop in the transition graph.
  - A string belongs to a language if and only if there is a path from the initial state to an accepting state in the finite automaton that corresponds to the string.
  - A language is contained in another language if and only if their intersection is equal to the first language.
  - A language is the complement of another language if and only if their union is equal to the alphabet star and their intersection is empty.