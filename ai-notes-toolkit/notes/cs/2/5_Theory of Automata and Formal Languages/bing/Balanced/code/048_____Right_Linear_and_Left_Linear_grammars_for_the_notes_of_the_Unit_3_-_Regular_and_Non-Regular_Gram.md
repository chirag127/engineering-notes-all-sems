### Right Linear and Left Linear Grammars

- A **linear grammar** is a formal grammar in which every production rule has at most one non-terminal symbol on the right-hand side or the left-hand side of the rule.
- A **right-linear grammar** (also called **right-regular grammar**) is a linear grammar in which every production rule has at most one non-terminal symbol on the right-hand side of the rule.
- A **left-linear grammar** (also called **left-regular grammar**) is a linear grammar in which every production rule has at most one non-terminal symbol on the left-hand side of the rule.
- Right-linear and left-linear grammars are equivalent in expressive power, meaning that they can generate the same set of languages, which are called **regular languages**.
- To convert a right-linear grammar to a left-linear grammar, or vice versa, we can use the following steps :
  - Reverse the order of symbols on the right-hand side of every production rule.
  - Replace every non-terminal symbol on the right-hand side with a new non-terminal symbol, and vice versa.
  - Add a new start symbol and a new production rule that derives the old start symbol.
- For example, consider the following right-linear grammar:

```
S -> aA | bB
A -> aA | bB | a
B -> aA | bB | b
```

- To convert it to a left-linear grammar, we can do the following:

```
S' -> AS | BS
A -> Aa | Ba | a
B -> Ab | Bb | b
```

- Here, we have reversed the order of symbols on the right-hand side of every rule, replaced A with B and B with A, and added a new start symbol S' and a new rule S' -> AS | BS.