# Right Linear and Left Linear Grammars

- A **linear grammar** is a type of context-free grammar in which the right-hand side of every production rule consists of at most one non-terminal symbol, possibly preceded and/or followed by some terminal symbols.
- A **right linear grammar** is a linear grammar in which the non-terminal symbol, if present, is always at the right end of the right-hand side of every production rule. For example, A -> aB | a | epsilon is a right linear grammar, where A and B are non-terminals, a is a terminal, and epsilon is the empty string.
- A **left linear grammar** is a linear grammar in which the non-terminal symbol, if present, is always at the left end of the right-hand side of every production rule. For example, A -> Ba | a | epsilon is a left linear grammar, where A and B are non-terminals, a is a terminal, and epsilon is the empty string.
- Right linear and left linear grammars are equivalent in expressive power, meaning that they can generate the same set of languages, which are precisely the **regular languages** .
- To convert a right linear grammar to a left linear grammar, we can use the following steps :
  - Reverse every terminal symbol in the right-hand side of every production rule. For example, A -> aB becomes A -> Ba, and B -> ab becomes B -> ba.
  - Replace every non-terminal symbol in the right-hand side of every production rule with a new non-terminal symbol that corresponds to the reverse of the original non-terminal symbol. For example, A -> Ba becomes A -> aB', and B -> ba becomes B -> abB'.
  - Add a new start symbol S and a new production rule S -> aA', where A' is the reverse of the original start symbol A.
  - Eliminate any epsilon productions by removing them and adding new production rules that skip the non-terminal symbol that produces epsilon. For example, if B -> epsilon, then remove it and add A -> a for every production rule of the form A -> aB.
- To convert a left linear grammar to a right linear grammar, we can use the same steps but in reverse order :
  - Eliminate any epsilon productions by removing them and adding new production rules that skip the non-terminal symbol that produces epsilon. For example, if B -> epsilon, then remove it and add A -> a for every production rule of the form A -> Ba.
  - Add a new start symbol S and a new production rule S -> A'a, where A' is the reverse of the original start symbol A.
  - Replace every non-terminal symbol in the left-hand side of every production rule with a new non-terminal symbol that corresponds to the reverse of the original non-terminal symbol. For example, A -> Ba becomes B' -> aA, and B -> ab becomes B' -> bA.
  - Reverse every terminal symbol in the left-hand side of every production rule. For example, B' -> aA becomes B' -> Aa, and B' -> bA becomes B' -> Ab.