## Unit 3 - Syntax-directed Translation

- Syntax-directed translation is a technique for translating the source program into the target program using the syntax and semantic information of the source language.
- Syntax-directed translation can be performed at compile time or at run time, depending on the implementation strategy.
- Syntax-directed translation can be divided into two phases: synthesis and analysis.
  - Synthesis is the process of constructing the target program from the bottom up, using the attributes of the syntax tree nodes and the semantic rules associated with the production rules.
  - Analysis is the process of checking the validity and consistency of the source program from the top down, using the attributes of the syntax tree nodes and the semantic rules associated with the production rules.
- Syntax-directed translation can be implemented using two methods: syntax-directed definitions and translation schemes.
  - Syntax-directed definitions are a notation for specifying the semantic rules along with the context-free grammar of the source language. They consist of a set of attribute grammars, which are grammar rules annotated with attributes and semantic functions.
  - Translation schemes are a notation for specifying the semantic rules along with the syntax-directed translation of the source language. They consist of a set of annotated parse trees, which are parse trees augmented with semantic actions and synthesized attributes.
- Syntax-directed translation can be used for various purposes, such as type checking, intermediate code generation, symbol table management, error detection and recovery, and optimization.