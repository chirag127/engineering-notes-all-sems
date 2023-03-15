### Context-Free Grammars

Context-free grammars (CFGs) are a formal notation for describing the syntax of programming languages. They are used in the field of compiler design to specify the structure of valid programs in a given language.

A context-free grammar consists of the following components:

1. A set of non-terminal symbols, which represent syntactic categories or variables.
2. A set of terminal symbols, which represent the basic symbols or tokens of the language.
3. A set of production rules, which specify how the non-terminal symbols can be rewritten as sequences of terminal and non-terminal symbols.
4. A start symbol, which is a designated non-terminal symbol that represents the whole program.

The production rules of a context-free grammar have the form `A → α`, where `A` is a non-terminal symbol and `α` is a sequence of terminal and non-terminal symbols. The production rule `A → α` can be read as "A can be rewritten as α".

A context-free grammar generates a language, which is the set of all strings of terminal symbols that can be derived from the start symbol by repeatedly applying the production rules.

Context-free grammars are called "context-free" because the production rules can be applied regardless of the context in which the non-terminal symbol appears. This means that the same non-terminal symbol can be rewritten in the same way, no matter where it appears in the string.

Context-free grammars are widely used in the design of compilers and other language processing tools. They provide a formal way to specify the syntax of a programming language, and can be used to automatically generate parsers and other language processing tools.

In the subject of Compiler Design, context-free grammars are an important concept in Unit 1 - Introduction to Compiler. Understanding context-free grammars is essential for understanding how compilers work and how to design and implement them.