## Unit 2 - Regular Expressions and Languages

- A regular expression is a concise way of describing a set of strings that share a common pattern.
- A regular expression can be used to specify the syntax of a language, to search for patterns in a text, or to validate user input.
- A regular expression consists of symbols that represent characters, sets of characters, or operations on sets of characters.
- Some common symbols and their meanings are:

| Symbol | Meaning |
| ------ | ------- |
| a      | The character a |
| [abc]  | Any one of the characters a, b, or c |
| [a-z]  | Any one of the characters from a to z |
| [^a]   | Any character except a |
| .      | Any character |
| a*     | Zero or more occurrences of a |
| a+     | One or more occurrences of a |
| a?     | Zero or one occurrence of a |
| a{m}   | Exactly m occurrences of a |
| a{m,n} | Between m and n occurrences of a |
| a|b    | Either a or b |
| (a)    | The expression a as a unit |
| ^a     | a at the beginning of a string |
| a$     | a at the end of a string |

- A regular expression can be converted to a finite automaton, which is a machine that can recognize the strings that match the expression.
- A finite automaton consists of a finite set of states, a finite set of input symbols, a transition function that maps a state and an input symbol to a new state, a start state, and a set of final states.
- A finite automaton can be deterministic or nondeterministic, depending on whether the transition function is one-to-one or many-to-one.
- A deterministic finite automaton (DFA) can be represented by a transition table or a transition diagram, which shows the states and the transitions between them.
- A nondeterministic finite automaton (NFA) can have multiple transitions for the same state and input symbol, or transitions that do not consume any input symbol (epsilon transitions).
- An NFA can be converted to an equivalent DFA using the subset construction algorithm, which creates a new state for each subset of states in the NFA.
- A language is a set of strings over some alphabet, which is a finite set of symbols.
- A language can be defined by a regular expression, a finite automaton, or a grammar, which is a set of rules that generate strings in the language.
- A language is regular if it can be defined by a regular expression or a finite automaton.
- A language is context-free if it can be defined by a grammar that has rules of the form A -> w, where A is a single nonterminal symbol and w is a string of terminals and nonterminals.
- A language is context-sensitive if it can be defined by a grammar that has rules of the form uA -> uw, where A is a single nonterminal symbol and u and w are strings of terminals and nonterminals.
- A language is recursively enumerable if it can be defined by a grammar that has rules of any form, or by a Turing machine, which is a machine that can read and write symbols on an infinite tape.