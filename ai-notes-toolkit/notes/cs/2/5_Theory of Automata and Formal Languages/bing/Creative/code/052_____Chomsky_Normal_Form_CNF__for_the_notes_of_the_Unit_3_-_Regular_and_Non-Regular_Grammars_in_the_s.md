### Chomsky Normal Form (CNF)

- Chomsky Normal Form (CNF) is a special form of context-free grammar (CFG) that has a simple and restricted structure.
- A CFG is in CNF if all its production rules are of the form:
  - A → BC, where A, B and C are non-terminal symbols
  - A → a, where A is a non-terminal symbol and a is a terminal symbol
  - S → ε, where S is the start symbol and ε is the empty string
- CNF is useful for simplifying the parsing and analysis of context-free languages, as well as proving some properties of CFGs.
- Every CFG can be converted into an equivalent CNF grammar, that is, a CNF grammar that generates the same language as the original CFG.
- The conversion process involves the following steps:
  - Step 1: If the start symbol S occurs on the right-hand side of any production, create a new start symbol S' and add a new production S' → S.
  - Step 2: Remove all ε-productions, that is, productions of the form A → ε, where A is not the start symbol. This can be done by replacing each occurrence of A on the right-hand side of any production with ε or removing it.
  - Step 3: Remove all unit productions, that is, productions of the form A → B, where A and B are non-terminal symbols. This can be done by replacing each occurrence of A on the right-hand side of any production with the right-hand side of B, and eliminating any duplicates.
  - Step 4: Convert all remaining productions into the form A → BC or A → a, where A, B and C are non-terminal symbols and a is a terminal symbol. This can be done by introducing new non-terminal symbols for each combination of symbols on the right-hand side of any production, and adding new productions for them. For example, if there is a production A → aBC, we can introduce a new non-terminal symbol X and add the productions A → XA and X → a.