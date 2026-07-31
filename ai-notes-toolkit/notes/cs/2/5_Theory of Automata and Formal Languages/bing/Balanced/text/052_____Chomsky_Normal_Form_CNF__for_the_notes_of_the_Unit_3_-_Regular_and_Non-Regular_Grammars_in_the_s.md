### Chomsky Normal Form (CNF)

- Chomsky normal form (CNF) is a special form of context-free grammar (CFG) that has a simplified structure and is useful for parsing and generating languages.
- A CFG is in CNF if all its production rules have one of the following forms:
  - A → BC, where A, B, and C are non-terminals and B ≠ S and C ≠ S.
  - A → a, where A is a non-terminal and a is a terminal symbol.
  - S → ε, where S is the start symbol and ε is the empty string.
- Every CFG can be converted into an equivalent CNF grammar that generates the same language, by applying a series of transformations that preserve the language.
- The transformations are:
  - Step 1: If the start symbol S occurs on some right side, create a new start symbol S' and a new production S' → S.
  - Step 2: Remove null productions, i.e., productions of the form A → ε where A ≠ S.
  - Step 3: Remove unit productions, i.e., productions of the form A → B where A and B are non-terminals.
  - Step 4: Replace terminals in the right side of productions with new non-terminals and add corresponding productions. For example, A → BaC becomes A → XaY, X → B, and Y → C, where X and Y are new non-terminals.
  - Step 5: Break long productions into shorter ones by introducing new non-terminals. For example, A → BCD becomes A → XY and X → BC, where X is a new non-terminal.
- The advantages of CNF are:
  - It simplifies the structure of CFGs and reduces the number of possible derivations for a given string.
  - It allows efficient parsing algorithms, such as the CYK algorithm, that can determine whether a string belongs to a language in polynomial time.
  - It enables the construction of random sentence generators, that can produce sentences of a given length from a grammar.