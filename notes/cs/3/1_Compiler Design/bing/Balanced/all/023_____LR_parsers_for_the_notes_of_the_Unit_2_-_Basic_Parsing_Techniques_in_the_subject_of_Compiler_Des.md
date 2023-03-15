# LR parsers

- LR parsers are a type of **bottom-up parsers** that analyse **deterministic context-free languages** in linear time .
- LR parsers read the input from **left to right** and produce a **rightmost derivation** in reverse .
- LR parsers use a **stack** to store the symbols of the derivation and a **state transition table** to guide the parsing actions .
- LR parsers can handle a large class of grammars, including **most programming languages** .
- LR parsers can detect **syntax errors** as soon as possible .
- There are several variants of LR parsers, such as:
  - **SLR** (Simple LR): uses a simplified method to construct the state transition table, but may not be able to parse some grammars that are LR .
  - **LALR** (Look-Ahead LR): uses a lookahead terminal to reduce the size of the state transition table, but may lose some parsing power compared to canonical LR .
  - **Canonical LR** (or LR(1)): uses a lookahead terminal to distinguish between different parsing actions, and can parse any grammar that is LR .
  - **Minimal LR** (or LR(0)): uses the smallest possible state transition table, but may require more parsing actions than other variants.
  - **GLR** (Generalized LR): uses a non-deterministic automaton to handle ambiguous grammars that are not LR.