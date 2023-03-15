# Right Linear and Left Linear Grammars

- A **linear grammar** is a type of context-free grammar in which the right-hand side of each production rule consists of at most one non-terminal symbol and any number of terminal symbols.
- A **right linear grammar** is a linear grammar in which the non-terminal symbol, if any, is at the right end of the right-hand side of each production rule. For example, A -> aB | a | epsilon is a right linear grammar, where A and B are non-terminals, a is a terminal, and epsilon is the empty string.
- A **left linear grammar** is a linear grammar in which the non-terminal symbol, if any, is at the left end of the right-hand side of each production rule. For example, A -> Ba | a | epsilon is a left linear grammar, where A and B are non-terminals, a is a terminal, and epsilon is the empty string.
- Right linear and left linear grammars are equivalent in expressive power, meaning that they can generate the same set of languages, which are precisely the **regular languages** .
- To convert a right linear grammar to a left linear grammar, we can use the following steps :
  - Reverse the right-hand side of each production rule. For example, A -> aB becomes A -> Ba.
  - Replace each non-terminal symbol with a new one. For example, A -> Ba becomes A' -> B'a.
  - Swap the start symbol with the non-terminal that corresponds to the original start symbol. For example, if S is the original start symbol and S' is the new one, then S' -> B'a becomes S -> aB'.
  - Reverse the right-hand side of each production rule again. For example, S -> aB' becomes S -> B'a.
- To convert a left linear grammar to a right linear grammar, we can use the same steps but in reverse order :
  - Reverse the right-hand side of each production rule. For example, A -> Ba becomes A -> aB.
  - Swap the start symbol with the non-terminal that corresponds to the original start symbol. For example, if S is the original start symbol and S' is the new one, then S -> aB becomes S' -> Ba.
  - Replace each non-terminal symbol with a new one. For example, S' -> Ba becomes S' -> B'a.
  - Reverse the right-hand side of each production rule again. For example, S' -> B'a becomes S' -> aB'.