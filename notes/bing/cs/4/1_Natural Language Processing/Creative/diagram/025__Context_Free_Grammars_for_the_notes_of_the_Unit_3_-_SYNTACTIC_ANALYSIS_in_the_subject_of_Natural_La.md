A context-free grammar (CFG) is a formal grammar that consists of a set of production rules that can be applied to a nonterminal symbol regardless of its context. A production rule is of the form A -> α, where A is a single nonterminal symbol, and α is a string of terminals and/or nonterminals (possibly empty). A CFG can be used to generate and parse strings that belong to a context-free language (CFL).

A diagram for a CFG can be drawn using the Backus-Naur form (BNF), which is a notation for expressing the production rules of a CFG. A BNF diagram consists of a set of boxes, each representing a nonterminal symbol, and a set of arrows, each representing a production rule. The arrows are labeled with the right-hand side of the production rule, and point from the left-hand side nonterminal to the nonterminal(s) or terminal(s) in the right-hand side. A special symbol ::= is used to separate the left-hand side nonterminal from the arrow label. For example, the following BNF diagram shows a CFG that generates arithmetic expressions:

    +-----------------+
    | expression ::=  |
    +-----------------+
          |     |
          |     | term
          |     v
          |  +------+
          |  | term |
          |  +------+
          |     |
          |     | factor
          |     v
          |  +--------+
          |  | factor |
          |  +--------+
          |     |
          |     | ( expression )
          |     | number
          |     v
          |  +----------+
          |  | number   |
          |  +----------+
          |     |
          |     | digit
          |     v
          |  +-------+
          |  | digit |
          |  +-------+
          |     |
          |     | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
          v     v   v   v   v   v   v   v   v   v   v
    +-----------------+   +---+   +---+   +---+   +---+   +---+   +---+   +---+   +---+   +---+
    | expression      |   | 0 |   | 1 |   | 2 |   | 3 |   | 4 |   | 5 |   | 6 |   | 7 |   | 8 |   | 9 |
    +-----------------+   +---+   +---+   +---+   +---+   +---+   +---+   +---+   +---+   +---+
          ^     ^     ^
          |     |     |
          |     |     | + | - | * | /
          |     |     v   v   v   v
          |     |   +---+ +---+ +---+ +---+
          |     |   | + | | - | | * | | / |
          |     |   +---+ +---+ +---+ +---+
          |     |
          |     | ( | )
          |     v   v
          |   +---+ +---+
          |   | ( | | ) |
          |   +---+ +---+
          |
          | expression + term | expression - term
          v
    +-----------------+
    | expression      |
    +-----------------+

I hope this diagram helps you understand the concept of context-free grammars. If you have any questions, please feel free to ask.