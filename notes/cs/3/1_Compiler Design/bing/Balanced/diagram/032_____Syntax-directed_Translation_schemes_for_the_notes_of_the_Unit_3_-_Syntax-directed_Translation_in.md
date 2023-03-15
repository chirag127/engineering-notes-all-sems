### Syntax-directed Translation schemes

- A syntax-directed translation scheme is a notation that associates semantic actions with the productions of a context-free grammar .
- A semantic action is a code fragment that performs some computation related to the meaning of the program .
- A syntax-directed translation scheme can be used to define the generation of intermediate code directly in terms of the syntactic structure of the source language .
- A syntax-directed translation scheme can be implemented by attaching the semantic actions to the nodes of a parse tree or a syntax tree, and executing them in some order.
- The order of execution of the semantic actions can be determined by the parsing method (top-down or bottom-up) or by the dependency relations among the attributes of the grammar symbols .
- An attribute is a value associated with a grammar symbol that carries some information about the program.
- There are two types of attributes: synthesized and inherited .
- A synthesized attribute is computed from the attributes of the children of a node in the parse tree or syntax tree .
- An inherited attribute is computed from the attributes of the parent and siblings of a node in the parse tree or syntax tree .
- A syntax-directed translation scheme can be represented by a context-free grammar with semantic actions embedded within the right sides of the productions .
- The semantic actions are enclosed in curly braces and can appear anywhere on the right side of a production .
- The semantic actions are executed in the order in which they appear in the parse tree or syntax tree .
- A syntax-directed translation scheme can be classified into two categories: S-attributed and L-attributed.
- An S-attributed scheme is one that uses only synthesized attributes.
- An L-attributed scheme is one that uses both synthesized and inherited attributes, but the inherited attributes can be computed in a left-to-right traversal of the parse tree or syntax tree.
- An example of a syntax-directed translation scheme for generating postfix notation from infix expressions is given below:

```
E -> E + T {print('+')}
E -> E - T {print('-')}
E -> T
T -> T * F {print('*')}
T -> T / F {print('/')}
T -> F
F -> (E)
F -> digit {print(digit)}
```

- The above scheme is S-attributed and can be implemented by a bottom-up parser.
- The following diagram shows the parse tree and the execution order of the semantic actions for the input `9-5+2`:

```
          E
        / | \
       /  |  \
      /   |   \
     E    -    T
    / \      / | \
   /   \    /  |  \
  /     \  /   |   \
 E       T T    *    F
 |      / \ |       / \
 |     /   \|      /   \
 |    /     \     /     \
 F   F       F   F       F
 |   |       |   |       |
 |   |       |   |       |
 |   |       |   |       |
digit digit digit digit digit
  9     5     2     3     4

Execution order: 9 5 - 2 3 * 4 + 
Postfix notation: 9 5 - 2 3 * 4 +
```