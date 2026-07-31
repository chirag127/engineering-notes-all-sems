### LR parsers

- LR parsers are a type of **bottom-up parsers** that analyse **deterministic context-free languages** in linear time .
- LR parsers read their input from **left to right** and produce a **rightmost derivation** in reverse .
- LR parsers are based on **state transition tables** that codify the grammar of the language they recognize.
- LR parsers are the most powerful parsers of all deterministic parsers in practice.
- There are several variants of LR parsers, such as:
  - SLR parsers: Simple LR parsers that use a simplified version of the LR(0) parsing table.
  - LALR parsers: Look-Ahead LR parsers that use a compact version of the LR(1) parsing table.
  - Canonical LR(1) parsers: LR parsers that use the full LR(1) parsing table with one lookahead terminal.
  - Minimal LR(1) parsers: LR parsers that use a minimal version of the LR(1) parsing table with one lookahead terminal.
  - GLR parsers: Generalized LR parsers that can handle nondeterministic and ambiguous grammars.
- LR parsers have some advantages, such as:
  - They can handle a large class of grammars, including most programming languages.
  - They can detect syntax errors as soon as possible.
  - They can be implemented efficiently using tables and stacks.
- LR parsers have some disadvantages, such as:
  - They can be difficult to construct and understand.
  - They can be large in size and memory consumption.
  - They can be incompatible with some grammar transformations, such as left factoring and left recursion elimination.