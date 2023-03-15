### Regular Languages and Computers

- Regular languages are a class of formal languages that can be defined by a regular expression, in the strict sense in theoretical computer science.
- Regular languages are used in parsing and designing programming languages and are one of the first concepts taught in computability courses.
- Regular languages and finite automata can model computational problems that require a very small amount of memory. For example, a finite automaton can generate a regular language to describe if a light switch is on or off, but it cannot keep track of how many times the light was switched on or off.
- Regular languages have the following properties:
  - They are closed under the operations of union, concatenation, and Kleene star.
  - They are recognized by deterministic finite automata (DFA) and nondeterministic finite automata (NFA).
  - They are equivalent to the languages accepted by regular grammars and right-linear grammars.
  - They have a finite number of equivalence classes under the Myhill-Nerode relation.
  - They can be decided by algorithms for emptiness, finiteness, membership, equivalence, and inclusion.
- Regular languages have limitations in their expressive power. They cannot describe languages that require counting or nesting, such as the language of balanced parentheses or the language of palindromes.
- Regular languages are a subset of context-free languages, which are a subset of recursively enumerable languages, which are a subset of all formal languages.
- The following diagram shows the hierarchy of formal languages and the corresponding models of computation:

```
+---------------------+
| All formal languages|
+---------------------+
|                     |
|                     |
|                     |
|                     |
|                     |
|                     |
|                     |
|                     |
|                     |
|                     |
|                     |
|                     |
|                     |
|                     |
|                     |
|                     |
+---------------------+
| Recursively         |
| enumerable languages|
+---------------------+
|                     |
|                     |
|                     |
|                     |
|                     |
|                     |
|                     |
|                     |
|                     |
|                     |
|                     |
|                     |
+---------------------+
| Context-free        |
| languages           |
+---------------------+
|                     |
|                     |
|                     |
|                     |
|                     |
|                     |
+---------------------+
| Regular languages   |
+---------------------+

+---------------------+     +---------------------+
| Turing machine      |     | Grammar (type 0)    |
+---------------------+     +---------------------+
|                     |     |                     |
|                     |     |                     |
|                     |     |                     |
|                     |     |                     |
|                     |     |                     |
|                     |     |                     |
|                     |     |                     |
|                     |     |                     |
|                     |     |                     |
|                     |     |                     |
|                     |     |                     |
|                     |     |                     |
+---------------------+     +---------------------+
| Pushdown automaton  |     | Grammar (type 2)    |
+---------------------+     +---------------------+
|                     |     |                     |
|                     |     |                     |
|                     |     |                     |
|                     |     |                     |
|                     |     |                     |
|                     |     |                     |
+---------------------+     +---------------------+
| Finite automaton    |     | Grammar (type 3)    |
+---------------------+     +---------------------+
```