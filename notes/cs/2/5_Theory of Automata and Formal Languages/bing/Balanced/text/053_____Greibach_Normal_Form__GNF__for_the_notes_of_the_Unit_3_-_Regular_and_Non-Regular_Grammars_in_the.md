### Greibach Normal Form (GNF)

- Greibach Normal Form (GNF) is a special form of context-free grammar (CFG) that has some advantages for parsing and generating languages.
- A CFG is in GNF if all production rules are of the form: `A → aA1A2...An`, where `A, A1, A2, ..., An` are non-terminal symbols and `a` is a terminal symbol .
- GNF has the property that every derivation of a word from a GNF grammar begins with a terminal symbol, which makes it suitable for top-down parsing methods.
- GNF is also useful for generating languages, as it can be used to construct a pushdown automaton (PDA) that accepts the language of the grammar.
- Every CFG that does not generate the empty word can be converted into an equivalent GNF grammar using a systematic algorithm .
- The algorithm consists of the following steps:
  - Step 1: If the start symbol `S` occurs on some right side, create a new start symbol `S'` and a new production `S' → S`.
  - Step 2: Remove null productions (using the null production removal algorithm discussed earlier).
  - Step 3: Remove unit productions (using the unit production removal algorithm discussed earlier).
  - Step 4: Eliminate terminals that appear in the middle or at the end of right sides (using the terminal elimination algorithm discussed earlier).
  - Step 5: Eliminate left recursion (using the left recursion elimination algorithm discussed earlier).
  - Step 6: Order the non-terminal symbols in some arbitrary order, such as `S, A, B, C, ...`.
  - Step 7: For each non-terminal symbol `A`, replace each production of the form `A → Bβ`, where `B` is a non-terminal symbol that appears after `A` in the order, with `A → a1A1a2A2...anAnβ`, where `B → a1A1a2A2...anAn` is a production of `B` in GNF. Repeat this step until no such production exists.