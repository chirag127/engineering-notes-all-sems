### Normal Forms for grammar

- Normal forms are ways of simplifying or restricting the structure of a grammar without changing its language.
- Normal forms are useful for designing algorithms that manipulate grammars, such as parsing, generating, or transforming natural languages.
- There are different types of normal forms for different types of grammars, such as Chomsky normal form (CNF) for context-free grammars, Greibach normal form (GNF) for context-free grammars, and Kuroda normal form (KNF) for context-sensitive grammars.
- A grammar is in Chomsky normal form if every production is of the form A -> BC or A -> a, where A, B, and C are nonterminals and a is a terminal.
- A grammar is in Greibach normal form if every production is of the form A -> aB1B2...Bn, where A and Bi are nonterminals and a is a terminal.
- A grammar is in Kuroda normal form if every production is of the form A -> B, A -> BC, A -> CD, or A -> a, where A, B, C, and D are nonterminals and a is a terminal.
- Any context-free grammar can be converted to Chomsky normal form or Greibach normal form by applying a series of transformations, such as eliminating epsilon-productions, unit-productions, useless symbols, and long productions.
- Any context-sensitive grammar can be converted to Kuroda normal form by applying a series of transformations, such as introducing new nonterminals, eliminating long productions, and replacing productions of the form A -> aB with A -> aC and C -> B.