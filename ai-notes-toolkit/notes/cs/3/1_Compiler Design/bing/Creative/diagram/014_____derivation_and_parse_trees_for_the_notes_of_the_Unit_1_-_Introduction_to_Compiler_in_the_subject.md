Hello, I am Sydney, your AI assistant. I can help you with your query. Here is some information on derivation and parse trees for the notes of the Unit 1 - Introduction to Compiler in the subject of Compiler Design.

### Derivation and Parse Trees

- A derivation is a sequence of applications of production rules that transforms the start symbol of a grammar into a string of terminals .
- A parse tree is a hierarchical structure that represents the derivation of the grammar to yield input strings .
- A parse tree has the following properties :
  - The root node is the start symbol of the grammar.
  - The internal nodes are non-terminals of the grammar.
  - The leaf nodes are terminals of the grammar.
  - The order of children of a node corresponds to the order of symbols in the right-hand side of the production rule used to derive the node.
  - The concatenation of the leaf nodes from left to right gives the input string derived by the grammar.
- A parse tree can be either a concrete syntax tree or an abstract syntax tree.
  - A concrete syntax tree, or parse tree, directly corresponds to the context-free grammar and includes all the syntactic details of the input string .
  - An abstract syntax tree, or AST, corresponds to a simplified or abstracted grammar and omits some of the syntactic details of the input string, such as parentheses, commas, etc .
  - An AST is usually used in multi-pass compilers, as it is easier to manipulate and analyze by the subsequent passes.
- An example of a grammar, a derivation, and a parse tree is given below:

Grammar:

```
S -> aAb
A -> c | d
```

Derivation:

```
S -> aAb
  -> acb
```

Parse tree:

```
    S
   / \
  a   b
 / \
A   c
```