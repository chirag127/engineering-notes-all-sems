# More about translation for the notes of the Unit 3 - Syntax-directed Translation in the subject of Compiler Design

- Syntax-directed translation is a method of compiler implementation where the source language translation is completely driven by the parser.
- It allows the compiler designer to define the generation of intermediate code directly in terms of the syntactic structure of the source language.
- It uses a context-free grammar with attributes and semantic actions associated with the grammar symbols and productions.
- Attributes are values that are computed at the nodes of the parse tree or syntax tree.
- Semantic actions are subroutines that are executed by the parser at the appropriate time for translation.
- There are two types of attributes: synthesized and inherited.
  - Synthesized attributes are computed from the attributes of the children nodes.
  - Inherited attributes are computed from the attributes of the parent and sibling nodes.
- There are two types of syntax-directed translation schemes: postfix and prefix.
  - Postfix schemes execute the semantic actions after the corresponding production is recognized.
  - Prefix schemes execute the semantic actions before the corresponding production is recognized.
- Syntax-directed translation can be done during parsing without building an explicit tree, or after parsing by traversing the tree.
- Syntax-directed translation can be implemented by using a symbol table, a stack, and a code generator.
  - The symbol table stores the attributes and values of the identifiers.
  - The stack stores the intermediate results of the semantic actions.
  - The code generator produces the intermediate code or target code from the semantic actions.