### Normal Forms for Grammar

In the context of Natural Language Processing, normal forms for grammar are used to simplify the process of syntactic analysis. There are two main normal forms for context-free grammars: Chomsky Normal Form (CNF) and Greibach Normal Form (GNF).

1. **Chomsky Normal Form (CNF)**: A context-free grammar is in Chomsky Normal Form if all production rules are of the form `A -> BC` or `A -> a`, where `A`, `B`, and `C` are non-terminal symbols and `a` is a terminal symbol. This means that the right-hand side of each production rule must consist of either two non-terminals or a single terminal.

2. **Greibach Normal Form (GNF)**: A context-free grammar is in Greibach Normal Form if all production rules are of the form `A -> aB`, where `A` and `B` are non-terminal symbols and `a` is a terminal symbol. This means that the right-hand side of each production rule must start with a terminal symbol followed by zero or more non-terminals.

Both CNF and GNF are useful for simplifying the process of parsing, as they restrict the form of the production rules and make it easier to apply parsing algorithms. Additionally, any context-free grammar can be converted into an equivalent grammar in either CNF or GNF.
