## Unit 3 - Syntax-directed Translation

- Syntax-directed translation is a technique for translating the source program into the target program using the syntax and semantic information of the source language.
- Syntax-directed translation can be performed at compile time or at run time, depending on the implementation strategy.
- Syntax-directed translation can be divided into two phases: analysis and synthesis.
  - Analysis phase: It involves parsing the source program and constructing an intermediate representation, such as an abstract syntax tree (AST) or a syntax tree with attributes (also called annotated or decorated syntax tree).
  - Synthesis phase: It involves traversing the intermediate representation and generating the target program, such as assembly code or machine code.
- Syntax-directed translation can be specified using syntax-directed definitions (SDDs) or translation schemes (TSs).
  - SDDs: They are a way of attaching semantic rules to the grammar productions of the source language. Each rule defines how to compute the attributes of a grammar symbol based on the attributes of its children or siblings.
  - TSs: They are a way of embedding semantic actions in the grammar productions of the source language. Each action is a piece of code that is executed when the corresponding production is recognized by the parser.
- Syntax-directed translation can be implemented using two methods: syntax-directed translation by recursive descent or syntax-directed translation by a syntax-directed translator generator.
  - Recursive descent: It is a top-down parsing technique that uses a set of recursive procedures, one for each nonterminal of the grammar, to parse the input and perform the semantic actions.
  - Translator generator: It is a tool that takes a grammar with semantic rules or actions as input and produces a parser and a translator as output. The parser can be either top-down or bottom-up, depending on the tool. The translator can be either a direct translator or an indirect translator, depending on the intermediate representation used.