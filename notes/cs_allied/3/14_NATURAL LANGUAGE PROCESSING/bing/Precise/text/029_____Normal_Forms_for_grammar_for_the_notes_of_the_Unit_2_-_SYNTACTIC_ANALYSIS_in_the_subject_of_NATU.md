### Normal Forms for Grammar

In the context of natural language processing, normal forms for grammar are used to simplify the process of syntactic analysis. Here are some key points to remember:

1. **Chomsky Normal Form (CNF)**: A context-free grammar is in Chomsky Normal Form if all production rules are of the form `A -> BC` or `A -> a`, where `A`, `B`, and `C` are non-terminal symbols and `a` is a terminal symbol.

2. **Greibach Normal Form (GNF)**: A context-free grammar is in Greibach Normal Form if all production rules are of the form `A -> aB`, where `A` and `B` are non-terminal symbols and `a` is a terminal symbol.

3. **Converting to CNF**: Any context-free grammar can be converted to an equivalent grammar in Chomsky Normal Form. This involves removing null productions, unit productions, and long productions.

4. **Converting to GNF**: Any context-free grammar can be converted to an equivalent grammar in Greibach Normal Form. This involves removing left recursion and left factoring.

These normal forms are useful for simplifying the process of parsing and generating parse trees for natural language sentences. They can also be used to prove theorems about context-free languages and their properties.
