## Unit 3 - Syntax-directed Translation

- Syntax-directed translation is a technique for translating the source program into the target program based on the syntax and semantics of both languages.
- Syntax-directed translation can be performed at compile time or run time, depending on the implementation strategy.
- Syntax-directed translation can be divided into two phases: analysis and synthesis.
  - Analysis phase: The source program is parsed and an intermediate representation (IR) is constructed, such as an abstract syntax tree (AST) or a directed acyclic graph (DAG).
  - Synthesis phase: The IR is traversed and the target program is generated, such as assembly code or machine code.
- Syntax-directed translation can be specified using syntax-directed definitions (SDDs) or translation schemes (TSs).
  - SDDs: A set of rules that associate semantic actions with the grammar productions of the source language. Semantic actions are fragments of code that are executed when a production is recognized by the parser. Semantic actions can manipulate attributes, which are values associated with the grammar symbols or nodes of the IR.
  - TSs: A notation that embeds semantic actions within the grammar productions of the source language. Semantic actions are enclosed in curly braces and can appear anywhere in the right-hand side of a production. Semantic actions can manipulate attributes or generate target code directly.
- Syntax-directed translation can be implemented using two methods: inherited or synthesized attributes, and syntax-directed translation schemes (SDTSs).
  - Inherited attributes: Attributes whose values are computed from the attributes of the parent or siblings of a node in the IR. Inherited attributes can be evaluated using a top-down traversal of the IR, such as a depth-first search (DFS).
  - Synthesized attributes: Attributes whose values are computed from the attributes of the children of a node in the IR. Synthesized attributes can be evaluated using a bottom-up traversal of the IR, such as a postorder DFS.
  - SDTSs: A method that combines SDDs and TSs to specify and implement syntax-directed translation. SDTSs can handle both inherited and synthesized attributes, and can generate target code in a single pass of the IR. SDTSs can be implemented using a recursive-descent parser or a bottom-up parser, such as a shift-reduce parser.