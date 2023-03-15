### Derivation and Parse Trees

- A derivation is a sequence of applications of production rules that transforms the start symbol of a grammar into a string of terminals.
- A parse tree is a hierarchical structure that represents the derivation of the grammar to yield input strings.
- A parse tree has the following properties:
  - The root node is the start symbol of the grammar.
  - The internal nodes are non-terminals of the grammar.
  - The leaf nodes are terminals of the grammar.
  - The order of children of a node corresponds to the order of symbols in the right-hand side of the production rule used to derive them.
- A parse tree can be constructed from a derivation by following these steps:
  - Start with a single node labeled with the start symbol.
  - For each step in the derivation, find the leftmost non-terminal node in the tree and replace it with a subtree whose root is the same non-terminal and whose children are the symbols in the right-hand side of the production rule used.
  - Repeat until all the nodes are terminals.
- A parse tree can also be used to generate a derivation by following these steps:
  - Start with the root node labeled with the start symbol.
  - For each internal node, write down the production rule that corresponds to its label and its children's labels.
  - Concatenate all the production rules in a top-down, left-to-right order.
  - Replace each non-terminal in the right-hand side of a production rule with the string derived from its subtree.
  - Repeat until the string consists of only terminals.
- A parse tree is also called a concrete syntax tree because it directly corresponds to the context-free grammar.
- A parse tree can be simplified by removing unnecessary nodes and symbols, such as parentheses, punctuation, and empty productions. The resulting tree is called an abstract syntax tree (AST), which corresponds to a simplified or abstract grammar.
- An AST is usually used in compiler design because it captures the essential structure and meaning of the source code, while ignoring the syntactic details.
- An example of a parse tree and an AST for the expression `a + b * c` is shown below:

```
Parse tree:

     E
    / \
   E   + 
  / \   \
 T   *   T
/   / \   \
a   T   *   F
    |   |   |
    b   F   c
        |
        c

AST:

    +
   / \
  a   *
     / \
    b   c
```