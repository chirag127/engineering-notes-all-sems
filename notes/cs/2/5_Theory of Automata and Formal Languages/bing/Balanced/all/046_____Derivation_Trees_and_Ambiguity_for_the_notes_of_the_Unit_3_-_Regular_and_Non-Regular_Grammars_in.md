# Derivation Trees and Ambiguity

- A derivation tree or parse tree is a graphical representation of the derivation of a string by a context-free grammar (CFG).
- A derivation tree shows how the start symbol of the grammar generates the string by applying the production rules in a hierarchical manner.
- A derivation tree has the following properties:
  - The root node is labeled with the start symbol of the grammar.
  - The internal nodes are labeled with the non-terminal symbols of the grammar.
  - The leaf nodes are labeled with the terminal symbols or the empty string of the grammar.
  - The order of the children of a node corresponds to the order of the symbols in the right-hand side of the production rule used to expand the node.
  - The concatenation of the labels of the leaf nodes from left to right gives the derived string.
- A derivation tree can be obtained from either a leftmost derivation or a rightmost derivation of the string, where the leftmost (or rightmost) non-terminal symbol is replaced at each step.
- A derivation tree is unique for a given derivation, but a string may have more than one derivation and hence more than one derivation tree by a CFG.
- A CFG is said to be ambiguous if there exists at least one string that has more than one derivation tree by the grammar.
- Ambiguity is a property of grammars, not languages. A language may have both ambiguous and unambiguous grammars.
- Some languages are inherently ambiguous, meaning that there is no unambiguous grammar for them.
- Ambiguity can cause problems in parsing and interpretation of strings, as different derivations may lead to different meanings or structures.
- Ambiguity can be resolved or reduced by using precedence rules, associativity rules, parentheses, or other conventions to disambiguate the grammar or the string.