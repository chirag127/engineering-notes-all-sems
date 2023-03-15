### Right Linear and Left Linear Grammars

- Right linear and left linear grammars are two special types of linear grammars, which are a subclass of context-free grammars.
- A linear grammar is a grammar in which every production rule has at most one non-terminal symbol on the right-hand side.
- A right linear grammar is a linear grammar in which every production rule has the non-terminal symbol (if any) at the rightmost position of the right-hand side. For example, A -> aB | a | epsilon is a right linear grammar, where A and B are non-terminals, a is a terminal, and epsilon is the empty string.
- A left linear grammar is a linear grammar in which every production rule has the non-terminal symbol (if any) at the leftmost position of the right-hand side. For example, A -> Ba | a | epsilon is a left linear grammar, where A and B are non-terminals, a is a terminal, and epsilon is the empty string.
- Right linear and left linear grammars are equivalent in expressive power, meaning that they can generate the same set of languages, which are precisely the regular languages .
- To convert a right linear grammar to a left linear grammar, or vice versa, one can use the following steps :
  - Reverse every terminal symbol in the right-hand side of every production rule. For example, A -> aB becomes A -> Ba, and B -> ab becomes B -> ba.
  - Replace every non-terminal symbol in the right-hand side of every production rule with a new non-terminal symbol that corresponds to the reverse of the original non-terminal symbol. For example, A -> Ba becomes A -> aB', and B -> ba becomes B -> abB'.
  - Add a new start symbol S and a new production rule S -> epsilon.
  - Reverse the order of the production rules.
- For example, consider the following right linear grammar:

```
A -> aB | a | epsilon
B -> aB | bB | epsilon
```

To convert it to a left linear grammar, we can apply the steps as follows:

```
A -> aB | a | epsilon    Reverse every terminal symbol: A -> Ba | a | epsilon
B -> aB | bB | epsilon    Reverse every terminal symbol: B -> Ba | bB | epsilon

A -> Ba | a | epsilon    Replace every non-terminal symbol: A -> aB' | a | epsilon
B -> Ba | bB | epsilon    Replace every non-terminal symbol: B -> aB' | bB' | epsilon

S -> epsilon    Add a new start symbol and a new production rule

S -> epsilon    Reverse the order of the production rules
B -> aB' | bB' | epsilon
A -> aB' | a | epsilon
```

The resulting left linear grammar is:

```
S -> epsilon
B -> aB' | bB' | epsilon
A -> aB' | a | epsilon
```

- Similarly, to convert a left linear grammar to a right linear grammar, we can apply the same steps in reverse order. For example, consider the following left linear grammar:

```
A -> Ba | a | epsilon
B -> Ab | b | epsilon
```

To convert it to a right linear grammar, we can apply the steps as follows:

```
A -> Ba | a | epsilon    Reverse the order of the production rules
B -> Ab | b | epsilon

A -> Ba | a | epsilon    Replace every non-terminal symbol: A -> B'a | a | epsilon
B -> Ab | b | epsilon    Replace every non-terminal symbol: B -> A'b | b | epsilon

S -> epsilon    Add a new start symbol and a new production rule

A -> B'a | a | epsilon    Reverse every terminal symbol: A -> aB' | a | epsilon
B -> A'b | b | epsilon    Reverse every terminal symbol: B -> bA' | b | epsilon
S -> epsilon
```

The resulting right linear grammar is:

```
A -> aB' | a | epsilon
B -> bA' | b | epsilon
S -> epsilon
```