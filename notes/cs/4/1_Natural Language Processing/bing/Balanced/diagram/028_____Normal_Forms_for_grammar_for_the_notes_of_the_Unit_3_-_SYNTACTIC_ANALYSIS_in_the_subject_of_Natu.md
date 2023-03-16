### Normal Forms for Grammar

- Normal forms for grammar are ways of transforming a grammar into a simpler or more restricted form without changing the language it generates.
- Normal forms are useful for parsing and analyzing natural language sentences using efficient algorithms.
- There are different types of normal forms for grammar, such as Chomsky normal form, Greibach normal form, and Kuroda normal form.
- Each normal form has its own rules and properties that define how a grammar can be converted into that form.

#### Chomsky Normal Form (CNF)

- A grammar is in Chomsky normal form if every production has one of the following forms:
  - A -> BC, where A, B, and C are non-terminal symbols
  - A -> a, where A is a non-terminal symbol and a is a terminal symbol
  - S -> ε, where S is the start symbol and ε is the empty string
- Any context-free grammar can be converted into an equivalent CNF grammar using the following steps:
  - Eliminate ε-productions, i.e. productions of the form A -> ε
  - Eliminate unit productions, i.e. productions of the form A -> B
  - Eliminate long productions, i.e. productions with more than two non-terminals on the right-hand side
  - Eliminate mixed productions, i.e. productions with both terminals and non-terminals on the right-hand side
- CNF is widely used in NLP for parsing and analyzing natural language sentences using the CYK algorithm.

#### Greibach Normal Form (GNF)

- A grammar is in Greibach normal form if every production has the following form:
  - A -> aα, where A is a non-terminal symbol, a is a terminal symbol, and α is a string of non-terminal symbols
- Any context-free grammar can be converted into an equivalent GNF grammar using the following steps:
  - Eliminate ε-productions and unit productions
  - Eliminate left recursion, i.e. productions of the form A -> Aα
  - Convert the remaining productions into the required form
- GNF is useful for parsing and analyzing natural language sentences using the top-down parsing algorithm.

#### Kuroda Normal Form (KNF)

- A grammar is in Kuroda normal form if every production has one of the following forms:
  - A -> BC, where A, B, and C are non-terminal symbols
  - A -> a, where A is a non-terminal symbol and a is a terminal symbol
  - A -> B, where A and B are non-terminal symbols
  - A -> ε, where A is the start symbol and ε is the empty string
- Any context-sensitive grammar can be converted into an equivalent KNF grammar using the following steps:
  - Eliminate ε-productions
  - Eliminate long productions
  - Eliminate mixed productions
  - Eliminate non-terminal symbols that do not appear in any derivation
- KNF is useful for proving the equivalence of context-sensitive grammars and linear bounded automata.