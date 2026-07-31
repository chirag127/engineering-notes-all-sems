# Simulate First and Follow of any given grammar

- First and follow are two sets that are used to determine the parsing table of a grammar.
- First set of a symbol is the set of terminals that can appear at the beginning of a string derived from that symbol.
- Follow set of a symbol is the set of terminals that can appear immediately after that symbol in a string derived from the start symbol.
- To find the first set of a symbol, we can use the following rules:
  - If the symbol is a terminal, then the first set is just that terminal.
  - If the symbol is a non-terminal, then for each production of the form `A -> α`, we add the first set of `α` to the first set of `A`, except for the empty string `ε`.
  - If the symbol is a non-terminal and there is a production of the form `A -> ε`, then we add `ε` to the first set of `A`.
  - If the symbol is a string of symbols, then we add the first set of the first symbol to the first set of the string, except for `ε`. If the first symbol can derive `ε`, then we also add the first set of the second symbol, and so on, until we reach a symbol that cannot derive `ε` or the end of the string.
- To find the follow set of a symbol, we can use the following rules:
  - If the symbol is the start symbol, then we add `$` (the end-of-input marker) to the follow set of the symbol.
  - If the symbol is a non-terminal and there is a production of the form `A -> αBβ`, then we add the first set of `β` to the follow set of `B`, except for `ε`.
  - If the symbol is a non-terminal and there is a production of the form `A -> αB` or `A -> αBβ` where `β` can derive `ε`, then we add the follow set of `A` to the follow set of `B`.
- To simulate the first and follow sets of a given grammar, we can use the following algorithm:
  - Initialize the first and follow sets of each symbol to be empty.
  - Repeat the following steps until no more changes occur:
    - For each production of the form `A -> α`, apply the rules for finding the first set of `A`.
    - For each production of the form `A -> αBβ`, apply the rules for finding the follow set of `B`.
  - Return the first and follow sets of each symbol.
- For example, given the following grammar:

```
S -> AB
A -> a | ε
B -> b | ε
```

- We can simulate the first and follow sets as follows:

```
First(S) = First(A) = {a, ε}
First(B) = {b, ε}
Follow(S) = {$}
Follow(A) = First(B) - {ε} = {b}
Follow(B) = Follow(S) = {$}
```

- Therefore, the first and follow sets of the grammar are:

```
First(S) = {a, ε}
First(A) = {a, ε}
First(B) = {b, ε}
Follow(S) = {$}
Follow(A) = {b}
Follow(B) = {$}
```