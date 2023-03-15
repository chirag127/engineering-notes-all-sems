# Derivation and Parse Trees

- Derivation is the process of applying production rules to replace non-terminal symbols in a string with terminal symbols or other non-terminal symbols .
- A production rule is a rule that defines how a non-terminal symbol can be rewritten as a sequence of terminal and/or non-terminal symbols .
- A grammar is a set of production rules that specify the syntax of a language .
- A parse tree is a hierarchical structure that represents the derivation of the grammar to yield input strings   .
- The root node of a parse tree has the start symbol of the grammar, and the leaf nodes have the terminal symbols of the input string   .
- A parse tree shows the order and the way in which the production rules are applied to generate the input string   .
- A parse tree can be drawn using the following steps:
  - Start with the start symbol as the root node.
  - Choose a production rule that has the root node as the left-hand side, and write the right-hand side as the children of the root node.
  - Repeat the above step for each non-terminal node, until all the nodes are terminal symbols.
  - If there is no production rule that can be applied to a non-terminal node, or if the terminal symbols do not match the input string, then the parse tree is invalid.
- A parse tree can also be called a concrete syntax tree, if it directly corresponds to the context-free grammar.
- An example of a parse tree for the input string `a + b * c` and the grammar `E -> E + T | T`, `T -> T * F | F`, `F -> a | b | c` is:

```
      E
     / \
    E   T
   / \ / \
  T  + T  F
 / \   |  |
F  *  F  c
|  |  |
a  b  b
```