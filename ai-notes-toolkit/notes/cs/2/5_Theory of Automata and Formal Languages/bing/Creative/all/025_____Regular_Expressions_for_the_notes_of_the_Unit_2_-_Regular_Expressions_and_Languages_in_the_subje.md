# Regular Expressions for the notes of the Unit 2 - Regular Expressions and Languages in the subject of Theory of Automata and Formal Languages

- A **regular expression** is a symbolic notation that can be used to describe a **regular language**  .
- A **regular language** is a set of strings that can be recognized by a **finite automaton**  .
- A **finite automaton** is a mathematical model of computation that consists of a finite set of states, a finite set of input symbols, a transition function that maps states and symbols to new states, and a set of final or accepting states.
- Regular expressions can be defined recursively over an alphabet ∑ as follows:
  - The empty set ɸ is a regular expression that denotes the language ɸ.
  - The empty string ɛ is a regular expression that denotes the language {ɛ}.
  - For any symbol a ∈ ∑, a is a regular expression that denotes the language {a}.
  - If R and S are regular expressions, then so are:
    - R + S (union), which denotes the language L(R) ∪ L(S).
    - RS (concatenation), which denotes the language L(R)L(S).
    - R* (Kleene star), which denotes the language L(R)*.
  - Nothing else is a regular expression.
- Regular expressions can be used to specify patterns that can be matched in input text. For example, the regular expression a*b* denotes the language of all strings that consist of zero or more a's followed by zero or more b's, such as ɛ, a, b, ab, aa, bb, aab, abb, etc.
- Regular expressions can be represented by **regular grammars**, which are a type of formal grammar that have rules of the form A -> a or A -> aB or A -> ɛ, where A and B are variables and a is a terminal symbol. For example, the regular grammar with rules S -> aS | bS | ɛ generates the same language as the regular expression a*b*.
- Regular expressions, regular languages, and finite automata are equivalent in expressive power, meaning that for any regular expression, there exists a regular language and a finite automaton that accept the same set of strings, and vice versa  . There are algorithms to convert between these different representations.