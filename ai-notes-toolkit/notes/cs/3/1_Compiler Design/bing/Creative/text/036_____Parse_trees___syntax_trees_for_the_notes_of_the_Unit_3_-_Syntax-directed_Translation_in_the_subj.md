### Parse trees and syntax trees

- Parse trees and syntax trees are data structures that represent the syntactic structure of a source code in compiler design .
- A parse tree is created by a parser, which is a component of a compiler that processes the source code and checks it for syntactic correctness .
- A parse tree shows the complete derivation of the source code according to the grammar rules of the language .
- A parse tree is also called a concrete syntax tree (CST) because it preserves all the details of the source code, such as parentheses, operators, keywords, etc.
- A parse tree can be represented as a labeled tree, where the internal nodes are non-terminals, the leaf nodes are terminals, and the edges are productions .
- A parse tree can be used to perform syntax analysis, error detection, and intermediate code generation .

- A syntax tree is a simplified or abstracted version of a parse tree that eliminates the unnecessary details and focuses on the essential structure of the source code .
- A syntax tree is also called an abstract syntax tree (AST) because it abstracts away the syntactic details and shows only the semantic information of the source code.
- A syntax tree can be represented as a labeled tree, where the internal nodes are operators or constructors, the leaf nodes are operands or values, and the edges are arguments .
- A syntax tree can be used to perform semantic analysis, optimization, and code generation .

- An example of a parse tree and a syntax tree for the expression `a + b * c` is shown below :

```
Parse tree:

    E
   / \
  T   E'
 / \ / \
F  T' +  T
| / \  / \
a F  * T  F
  |    |  |
  b    c  ε

Syntax tree:

   +
 /   \
a    *
    / \
   b   c
```