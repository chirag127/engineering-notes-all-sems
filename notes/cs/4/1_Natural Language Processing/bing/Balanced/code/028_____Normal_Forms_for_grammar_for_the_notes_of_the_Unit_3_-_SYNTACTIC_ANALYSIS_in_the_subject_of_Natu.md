# Normal Forms for Grammar

- Normal forms for grammar are ways of transforming a grammar into a simpler or more restricted form without changing the language it generates.
- Normal forms are useful for natural language processing (NLP) because they make parsing and analyzing natural language sentences easier using efficient algorithms.
- There are different types of normal forms for grammar, such as Chomsky normal form, Greibach normal form, and Kuroda normal form. Each normal form has its own rules and properties.
- In this section, we will focus on Chomsky normal form (CNF), which is widely used in NLP for parsing and analyzing natural language sentences.

## Chomsky Normal Form

- A grammar is in Chomsky normal form if every production rule has one of the following forms:
  - A -> BC, where A, B, and C are non-terminal symbols
  - A -> a, where A is a non-terminal symbol and a is a terminal symbol
  - S -> ε, where S is the start symbol and ε is the empty string
- Any context-free grammar can be converted to an equivalent CNF grammar using a series of transformations, such as eliminating ε-rules, unit rules, and useless symbols, and introducing new non-terminal symbols.
- The advantage of CNF is that it allows parsing sentences using the CYK algorithm, which is a dynamic programming algorithm that can determine whether a given string belongs to the language of a CNF grammar in polynomial time.
- The disadvantage of CNF is that it may increase the size of the grammar and lose some information about the original structure of the sentences.