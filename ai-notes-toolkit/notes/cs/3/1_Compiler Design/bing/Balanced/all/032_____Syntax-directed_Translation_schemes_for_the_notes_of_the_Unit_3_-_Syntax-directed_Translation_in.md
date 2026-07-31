# Syntax-directed Translation Schemes

- A syntax-directed translation scheme is a notation that combines a context-free grammar with semantic actions .
- Semantic actions are fragments of code that specify how to generate intermediate code or perform other tasks related to the translation.
- Semantic actions can be embedded within the right sides of productions, or associated with grammar symbols .
- The order of execution of semantic actions depends on the order of traversal of the parse tree or syntax tree .
- Syntax-directed translation schemes can be classified into two types: **synthesized** and **inherited** .
- Synthesized attributes are computed from the attributes of the children nodes in the parse tree .
- Inherited attributes are computed from the attributes of the parent or sibling nodes in the parse tree .
- A syntax-directed translation scheme is **S-attributed** if it only uses synthesized attributes .
- A syntax-directed translation scheme is **L-attributed** if it uses both synthesized and inherited attributes, but the inherited attributes can be computed in a single left-to-right traversal of the parse tree .
- A syntax-directed translation scheme can be implemented by attaching semantic actions to the parser, either in a top-down or bottom-up manner .
- A syntax-directed translation scheme can also be implemented by constructing an annotated parse tree or syntax tree, and then evaluating the semantic actions in a separate traversal.
- Syntax-directed translation schemes are beneficial because they allow the compiler designer to define the generation of intermediate code directly in terms of the syntactic structure of the source language .