### Procedures call for the notes of the Unit 3 - Syntax-directed Translation in the subject of Compiler Design

- Syntax-directed translation is a method of compiler implementation where the source language translation is completely driven by the parser .
- It allows the compiler designer to define the generation of intermediate code directly in terms of the syntactic structure of the source language.
- It uses a context-free grammar with semantic rules or actions associated with each production and attributes associated with each grammar symbol .
- The semantic rules or actions are executed when the corresponding production is used during parsing .
- The attributes are values computed by the semantic rules or actions and can be used to store information about the source program .
- The attributes can be classified into two types: synthesized and inherited .
- Synthesized attributes are computed at a node from the attribute values of its children .
- Inherited attributes are computed at a node from the attribute values of its parent and siblings .
- The general approach to syntax-directed translation is to construct a parse tree or syntax tree and compute the values of attributes at the nodes of the tree by visiting them in some order.
- In many cases, translation can be done during parsing without building an explicit tree.
- Syntax-directed translation can be used for various tasks in compiler design, such as type checking, intermediate code generation, symbol table management, etc.