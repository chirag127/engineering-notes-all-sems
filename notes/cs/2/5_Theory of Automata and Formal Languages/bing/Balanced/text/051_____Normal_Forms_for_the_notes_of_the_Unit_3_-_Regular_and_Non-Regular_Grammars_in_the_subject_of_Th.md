### Normal Forms

- A normal form is a standard way of writing the production rules of a grammar, such that the rules have a certain structure or pattern.
- Normal forms are useful for simplifying the analysis and manipulation of grammars, such as parsing, generating, and proving properties of languages.
- There are different types of normal forms for different types of grammars, such as context-free grammars (CFGs) and regular grammars (RGs).
- Two common normal forms for CFGs are Chomsky normal form (CNF) and Greibach normal form (GNF).
- Two common normal forms for RGs are right-linear normal form (RLNF) and left-linear normal form (LLNF).

### Chomsky Normal Form

- A CFG is in CNF if all of its production rules are of the form:

  - A → BC, where A, B, and C are nonterminal symbols
  - A → a, where A is a nonterminal symbol and a is a terminal symbol
  - S → ε, where S is the start symbol and ε is the empty string

- Any CFG can be converted to an equivalent CFG in CNF by applying a series of transformations, such as eliminating ε-rules, unit rules, and long rules.
- CNF is useful for designing efficient parsing algorithms, such as the CYK algorithm, which can determine whether a string belongs to a language in polynomial time.

### Greibach Normal Form

- A CFG is in GNF if all of its production rules are of the form:

  - A → aα, where A is a nonterminal symbol, a is a terminal symbol, and α is a string of nonterminal symbols

- Any CFG can be converted to an equivalent CFG in GNF by applying a series of transformations, such as eliminating left recursion, left factoring, and useless symbols.
- GNF is useful for designing recursive-descent parsers, which can generate a parse tree for a string by following the production rules from left to right.

### Right-Linear Normal Form

- A RG is in RLNF if all of its production rules are of the form:

  - A → aB, where A and B are nonterminal symbols and a is a terminal symbol
  - A → a, where A is a nonterminal symbol and a is a terminal symbol
  - A → ε, where A is a nonterminal symbol and ε is the empty string

- Any RG can be converted to an equivalent RG in RLNF by applying a transformation that reverses the order of the symbols in the right-hand side of each rule.
- RLNF is useful for representing regular languages as finite automata, where each nonterminal symbol corresponds to a state, each terminal symbol corresponds to a transition, and the empty string corresponds to a final state.

### Left-Linear Normal Form

- A RG is in LLNF if all of its production rules are of the form:

  - A → Ba, where A and B are nonterminal symbols and a is a terminal symbol
  - A → a, where A is a nonterminal symbol and a is a terminal symbol
  - A → ε, where A is a nonterminal symbol and ε is the empty string

- Any RG can be converted to an equivalent RG in LLNF by applying a transformation that reverses the order of the symbols in the right-hand side of each rule and then applies the transformation for RLNF.
- LLNF is useful for representing regular languages as finite automata, where each nonterminal symbol corresponds to a state, each terminal symbol corresponds to a transition, and the empty string corresponds to a final state.