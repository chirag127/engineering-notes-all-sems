# Translation with a Top Down Parser

- Translation with a top down parser is a technique of syntax-directed translation that involves passing information from the root node to the leaf nodes of the parse tree.
- A top down parser constructs the parse tree from the top (start symbol) to the bottom (input string) by using leftmost derivation.
- A top down parser can be implemented by a recursive descent parser or a predictive parser.
- A top down parser can use attributes and semantic actions to perform translation during parsing.
- Attributes are values associated with the nodes of the parse tree that store information about the syntax and semantics of the input string.
- Semantic actions are fragments of code that are executed when a production is applied during parsing. They can manipulate the attributes of the nodes and perform other tasks such as generating intermediate code, checking types, or reporting errors.
- A top down parser can use two types of attributes: synthesized attributes and inherited attributes.
- Synthesized attributes are attributes that depend only on the attributes of the children nodes. They are computed in a bottom-up manner and passed up the parse tree.
- Inherited attributes are attributes that depend on the attributes of the parent node or the siblings nodes. They are computed in a top-down manner and passed down the parse tree.
- A top down parser can use two types of semantic actions: S-attributed actions and L-attributed actions.
- S-attributed actions are semantic actions that use only synthesized attributes. They can be executed in a bottom-up parser or a top-down parser.
- L-attributed actions are semantic actions that use both synthesized and inherited attributes, but the inherited attributes are restricted to be left-to-right. They can be executed in a top-down parser, but not in a bottom-up parser.