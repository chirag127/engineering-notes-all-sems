### Normal Forms

In the context of Regular and Non-Regular Grammars in the subject of Theory of Automata and Formal Languages, normal forms refer to standard ways of representing grammars. There are several normal forms that a grammar can be converted into, including Chomsky Normal Form (CNF) and Greibach Normal Form (GNF).

1. **Chomsky Normal Form (CNF)**: A context-free grammar is said to be in Chomsky Normal Form if all of its production rules are of the form `A -> BC` or `A -> a`, where `A`, `B`, and `C` are non-terminal symbols and `a` is a terminal symbol. This means that the right-hand side of each production rule must consist of either two non-terminals or a single terminal.

2. **Greibach Normal Form (GNF)**: A context-free grammar is said to be in Greibach Normal Form if all of its production rules are of the form `A -> aB1B2...Bn`, where `A` is a non-terminal symbol, `a` is a terminal symbol, and `B1`, `B2`, ..., `Bn` are non-terminal symbols. This means that the right-hand side of each production rule must start with a terminal symbol followed by zero or more non-terminals.

Converting a grammar to one of these normal forms can be useful for certain algorithms and proofs in the study of formal languages. It is important to note that not all grammars can be converted to these normal forms, and the process of conversion may result in an equivalent grammar with a different set of production rules.