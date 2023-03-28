
### Greibach Normal Form (GNF)

* GNF is a normal form for context-free grammars (CFGs) which is used to transform a CFG into an equivalent CFG in Chomsky Normal Form (CNF).
* GNF ensures that all productions in the grammar have the form **A → aB**, where **A** is a non-terminal, **a** is a terminal, and **B** is a string of non-terminals.
* GNF is useful for parsing because it simplifies the process of finding a parse tree.
* In order to transform a CFG into GNF, the following steps must be taken:
    1. Remove all productions that do not have the form **A → aB**.
    2. Replace all productions of the form **A → a** with the productions **A → aX** and **X → ε**, where **X** is a new non-terminal.
    3. Replace all productions of the form **A → BC** with the productions **A → YC** and **Y → aB**, where **Y** is a new non-terminal and **a** is a terminal.
* After the transformation, the grammar is in GNF and can be used for parsing.