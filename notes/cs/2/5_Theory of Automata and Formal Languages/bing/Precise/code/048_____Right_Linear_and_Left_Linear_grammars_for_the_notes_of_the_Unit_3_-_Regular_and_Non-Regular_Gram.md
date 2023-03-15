### Right Linear and Left Linear grammars

Right linear and left linear grammars are two types of regular grammars. They are used to generate regular languages, which are a subset of the context-free languages.

- **Right Linear Grammars**: In a right linear grammar, the production rules are of the form `A -> aB` or `A -> a`, where `A` and `B` are non-terminal symbols and `a` is a terminal symbol. This means that the non-terminal symbol can only appear on the right side of the production rule.

- **Left Linear Grammars**: In a left linear grammar, the production rules are of the form `A -> Ba` or `A -> a`, where `A` and `B` are non-terminal symbols and `a` is a terminal symbol. This means that the non-terminal symbol can only appear on the left side of the production rule.

Both right linear and left linear grammars can generate the same set of regular languages. However, the structure of the grammar and the derivation trees will be different. It is possible to convert a right linear grammar to a left linear grammar and vice versa.

These grammars are important in the study of regular languages and automata theory, as they provide a way to formally define and generate regular languages. Regular languages have many applications, including in the design of regular expressions and lexical analyzers in compilers.