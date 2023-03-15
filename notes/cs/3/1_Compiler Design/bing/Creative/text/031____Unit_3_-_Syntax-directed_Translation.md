## Unit 3 - Syntax-directed Translation

- Syntax-directed translation is a technique for translating the source program into the target program using the syntax and semantic information of the source language.
- Syntax-directed translation can be performed at compile time or at run time, depending on the implementation strategy.
- Syntax-directed translation can be implemented using two methods: syntax-directed definitions (SDDs) and translation schemes.
- Syntax-directed definitions are a way of specifying the translation by attaching semantic rules to the grammar productions of the source language.
- Translation schemes are a way of specifying the translation by augmenting the grammar productions of the source language with semantic actions that are executed during parsing.
- Syntax-directed definitions and translation schemes can be classified into two types: inherited and synthesized.
- Inherited attributes are those that are passed from the parent node to the child node in the syntax tree, while synthesized attributes are those that are computed from the child nodes and passed to the parent node in the syntax tree.
- Inherited attributes are useful for implementing context-sensitive features of the source language, such as type checking, scope rules, and parameter passing.
- Synthesized attributes are useful for implementing context-free features of the source language, such as code generation, constant folding, and expression evaluation.
- Syntax-directed translation can be applied to various phases of compilation, such as lexical analysis, syntax analysis, intermediate code generation, and code optimization.