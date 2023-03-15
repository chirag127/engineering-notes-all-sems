# LR parsers

- LR parsers are a type of **bottom-up parsers** that analyse **deterministic context-free languages** in linear time.
- LR parsers read the input from **left to right** and produce a **rightmost derivation** in reverse.
- LR parsers use a **stack** to store the symbols of the derivation and a **state transition table** to guide the parsing actions.
- LR parsers can handle a large class of grammars, including **all LR(k) grammars**, which are grammars that can be parsed by an LR parser with **k** symbols of lookahead.
- There are several variants of LR parsers, such as:
  - **SLR parsers**, which use a simplified version of the LR(0) state transition table and a follow set to determine the reduce actions.
  - **LALR parsers**, which use a compressed version of the LR(1) state transition table by merging states with the same LR(0) core.
  - **Canonical LR(1) parsers**, which use the full LR(1) state transition table with one symbol of lookahead for each item.
  - **Minimal LR(1) parsers**, which use a reduced version of the LR(1) state transition table by eliminating redundant states and transitions.
  - **GLR parsers**, which use a generalized version of the LR algorithm that can handle **ambiguous grammars** by creating multiple parse trees.
- LR parsers have some advantages over other types of parsers, such as:
  - LR parsers can detect syntax errors as soon as possible, without reading the entire input.
  - LR parsers can handle left-recursive grammars and grammars with common prefixes, which are problematic for LL parsers.
  - LR parsers can parse a larger class of grammars than LL parsers, and are more efficient than backtracking parsers.
- LR parsers also have some disadvantages, such as:
  - LR parsers are more complex and difficult to construct than LL parsers, especially for large grammars.
  - LR parsers may require more memory than LL parsers, due to the size of the state transition table.
  - LR parsers may not be suitable for interactive or incremental parsing, as they require the entire input to be available before parsing.