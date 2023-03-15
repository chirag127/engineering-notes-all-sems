### Parsers

A parser is a program that is part of the compiler, and parsing is part of the compiling process. Parsing happens during the analysis stage of compilation. In parsing, code is taken from the preprocessor, broken into smaller pieces and analyzed so other software can understand it.

The parser is also known as syntax analyzer, because it checks the syntax of the source code and ensures that it conforms to the rules of the grammar. The parser also generates an intermediate representation (IR) of the source code, which is often a syntax tree or an abstract syntax tree.

There are different types of parsers in compiler design, which can be classified based on the following criteria:

- The direction of derivation: top-down or bottom-up.
- The amount of lookahead: zero, one or more symbols.
- The type of grammar: LL, LR, LALR, SLR, etc.
- The method of implementation: recursive descent, table-driven, etc.

Some examples of parsers are:

- Recursive descent parser: a top-down parser that uses recursive functions to match the input with the grammar. It is easy to implement but may have backtracking and ambiguity problems.
- Predictive parser: a top-down parser that uses a parsing table to determine the next production to apply based on the current input and stack symbols. It is efficient and avoids backtracking, but can only handle LL(1) grammars.
- Shift-reduce parser: a bottom-up parser that uses a stack and an input buffer to reduce the input to the start symbol of the grammar. It can handle a large class of grammars, but may have shift-reduce or reduce-reduce conflicts.
- LR parser: a bottom-up parser that uses a parsing table and a stack to perform shift and reduce actions based on the current state and input symbol. It can handle LR(k) grammars, which are a superset of context-free grammars. There are different variants of LR parsers, such as SLR, LALR, CLR, etc.