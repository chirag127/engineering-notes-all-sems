### Normal Forms for Grammar

- Normal forms for grammar are ways of transforming a grammar into a simpler or more restricted form without changing the language it generates.
- Normal forms are useful for simplifying the analysis and parsing of natural language sentences, as well as for proving properties of grammars and languages.
- Some common normal forms for grammar are:

  - **Chomsky Normal Form (CNF)**: A grammar is in CNF if every production rule is of the form A -> BC or A -> a, where A, B, and C are non-terminal symbols and a is a terminal symbol .
  - **Greibach Normal Form (GNF)**: A grammar is in GNF if every production rule is of the form A -> aB1B2...Bn, where A and Bi are non-terminal symbols and a is a terminal symbol.
  - **Backus-Naur Form (BNF)**: A grammar is in BNF if every production rule is of the form A -> B | C | D | ..., where A is a non-terminal symbol and B, C, D, ... are sequences of terminal and non-terminal symbols.
  - **Extended Backus-Naur Form (EBNF)**: A grammar is in EBNF if it is in BNF with some additional notation, such as parentheses, brackets, braces, and repetition operators, to express optional, alternative, and repeated elements.

- To convert a grammar to a normal form, there are some standard algorithms that can be applied, such as:

  - **Removing useless symbols**: Useless symbols are non-terminal symbols that do not appear in any derivation of a terminal string, or that cannot derive any terminal string. They can be removed by finding the set of generating symbols and the set of reachable symbols, and eliminating the symbols that are not in both sets.
  - **Removing epsilon-productions**: Epsilon-productions are rules of the form A -> ε, where ε is the empty string. They can be removed by finding the set of nullable symbols, and replacing each occurrence of a nullable symbol in a right-hand side with all possible combinations of including or excluding that symbol.
  - **Removing unit-productions**: Unit-productions are rules of the form A -> B, where A and B are non-terminal symbols. They can be removed by finding the set of unit-pairs, and adding new rules for each unit-pair that correspond to the rules of the second symbol in the pair.
  - **Converting to CNF**: To convert a grammar to CNF, the following steps can be applied after removing useless symbols, epsilon-productions, and unit-productions :

    - Introduce new non-terminal symbols for each terminal symbol that appears in a right-hand side with more than one symbol, and replace the terminal symbol with the new non-terminal symbol in the rule.
    - Introduce new non-terminal symbols for each right-hand side with more than two symbols, and replace the right-hand side with a sequence of two-symbol rules that use the new non-terminal symbols.
    - Eliminate any remaining rules that are not of the form A -> BC or A -> a.

  - **Converting to GNF**: To convert a grammar to GNF, the following steps can be applied after converting it to CNF:

    - For each rule of the form A -> BC, where B is not a terminal symbol, replace it with a set of rules of the form A -> bC1C2...Cn, where b is a terminal symbol and C1C2...Cn are the right-hand sides of the rules that have B as the left-hand side.
    - Repeat the previous step until there are no rules of the form A -> BC, where B is not a terminal symbol.
    - Eliminate any remaining rules that are not of the form A -> aB1B2...Bn.

  - **Converting to BNF**: To convert a grammar to BNF, the following steps can be applied:

    - Replace any notation that is not in BNF, such as parentheses, brackets, braces, and repetition operators, with equivalent BNF notation, such as using | for alternatives, and introducing new non-terminal symbols for optional and repeated elements.
    - Eliminate any remaining rules that are not of the form A -> B | C | D | ...

  - **Converting to EBNF**: To convert a