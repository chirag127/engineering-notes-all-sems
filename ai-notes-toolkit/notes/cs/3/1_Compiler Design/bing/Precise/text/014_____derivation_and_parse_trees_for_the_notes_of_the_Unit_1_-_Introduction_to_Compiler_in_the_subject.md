### Derivation and Parse Trees

- In the context of compiler design, a **derivation** is a sequence of grammar rule applications that transform the start symbol of a grammar into a string of terminal symbols.
- A **parse tree** is a graphical representation of a derivation, where the root of the tree is the start symbol, the leaves are the terminal symbols, and the internal nodes are the non-terminal symbols.
- There are two types of derivations: **leftmost** and **rightmost**.
- In a **leftmost derivation**, the leftmost non-terminal symbol is always expanded first.
- In a **rightmost derivation**, the rightmost non-terminal symbol is always expanded first.
- The **parse tree** can be constructed from either a leftmost or a rightmost derivation.
- The **parse tree** shows the hierarchical structure of the input string, and it is used by the compiler to generate the intermediate code and to perform semantic analysis.
- The **parse tree** is also used to detect syntax errors in the input string, by checking if the input string can be derived from the start symbol using the grammar rules.
