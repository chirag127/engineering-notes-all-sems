### Greibach Normal Form (GNF)

- Greibach Normal Form (GNF) is a special form of context-free grammar (CFG) that has some advantages for parsing and proving properties of languages.
- A CFG is in GNF if all production rules are of the form: `A → aA1A2...An`, where `A, A1, A2, ..., An` are non-terminal symbols and `a` is a terminal symbol.
- GNF is useful for constructing a top-down parser for a CFG, since the first symbol on the right-hand side of any rule is always a terminal symbol.
- GNF is also useful for proving that every context-free language can be accepted by a pushdown automaton, since the terminal symbol can be matched with the input and the non-terminal symbols can be pushed onto the stack.
- Every CFG can be converted into an equivalent GNF using a systematic algorithm . The algorithm consists of the following steps:
  - Step 1: If the start symbol `S` occurs on some right side, create a new start symbol `S'` and a new production `S' → S`.
  - Step 2: Remove null productions (productions of the form `A → ε`, where `ε` is the empty string) using the null production removal algorithm discussed earlier.
  - Step 3: Remove unit productions (productions of the form `A → B`, where `A` and `B` are non-terminal symbols) using the unit production removal algorithm discussed earlier.
  - Step 4: Eliminate left recursion (direct or indirect) from the grammar using the left recursion elimination algorithm discussed earlier.
  - Step 5: For each non-terminal `A`, order the productions of the form `A → a...` (where `a` is a terminal symbol) before the productions of the form `A → B...` (where `B` is a non-terminal symbol).
  - Step 6: For each pair of non-terminals `A` and `B`, replace every production of the form `A → Bγ` (where `γ` is a string of terminal and non-terminal symbols) by the productions `A → δ1γ | δ2γ | ... | δkγ`, where `B → δ1 | δ2 | ... | δk` are all the productions for `B` that start with a terminal symbol. Repeat this step until no production of the form `A → Bγ` remains in the grammar.
  - Step 7: For each non-terminal `A`, replace every production of the form `A → aB1B2...Bn` (where `a` is a terminal symbol and `n > 1`) by the productions `A → aX1`, `X1 → B1X2`, `X2 → B2X3`, ..., `Xn-1 → Bn-1Bn`, where `X1, X2, ..., Xn-1` are new non-terminal symbols. Repeat this step until no production of the form `A → aB1B2...Bn` remains in the grammar.
  - Step 8: The resulting grammar is in GNF.