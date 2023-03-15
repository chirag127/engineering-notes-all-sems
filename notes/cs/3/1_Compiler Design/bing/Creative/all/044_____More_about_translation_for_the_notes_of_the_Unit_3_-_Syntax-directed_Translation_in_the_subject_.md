# More about translation for the notes of the Unit 3 - Syntax-directed Translation in the subject of Compiler Design

- Syntax-directed translation is a method of compiler implementation where the source language translation is completely driven by the parser.
- Syntax-directed translation uses a context-free grammar with attributes and semantic actions to define the translation of the source language into the intermediate code .
- Attributes are values associated with the grammar symbols (terminals or non-terminals) that can be computed from the values of other attributes.
- Semantic actions are subroutines that are executed by the parser at the appropriate time to perform the translation.
- Syntax-directed translation can be divided into two subsets: synthesized and inherited attributes.
  - Synthesized attributes are attributes that are computed at a node from the attribute values of its children.
  - Inherited attributes are attributes that are computed at a node from the attribute values of its parent and siblings.
- Syntax-directed translation can be implemented in two ways: syntax-directed translation schemes and syntax-directed definitions.
  - Syntax-directed translation schemes are context-free grammars with semantic actions embedded within braces ({ }) in the right-hand sides of the productions.
  - Syntax-directed definitions are context-free grammars with attributes and semantic rules associated with each production.
- Syntax-directed translation can be done during parsing without building an explicit parse tree or syntax tree, or after parsing by traversing the parse tree or syntax tree in some order.
  - During parsing, the semantic actions are executed as soon as the corresponding grammar symbols are recognized by the parser.
  - After parsing, the semantic actions are executed by visiting the nodes of the parse tree or syntax tree in a bottom-up or top-down order.