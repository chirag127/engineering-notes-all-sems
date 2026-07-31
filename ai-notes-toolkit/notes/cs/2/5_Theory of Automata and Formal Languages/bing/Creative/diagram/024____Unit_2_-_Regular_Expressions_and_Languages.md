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
| a|b    | Either a or b |
| (a)    | The expression a as a unit |
| ^a     | a at the beginning of a string |
| a$     | a at the end of a string |

- A regular expression can be used to define a regular language, which is a language that can be recognized by a finite automaton.
- A finite automaton is a mathematical model of computation that consists of a finite set of states, a finite set of input symbols, a transition function that maps a state and an input symbol to a new state, a start state, and a set of final or accepting states.
- A finite automaton can be represented by a state diagram, which is a graph where the nodes are the states and the edges are labeled by the input symbols that cause the transitions.
- A finite automaton can be deterministic or nondeterministic, depending on whether the transition function is a function or a relation.
- A deterministic finite automaton (DFA) has exactly one transition for each state and input symbol, and can be in only one state at a time.
- A nondeterministic finite automaton (NFA) can have zero, one, or more transitions for each state and input symbol, and can be in multiple states at the same time.
- A DFA can be simulated by an NFA, and an NFA can be converted to an equivalent DFA using the subset construction algorithm.
- A regular language is a language that can be recognized by some DFA or NFA.
- A regular language can also be defined by a regular grammar, which is a grammar that has rules of the form A -> a or A -> aB, where A and B are variables and a is a terminal symbol.
- A regular grammar can be right-linear or left-linear, depending on whether the variable B is on the right or the left of the rule.
- A right-linear grammar can be converted to an equivalent NFA, and a left-linear grammar can be converted to an equivalent NFA by reversing the strings and the rules.
- A regular language can also be defined by a regular expression, using the following rules:

| Regular Expression | Language |
| ------------------ | -------- |
| a                  | {a} |
| R1 + R2            | L(R1) U L(R2) |
| R1 R2              | L(R1) L(R2) |
| R*                 | L(R)* |
| (R)                | L(R) |
| e                  | {e} |
| Ø                  | Ø |

- where L(R) denotes the language defined by the regular expression R, U denotes the union operation, and * denotes the Kleene star operation.
- A regular expression can be converted to an equivalent NFA using the Thompson's construction algorithm, and an NFA can be converted to an equivalent regular expression using the state elimination method.
- The regular languages are closed under the following operations: union, concatenation, Kleene star, complement, intersection, difference, and reversal.
- The regular languages are not closed under the following operations: prefix, suffix, substring, and exponentiation.