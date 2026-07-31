### Normal Forms for Grammar

In the context of Natural Language Processing, normal forms for grammar are used to simplify the process of syntactic analysis. There are two main normal forms for context-free grammars: Chomsky Normal Form (CNF) and Greibach Normal Form (GNF).

1. **Chomsky Normal Form (CNF)**: A context-free grammar is said to be in Chomsky Normal Form if all production rules are of the form `A -> BC` or `A -> a`, where `A`, `B`, and `C` are non-terminal symbols and `a` is a terminal symbol. This means that the right-hand side of each production rule must consist of either two non-terminals or a single terminal.

2. **Greibach Normal Form (GNF)**: A context-free grammar is said to be in Greibach Normal Form if all production rules are of the form `A -> aB`, where `A` and `B` are non-terminal symbols and `a` is a terminal symbol. This means that the right-hand side of each production rule must start with a terminal symbol, followed by zero or more non-terminals.

Both CNF and GNF have their own advantages and disadvantages. CNF is useful for proving theorems about context-free languages, while GNF is useful for constructing parsing algorithms. It is possible to convert a context-free grammar into either CNF or GNF, although the process may result in an increase in the number of production rules.
