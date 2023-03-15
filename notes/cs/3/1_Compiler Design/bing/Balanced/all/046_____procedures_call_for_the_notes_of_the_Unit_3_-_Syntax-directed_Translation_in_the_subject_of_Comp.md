# Unit 3 - Syntax-directed Translation

- Syntax-directed translation is a method of compiler implementation where the source language translation is driven by the parser.
- The parser uses the grammar of the source language and some semantic rules to generate intermediate code or other forms of output.
- The semantic rules are associated with the grammar productions or symbols and specify how to compute the attributes of the nodes in the parse tree or syntax tree.
- The attributes are values that can be used to store information about the source program, such as types, values, locations, labels, etc.
- The semantic rules can be executed during parsing (syntax-directed definition) or after parsing (syntax-directed translation scheme).
- The order of visiting the nodes in the parse tree or syntax tree can be determined by the dependency graph of the attributes, which shows the flow of information among the nodes.
- The attributes can be classified into two types: synthesized attributes and inherited attributes.
- Synthesized attributes are computed from the attributes of the children nodes or the node itself.
- Inherited attributes are computed from the attributes of the parent node or the siblings nodes.
- A grammar that can be implemented using only synthesized attributes is called S-attributed grammar.
- A grammar that can be implemented using both synthesized and inherited attributes is called L-attributed grammar.
- Syntax-directed translation can be used for various tasks in compiler design, such as type checking, intermediate code generation, symbol table management, etc.