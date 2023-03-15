## Unit 3 - Syntax-directed Translation

- Syntax-directed translation is a technique for translating the source program into the target program using the syntax and semantic information of the source language.
- Syntax-directed translation can be performed at compile time or at run time, depending on the implementation strategy.
- Syntax-directed translation can be implemented using two methods: syntax-directed definitions and translation schemes.
- Syntax-directed definitions (SDDs) are a way of specifying the translation by attaching semantic rules to the grammar productions of the source language.
- SDDs consist of a context-free grammar and a set of semantic rules, also called attributes, for each grammar symbol.
- Attributes can be classified into two types: synthesized attributes and inherited attributes.
- Synthesized attributes are computed from the attributes of the children of a parse tree node, while inherited attributes are computed from the attributes of the parent and siblings of a parse tree node.
- SDDs can be evaluated by constructing an annotated parse tree, which is a parse tree with attribute values at each node, and then applying the semantic rules in a bottom-up or top-down order.
- Bottom-up evaluation of SDDs can be done using a technique called L-attributed evaluation, which requires that each inherited attribute of a node depends only on the attributes of the nodes to its left and the synthesized attributes of its parent.
- Top-down evaluation of SDDs can be done using a technique called S-attributed evaluation, which requires that each attribute of a node is synthesized and depends only on the attributes of the children of the node.
- Translation schemes are a way of specifying the translation by embedding semantic actions in the grammar productions of the source language.
- Semantic actions are fragments of code that are executed when a production is applied during parsing.
- Semantic actions can perform various tasks, such as generating intermediate code, building symbol tables, checking types, etc.
- Translation schemes can be implemented using a parser generator tool, such as Yacc or Bison, which can generate a parser that executes the semantic actions along with the parsing process.