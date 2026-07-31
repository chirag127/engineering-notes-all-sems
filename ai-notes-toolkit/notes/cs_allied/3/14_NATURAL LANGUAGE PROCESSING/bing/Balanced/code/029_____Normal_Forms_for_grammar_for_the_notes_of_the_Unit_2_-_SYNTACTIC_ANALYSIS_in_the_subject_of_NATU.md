### Normal Forms for Grammar

- Normal forms for grammar are ways of transforming a grammar into a simpler or more restricted form without changing the language it generates.
- Normal forms are useful for simplifying the analysis and parsing of natural languages, as well as for proving properties of grammars and languages.
- There are different types of normal forms for different types of grammars, such as regular, context-free, context-sensitive, and unrestricted grammars.
- Some examples of normal forms for grammar are:

  - **Chomsky Normal Form (CNF)**: A context-free grammar is in CNF if every production is of the form A -> BC or A -> a, where A, B, and C are non-terminals and a is a terminal. CNF is useful for parsing natural languages using the CYK algorithm.
  - **Greibach Normal Form (GNF)**: A context-free grammar is in GNF if every production is of the form A -> aB1B2...Bn, where A and Bi are non-terminals and a is a terminal. GNF is useful for parsing natural languages using a top-down parser.
  - **Kuroda Normal Form (KNF)**: A context-sensitive grammar is in KNF if every production is of the form A -> B, A -> BC, AB -> CD, or ABC -> DE, where A, B, C, D, and E are non-terminals. KNF is useful for proving that context-sensitive languages are equivalent to linear bounded automata.
  - **Backus-Naur Form (BNF)**: A meta-syntax for describing context-free grammars, where productions are of the form <symbol> ::= <expression>, where <symbol> is a non-terminal and <expression> is a sequence of terminals and non-terminals. BNF is useful for defining the syntax of programming languages and natural languages.