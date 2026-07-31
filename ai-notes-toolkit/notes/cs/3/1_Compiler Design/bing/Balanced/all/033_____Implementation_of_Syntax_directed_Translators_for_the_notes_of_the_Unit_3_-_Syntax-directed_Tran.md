# Implementation of Syntax-Directed Translators

- Syntax-directed translation is a method of compiler implementation where the source language translation is driven by the parser.
- A syntax-directed translation scheme is a context-free grammar with attributes and semantic actions associated with the grammar symbols and productions.
- Attributes are values that are computed at the nodes of the parse tree or syntax tree.
- Semantic actions are subroutines that are executed by the parser at the appropriate time for translation.
- There are two types of attributes: synthesized and inherited.
  - Synthesized attributes are computed from the attributes of the children nodes.
  - Inherited attributes are computed from the attributes of the parent and sibling nodes.
- There are two types of syntax-directed translation schemes: postfix and prefix.
  - Postfix schemes execute the semantic actions after the corresponding production is recognized.
  - Prefix schemes execute the semantic actions before the corresponding production is recognized.
- The implementation of syntax-directed translators can be done in two ways: by augmenting the parser or by using an explicit tree.
  - Augmenting the parser means embedding the semantic actions in the grammar and executing them during parsing.
  - Using an explicit tree means constructing a parse tree or syntax tree and visiting the nodes in some order to compute the attributes and execute the semantic actions.