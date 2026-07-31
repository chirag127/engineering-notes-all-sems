# Capabilities of CFG for the notes of the Unit 1 - Introduction to Compiler in the subject of Compiler Design

- CFG stands for Context-Free Grammar, which is a formal notation for describing the syntax of a programming language.
- A CFG consists of a set of production rules that specify how to derive strings from a start symbol, using a finite set of non-terminal symbols and terminal symbols.
- A terminal symbol is a symbol that cannot be further derived, such as a keyword, an operator, or a literal in a programming language.
- A non-terminal symbol is a symbol that can be replaced by a sequence of symbols according to the production rules, such as an expression, a statement, or a program in a programming language.
- A start symbol is a special non-terminal symbol that represents the whole language.
- A production rule has the form A -> α, where A is a non-terminal symbol and α is a sequence of terminal and non-terminal symbols. It means that A can be replaced by α in a derivation.
- A derivation is a sequence of steps that apply production rules to generate a string from the start symbol. It shows how a string belongs to the language defined by the CFG.
- A parse tree is a graphical representation of a derivation, where the nodes are symbols and the edges are production rules. It shows the hierarchical structure of a string in the language.
- CFGs have the following capabilities for describing the syntax of programming languages:
  - They can capture the recursive nature of many syntactic constructs, such as nested expressions, statements, and functions.
  - They can express the precedence and associativity of operators, by using different levels of non-terminal symbols and production rules.
  - They can handle ambiguous syntax, by allowing multiple derivations or parse trees for the same string. However, ambiguity is usually undesirable and should be resolved by using additional rules or conventions.
  - They can be easily manipulated and analyzed by algorithms, such as parsing, which is the process of finding a derivation or a parse tree for a given string. Parsing is an essential task for compilers, as it checks the syntactic correctness of the source code and produces an intermediate representation for further processing.