## Unit 3 - Syntax-directed Translation

- Syntax-directed translation is a technique for translating the source program into the target program using the syntax and semantic information of the source language.
- Syntax-directed translation can be performed at compile time or at run time, depending on the implementation strategy.
- Syntax-directed translation can be divided into two phases: synthesis and analysis.
  - Synthesis is the process of constructing the target program from the bottom up, using the attributes and actions associated with the grammar rules of the source language.
  - Analysis is the process of checking the validity and meaning of the source program from the top down, using the attributes and actions associated with the grammar symbols of the source language.
- Syntax-directed translation can be implemented using two data structures: syntax trees and annotated parse trees.
  - A syntax tree is a tree representation of the derivation of the source program, where each node corresponds to a grammar symbol and each leaf corresponds to a token.
  - An annotated parse tree is a syntax tree augmented with the attribute values and actions for each node, which are computed during the parsing process.
- Syntax-directed translation can be classified into two types: S-attributed and L-attributed.
  - S-attributed translation is a type of syntax-directed translation where the attribute values depend only on the values of the children nodes or the lexical value of the node itself.
  - L-attributed translation is a type of syntax-directed translation where the attribute values depend on the values of the left siblings, the children nodes, or the lexical value of the node itself.
- Syntax-directed translation can be used for various purposes, such as type checking, intermediate code generation, code optimization, and code generation.