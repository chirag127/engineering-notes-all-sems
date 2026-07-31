### Right Linear and Left Linear Grammars

- A **linear grammar** is a type of context-free grammar in which the right-hand side of each production rule consists of at most one non-terminal symbol, possibly preceded and/or followed by some terminal symbols.
- A **right linear grammar** is a linear grammar in which the non-terminal symbol, if any, appears at the right end of the right-hand side of each production rule. For example, A -> aB | a | epsilon is a right linear grammar, where A and B are non-terminals, a is a terminal, and epsilon is the empty string.
- A **left linear grammar** is a linear grammar in which the non-terminal symbol, if any, appears at the left end of the right-hand side of each production rule. For example, A -> Ba | a | epsilon is a left linear grammar, where A and B are non-terminals, a is a terminal, and epsilon is the empty string.
- Right linear and left linear grammars are equivalent in expressive power, meaning that they can generate the same set of languages, which are precisely the **regular languages** .
- To convert a right linear grammar to a left linear grammar, we can use the following steps :
  - Reverse the right-hand side of each production rule. For example, A -> aB becomes A -> Ba.
  - Replace each non-terminal symbol with a new one. For example, A -> Ba becomes A' -> B'a.
  - Swap the start symbol with the non-terminal that corresponds to the original start symbol. For example, if S is the start symbol, then S -> aB becomes B' -> aS'.
  - Reverse the right-hand side of each production rule again. For example, A' -> B'a becomes A' -> aB'.
- To convert a left linear grammar to a right linear grammar, we can use the same steps but in reverse order .
- Here are some examples of conversions between right linear and left linear grammars :

| Right Linear Grammar | Left Linear Grammar |
|----------------------|---------------------|
| A -> aB \| a \| epsilon | B' -> aA' \| a \| epsilon |
| B -> aB \| bB \| epsilon | A' -> Ba' \| Bb' \| epsilon |
| S -> aB \| bA \| epsilon | A' -> bS' \| aB' \| epsilon |
| A -> Bb \| epsilon | B' -> bA' \| epsilon |
| B -> aA \| bB \| epsilon | A' -> Ba' \| Bb' \| epsilon |
| S -> aA \| bB \| epsilon | A' -> aS' \| bB' \| epsilon |
| A -> aB \| a | B' -> aA' \| a |
| B -> bA \| b | A' -> Bb' \| b |
| S -> aA \| bB | A' -> aS' \| Bb' |