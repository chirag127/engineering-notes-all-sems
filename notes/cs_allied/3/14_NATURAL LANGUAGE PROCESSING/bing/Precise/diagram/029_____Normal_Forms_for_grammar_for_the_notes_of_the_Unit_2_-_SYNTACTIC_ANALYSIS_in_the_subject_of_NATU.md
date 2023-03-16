### Normal Forms for Grammar

In the context of syntactic analysis in natural language processing, normal forms for grammar refer to specific forms of context-free grammars that are used to simplify parsing and improve the efficiency of syntactic analysis algorithms. There are two main normal forms for context-free grammars: Chomsky Normal Form (CNF) and Greibach Normal Form (GNF).

1. **Chomsky Normal Form (CNF)**: A context-free grammar is in Chomsky Normal Form if all production rules are of the form `A -> BC` or `A -> a`, where `A`, `B`, and `C` are non-terminal symbols and `a` is a terminal symbol. This means that the right-hand side of each production rule must consist of either two non-terminals or a single terminal.

2. **Greibach Normal Form (GNF)**: A context-free grammar is in Greibach Normal Form if all production rules are of the form `A -> aB`, where `A` and `B` are non-terminal symbols and `a` is a terminal symbol. This means that the right-hand side of each production rule must start with a terminal symbol followed by zero or more non-terminals.

Both CNF and GNF have the property that they can be used to construct parsing algorithms with a polynomial time complexity. This makes them useful for practical applications of syntactic analysis in natural language processing. Additionally, any context-free grammar can be converted into an equivalent grammar in either CNF or GNF, which means that these normal forms can be used as a standard representation for context-free grammars.