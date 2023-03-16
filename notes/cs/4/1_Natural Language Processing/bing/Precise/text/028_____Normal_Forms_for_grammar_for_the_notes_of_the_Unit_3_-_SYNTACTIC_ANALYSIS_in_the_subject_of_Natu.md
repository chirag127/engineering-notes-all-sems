### Normal Forms for Grammar

In the context of Natural Language Processing, normal forms for grammar refer to the standardization of context-free grammars (CFGs) to simplify their use in syntactic analysis. There are two main normal forms for CFGs: Chomsky Normal Form (CNF) and Greibach Normal Form (GNF).

1. **Chomsky Normal Form (CNF)**: A CFG is in CNF if all production rules are of the form `A -> BC` or `A -> a`, where `A`, `B`, and `C` are non-terminal symbols and `a` is a terminal symbol. This means that the right-hand side of each production rule must consist of either two non-terminals or a single terminal.

2. **Greibach Normal Form (GNF)**: A CFG is in GNF if all production rules are of the form `A -> aB1B2...Bn`, where `A` is a non-terminal symbol, `a` is a terminal symbol, and `B1`, `B2`, ..., `Bn` are non-terminal symbols. This means that the right-hand side of each production rule must start with a terminal symbol, followed by zero or more non-terminals.

Both CNF and GNF have their advantages and disadvantages. CNF is useful for proving theorems about context-free languages, while GNF is useful for constructing parsing algorithms. Converting a CFG to either CNF or GNF can simplify the process of syntactic analysis in natural language processing.