# Translation with a Top Down Parser

- Translation with a top down parser is a technique of syntax-directed translation that involves passing information from the root node to the leaf nodes of the parse tree.
- A top down parser constructs the parse tree from the top (start symbol) to the bottom (input string) by using leftmost derivation.
- A top down parser can be implemented by a recursive descent parser or a predictive parser.
- A top down parser can use attributes and semantic actions to perform translation during parsing.
- Attributes are values associated with the nodes of the parse tree that can be used to store information such as type, value, scope, etc.
- Semantic actions are fragments of code that are executed when a production is applied during parsing. They can be used to perform operations such as code generation, symbol table manipulation, error reporting, etc.
- A top down parser can use two types of attributes: synthesized attributes and inherited attributes.
- Synthesized attributes are attributes that are computed from the attributes of the children nodes. They are passed bottom-up in the parse tree.
- Inherited attributes are attributes that are computed from the attributes of the parent node or the siblings nodes. They are passed top-down in the parse tree.
- A top down parser can use two types of semantic actions: embedded actions and inherited actions.
- Embedded actions are semantic actions that are inserted within the right-hand side of a production. They are executed when the parser recognizes the corresponding symbol in the input.
- Inherited actions are semantic actions that are attached to the left-hand side of a production. They are executed before the parser expands the corresponding non-terminal in the input.
- A top down parser can use a syntax-directed definition (SDD) to specify the attributes and semantic actions for each production in the grammar.
- A syntax-directed definition consists of a context-free grammar and a set of semantic rules that define the attributes and semantic actions for each production.
- A syntax-directed definition can be classified as S-attributed or L-attributed based on the types of attributes and semantic actions it uses.
- An S-attributed definition uses only synthesized attributes and embedded actions. It can be easily implemented by a top down parser by executing the semantic actions in postorder traversal of the parse tree.
- An L-attributed definition uses both synthesized and inherited attributes, but the inherited attributes can be computed from the attributes of the left siblings only. It can also be implemented by a top down parser by executing the semantic actions in preorder traversal of the parse tree.