### Syntax-directed Translation schemes

- A syntax-directed translation scheme is a notation that associates semantic actions with the productions of a context-free grammar .
- A semantic action is a code fragment that is executed when a production is recognized by the parser.
- A syntax-directed translation scheme can be used to define the generation of intermediate code directly in terms of the syntactic structure of the source language.
- There are two types of attributes that can be associated with the grammar symbols: synthesized and inherited.
  - A synthesized attribute is computed from the attributes of the children of a node in the parse tree.
  - An inherited attribute is computed from the attributes of the parent and siblings of a node in the parse tree.
- A syntax-directed translation scheme can be implemented by either constructing a parse tree or by using a parser stack .
  - If a parse tree is constructed, the semantic actions can be executed by visiting the nodes of the tree in some order, such as postorder or inorder.
  - If a parser stack is used, the semantic actions can be executed during parsing, without building an explicit tree. This is also called a postfix translation scheme.
- A syntax-directed translation scheme can be used to perform various tasks in the compiler, such as type checking, symbol table management, intermediate code generation, and code optimization.