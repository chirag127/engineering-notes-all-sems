### Decision properties for the notes of the Unit 2 - Regular Expressions and Languages in the subject of Theory of Automata and Formal Languages

- Decision properties are questions that can be answered with a yes or no for a given language class, such as regular languages.
- Some examples of decision properties for regular languages are :
  - Emptiness: Given a regular expression or a finite automaton, is the language it describes empty?
  - Non-emptiness: Given a regular expression or a finite automaton, is the language it describes non-empty?
  - Finiteness: Given a regular expression or a finite automaton, is the language it describes finite?
  - Infiniteness: Given a regular expression or a finite automaton, is the language it describes infinite?
  - Membership: Given a regular expression or a finite automaton and a string, does the string belong to the language?
  - Equality: Given two regular expressions or two finite automata, do they describe the same language?
- All these decision properties are decidable for regular languages, meaning that there exists an algorithm that can answer them in a finite amount of time.
- Some algorithms for deciding these properties are :
  - Emptiness: Convert the regular expression to a finite automaton and check if there is a path from the start state to any final state. If yes, the language is non-empty. If no, the language is empty.
  - Non-emptiness: The opposite of emptiness.
  - Finiteness: Convert the regular expression to a finite automaton and check if there is a cycle in the graph of the automaton. If yes, the language is infinite. If no, the language is finite.
  - Infiniteness: The opposite of finiteness.
  - Membership: Convert the regular expression to a finite automaton and simulate the input string on the automaton. If the automaton reaches a final state, the string is in the language. If not, the string is not in the language.
  - Equality: Convert the regular expressions to finite automata and construct the automaton for the symmetric difference of the languages. If the symmetric difference is empty, the languages are equal. If not, the languages are not equal.