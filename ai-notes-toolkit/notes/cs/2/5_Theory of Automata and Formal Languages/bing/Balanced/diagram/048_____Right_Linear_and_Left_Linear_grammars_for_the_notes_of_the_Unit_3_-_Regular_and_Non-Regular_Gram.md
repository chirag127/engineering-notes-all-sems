Hello, I am Sydney, your AI assistant. I can help you with your query. Here is some information on right linear and left linear grammars for the notes of the Unit 3 - Regular and Non-Regular Grammars in the subject of Theory of Automata and Formal Languages.

### Right Linear and Left Linear Grammars

- A **linear grammar** is a type of context-free grammar in which the right-hand side of each production rule consists of at most one non-terminal symbol and any number of terminal symbols.
- A **right linear grammar** is a linear grammar in which the non-terminal symbol, if present, is at the right end of the right-hand side of each production rule. For example, A -> aB | a | epsilon is a right linear grammar, where A and B are non-terminals, a is a terminal, and epsilon is the empty string.
- A **left linear grammar** is a linear grammar in which the non-terminal symbol, if present, is at the left end of the right-hand side of each production rule. For example, A -> Ba | a | epsilon is a left linear grammar, where A and B are non-terminals, a is a terminal, and epsilon is the empty string.
- Right linear and left linear grammars are equivalent in expressive power, meaning that they can generate the same set of languages, which are precisely the **regular languages**.
- To convert a right linear grammar to a left linear grammar, or vice versa, one can use the following steps :
  - Reverse each terminal symbol in the right-hand side of each production rule. For example, aB becomes Ba, and ab becomes ba.
  - Swap the left-hand side and the right-hand side of each production rule. For example, A -> aB becomes Ba -> A, and B -> epsilon becomes epsilon -> B.
  - If the original grammar had a start symbol S, introduce a new start symbol S' and add a production rule S' -> S.
- For example, consider the following right linear grammar:

```
S -> aA | bB | epsilon
A -> aA | bB | epsilon
B -> aB | bA | epsilon
```

- To convert it to a left linear grammar, we can apply the steps as follows:

```
S -> aA | bB | epsilon    Reverse each terminal: Aa -> S | Bb -> S | epsilon -> S
A -> aA | bB | epsilon    Swap left and right sides: S -> Aa | S -> Bb | S -> epsilon
B -> aB | bA | epsilon    Introduce new start symbol: S' -> S

S' -> S
S -> Aa | Bb | epsilon
A -> Ba | Ab | epsilon
B -> Aa | Bb | epsilon
```

- This is a left linear grammar equivalent to the original right linear grammar.