A probabilistic context-free grammar (PCFG) is an extension of a context-free grammar (CFG) with a probability for each production rule. PCFGs are used to model the syntax of natural languages and to resolve syntactic ambiguity by assigning probabilities to each parse tree. PCFGs can be learned from tree-banks of annotated sentences.

A PCFG consists of a set of non-terminal symbols, a set of terminal symbols, a start symbol, and a set of production rules of the form A -> B C, where A, B, and C are non-terminals, or A -> a, where A is a non-terminal and a is a terminal. Each production rule has a probability p, such that the sum of the probabilities of all rules with the same left-hand side is 1.

The following diagram illustrates the basic structure of a PCFG:

```
    +-----------------+
    | Non-terminal    |
    | symbols         |
    +-----------------+
          |  ^
          |  |
          |  | Start symbol
          |  |
          v  |
    +-----------------+
    | Production      |
    | rules with      |
    | probabilities   |
    +-----------------+
          |  ^
          |  |
          |  | Parse trees
          |  |
          v  |
    +-----------------+
    | Terminal        |
    | symbols         |
    +-----------------+
```