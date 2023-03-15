### Greibach Normal Form (GNF)

- Greibach Normal Form (GNF) is a special form of context-free grammar (CFG) that has some advantages for parsing and generating languages.
- A CFG is in GNF if all production rules are of the form: `A → aA1A2...An`, where `A, A1, A2, ..., An` are non-terminal symbols and `a` is a terminal symbol.
- GNF is useful for constructing a top-down parser for a given CFG, since the first symbol of the right-hand side of any rule is always a terminal symbol.
- GNF is also useful for generating a language from a CFG, since the terminal symbols can be output in a left-to-right order.
- Any CFG can be converted to an equivalent GNF using a systematic algorithm. The algorithm consists of the following steps:
  - Step 1: If the start symbol `S` occurs on some right side, create a new start symbol `S'` and a new production `S' → S`.
  - Step 2: Remove null productions (productions of the form `A → ε`) using the null production removal algorithm.
  - Step 3: Remove unit productions (productions of the form `A → B`) using the unit production removal algorithm.
  - Step 4: Eliminate any terminal symbol that appears in a right-hand side with more than one symbol, by introducing new non-terminal symbols and productions.
  - Step 5: Order the non-terminal symbols in some order, such as `S, A, B, C, ...`.
  - Step 6: For each non-terminal symbol `A`, eliminate any non-terminal symbol `B` that appears in a right-hand side of `A` and is lower in the order, by replacing `B` with the right-hand sides of `B`.
  - Step 7: The resulting grammar is in GNF.