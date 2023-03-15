# Normal Forms

In the context of Unit 3 - Regular and Non-Regular Grammars in the subject of Theory of Automata and Formal Languages, normal forms refer to standard ways of representing context-free grammars. There are two main normal forms for context-free grammars: Chomsky Normal Form (CNF) and Greibach Normal Form (GNF).

1. **Chomsky Normal Form (CNF)**: A context-free grammar is in Chomsky Normal Form if all production rules are of the form `A -> BC` or `A -> a`, where `A`, `B`, and `C` are non-terminal symbols and `a` is a terminal symbol. The start symbol is allowed to have a production rule of the form `S -> ε`, where `ε` represents the empty string.

2. **Greibach Normal Form (GNF)**: A context-free grammar is in Greibach Normal Form if all production rules are of the form `A -> aB`, where `A` and `B` are non-terminal symbols and `a` is a terminal symbol. The start symbol is allowed to have a production rule of the form `S -> ε`, where `ε` represents the empty string.

Both normal forms have their own advantages and disadvantages. CNF is useful for proving the pumping lemma for context-free languages, while GNF is useful for constructing pushdown automata for context-free languages.