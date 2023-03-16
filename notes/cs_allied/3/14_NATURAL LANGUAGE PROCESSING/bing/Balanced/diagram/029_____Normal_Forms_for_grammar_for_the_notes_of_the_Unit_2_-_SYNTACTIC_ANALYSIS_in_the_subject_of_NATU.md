### Normal Forms for Grammar

- Normal forms for grammar are ways of transforming a grammar into a simpler or more restricted form without changing the language it generates.
- Normal forms are useful for natural language processing (NLP) because they make parsing and analyzing natural language sentences easier using efficient algorithms.
- There are different types of normal forms for grammar, such as Chomsky normal form, Greibach normal form, and Kuroda normal form.
- Chomsky normal form (CNF) is a normal form for context-free grammars (CFGs) that requires every production rule to have one of the following forms :
  - A -> BC, where A, B, and C are non-terminal symbols
  - A -> a, where A is a non-terminal symbol and a is a terminal symbol
  - S -> ε, where S is the start symbol and ε is the empty string
- Greibach normal form (GNF) is a normal form for CFGs that requires every production rule to have the following form:
  - A -> aα, where A is a non-terminal symbol, a is a terminal symbol, and α is a string of non-terminal symbols
- Kuroda normal form (KNF) is a normal form for context-sensitive grammars (CSGs) that requires every production rule to have one of the following forms:
  - A -> BC, where A, B, and C are non-terminal symbols
  - AB -> CD, where A, B, C, and D are non-terminal symbols
  - A -> a, where A is a non-terminal symbol and a is a terminal symbol
  - A -> ε, where A is a non-terminal symbol and ε is the empty string
- To convert a grammar to a normal form, there are algorithms that apply a series of transformations to the production rules, such as eliminating ε-rules, unit rules, useless symbols, and long rules .