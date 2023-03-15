### Normal Forms

- A normal form is a standard way of writing the production rules of a context-free grammar (CFG).
- A normal form can simplify the analysis and manipulation of CFGs, such as parsing and generating languages.
- There are different types of normal forms, such as Chomsky normal form, Greibach normal form, Kuroda normal form, etc.
- Each normal form has its own criteria and advantages, and a CFG can be converted from one normal form to another by applying certain transformations.

### Chomsky Normal Form

- A CFG is in Chomsky normal form (CNF) if all of its production rules are of the form:

  - A → BC, where A, B, and C are nonterminal symbols
  - A → a, where A is a nonterminal symbol and a is a terminal symbol
  - S → ε, where S is the start symbol and ε is the empty string

- A CFG in CNF has the property that every derivation of a nonempty string has exactly 2n-1 steps, where n is the length of the string.
- A CFG in CNF can be parsed in polynomial time using the CYK algorithm.

### Greibach Normal Form

- A CFG is in Greibach normal form (GNF) if all of its production rules are of the form:

  - A → aα, where A is a nonterminal symbol, a is a terminal symbol, and α is a string of nonterminal symbols

- A CFG in GNF has the property that every leftmost derivation of a string has exactly n steps, where n is the length of the string.
- A CFG in GNF can be parsed using a recursive-descent parser with backtracking.