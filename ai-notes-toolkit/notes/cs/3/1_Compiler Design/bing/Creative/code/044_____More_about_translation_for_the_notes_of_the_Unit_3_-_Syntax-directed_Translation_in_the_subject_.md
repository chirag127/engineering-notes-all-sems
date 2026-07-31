### More about translation for the notes of the Unit 3 - Syntax-directed Translation in the subject of Compiler Design

- Syntax-directed translation is a method of compiler implementation where the source language translation is completely driven by the parser.
- It allows the compiler designer to define the generation of intermediate code directly in terms of the syntactic structure of the source language.
- It uses a context-free grammar with attributes and semantic actions associated with the grammar symbols and productions.
- The attributes are values that are computed at the nodes of the parse tree or syntax tree by visiting them in some order.
- The semantic actions are subroutines that are invoked by the parser at the appropriate time for translation.
- There are two types of attributes: synthesized and inherited.
  - Synthesized attributes are computed from the attributes of the children nodes or the node itself.
  - Inherited attributes are computed from the attributes of the parent node or the siblings nodes.
- There are two types of syntax-directed translation schemes: postfix and prefix.
  - Postfix schemes are based on bottom-up parsing and execute the semantic actions after the right-hand side of a production is recognized.
  - Prefix schemes are based on top-down parsing and execute the semantic actions before the left-hand side of a production is expanded.
- Syntax-directed translation can be implemented by augmenting the parser with semantic actions or by using an intermediate representation such as abstract syntax trees.