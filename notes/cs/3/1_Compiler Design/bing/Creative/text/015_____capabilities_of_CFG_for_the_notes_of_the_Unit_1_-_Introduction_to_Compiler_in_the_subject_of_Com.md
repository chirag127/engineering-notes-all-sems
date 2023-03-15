### Capabilities of CFG for the notes of the Unit 1 - Introduction to Compiler in the subject of Compiler Design

- CFG stands for Context-Free Grammar, which is a formal notation for describing the syntax of a programming language.
- A CFG consists of a set of production rules that specify how to generate valid sentences in the language from a set of terminal and non-terminal symbols.
- A terminal symbol is a symbol that cannot be further decomposed into smaller symbols, such as a keyword, an identifier, or a punctuation mark.
- A non-terminal symbol is a symbol that can be replaced by a sequence of symbols according to the production rules, such as an expression, a statement, or a program.
- A production rule has the form A -> B, where A is a non-terminal symbol and B is a sequence of terminal and non-terminal symbols. The rule means that A can be replaced by B in any sentence.
- A CFG can be represented by a four-tuple (V, T, P, S), where V is the set of non-terminal symbols, T is the set of terminal symbols, P is the set of production rules, and S is the start symbol.
- For example, a CFG for a simple arithmetic language can be defined as follows:

  - V = {E, T, F}
  - T = {+, -, *, /, (, ), id, num}
  - P = {E -> E + T | E - T | T, T -> T * F | T / F | F, F -> (E) | id | num}
  - S = E

- A CFG can describe the hierarchical structure of a sentence in the language by using a parse tree, which is a tree representation of the derivation of the sentence from the start symbol.
- A parse tree has the following properties:

  - The root node is labeled with the start symbol.
  - Each internal node is labeled with a non-terminal symbol.
  - Each leaf node is labeled with a terminal symbol or an empty string.
  - The children of an internal node are labeled with the symbols on the right-hand side of the production rule that was used to replace the node's symbol.
  - The concatenation of the labels of the leaf nodes from left to right gives the sentence that was derived.

- For example, the parse tree for the sentence id + num * id in the arithmetic language is:

```
        E
       / \
      E   T
     / \ / \
    id + T  F
       / \  |
      F  * id
      |
     num
```

- A CFG can define the syntax of a language, but not the semantics, which is the meaning or behavior of the sentences in the language.
- A CFG can also define the syntax of some natural languages, such as English, but not all of them, as some natural languages have context-sensitive features that cannot be captured by a CFG.
- A CFG can be used to design a compiler, which is a program that translates a source program written in one language into a target program written in another language, usually a lower-level language that can be executed by a machine.
- A compiler typically consists of two phases: analysis and synthesis.
- The analysis phase parses the source program using a CFG and produces an intermediate representation, such as an abstract syntax tree, that captures the essential structure and meaning of the program.
- The synthesis phase transforms the intermediate representation into the target program using a set of code generation rules that map the intermediate constructs to the target constructs.
- A CFG can also be used to design a parser, which is a component of a compiler that performs the analysis phase.
- A parser can be classified into two types: top-down and bottom-up.
- A top-down parser starts from the start symbol and tries to match the input string with the production rules from left to right, using a lookahead symbol to guide the choice of the rules.
- A bottom-up parser starts from the input string and tries to reduce it to the start symbol by applying the production rules in reverse, using a stack to store the symbols that have been recognized.