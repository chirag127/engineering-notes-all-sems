### Derivation and Parse Trees

- A derivation is a sequence of applications of production rules that transforms the start symbol of a grammar into a string of terminals.
- A parse tree is a hierarchical structure that represents the derivation of the grammar to yield input strings.
- The root node of a parse tree has the start symbol of the grammar, and the leaves are the terminals of the string.
- A parse tree can be constructed from a derivation by following these steps:
  - Start with a single node labeled with the start symbol.
  - For each step of the derivation, find the node labeled with the nonterminal that is replaced, and create a new node for each symbol on the right-hand side of the production rule.
  - Connect the new nodes to the parent node with branches, and label them with the symbols on the right-hand side of the production rule.
  - Repeat until all nonterminals are replaced by terminals.
- A parse tree can also be used to generate a derivation by following these steps:
  - Start with the root node labeled with the start symbol.
  - For each node with children, write the production rule that corresponds to the node and its children, with the node on the left-hand side and the children on the right-hand side.
  - Write the symbols on the right-hand side of the production rule in the order of the children from left to right.
  - Repeat until all nodes are visited and the string of terminals is obtained.
- A parse tree is also called a concrete syntax tree, because it directly corresponds to the context-free grammar.
- An abstract syntax tree is a simplified version of a parse tree, that omits some details of the grammar and focuses on the essential structure and meaning of the input string.
- An abstract syntax tree can be constructed from a parse tree by following these steps:
  - Remove the nodes that correspond to punctuation, parentheses, or other syntactic elements that do not affect the meaning of the input string.
  - Collapse the nodes that correspond to unary production rules, that is, rules that have only one symbol on the right-hand side.
  - Rename the nodes that correspond to nonterminals with more meaningful names, such as operators, operands, expressions, statements, etc.
  - Repeat until the parse tree is simplified and abstracted.
- An abstract syntax tree can also be used to generate a parse tree by following these steps:
  - Start with the root node of the abstract syntax tree.
  - For each node with children, find the production rule that corresponds to the node and its children, with the node on the left-hand side and the children on the right-hand side.
  - Create a new node for each symbol on the right-hand side of the production rule, and connect them to the parent node with branches.
  - Label the new nodes with the symbols on the right-hand side of the production rule.
  - If the node corresponds to a punctuation, parentheses, or other syntactic element, add it to the parse tree as a leaf node.
  - If the node corresponds to a unary production rule, do not create a new node, but use the existing node as the child of the parent node.
  - If the node has a different name than the nonterminal in the production rule, rename it to match the nonterminal.
  - Repeat until all nodes are visited and the parse tree is obtained.
- An example of a derivation, a parse tree, and an abstract syntax tree for the grammar:

  - S -> E
  - E -> E + T | T
  - T -> T * F | F
  - F -> (E) | id

  and the input string:

  - id + id * id

  is shown below:

  - Derivation:

    - S -> E
    - E -> E + T
    - E -> T + T
    - T -> F + T
    - F -> id + T
    - T -> T * F
    - T -> F * F
    - F -> id * F
    - F -> id * id

  - Parse tree:

    ```
        S
        |
        E
       / \
      E   T
     / \ / \
    T  + T * F
    |    |   |
    F    F   id
    |    |
    id   id
    ```

  - Abstract syntax tree:

    ```
        E
       / \
      id  +
         / \
        id  *
           / \
          id  id
    ```