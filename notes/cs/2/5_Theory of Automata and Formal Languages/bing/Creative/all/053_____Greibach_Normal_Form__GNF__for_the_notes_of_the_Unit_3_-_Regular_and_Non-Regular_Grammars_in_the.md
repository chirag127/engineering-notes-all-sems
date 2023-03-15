# Greibach Normal Form (GNF)

- Greibach Normal Form (GNF) is a special form of context-free grammar (CFG) that has some restrictions on the right-hand side of the production rules.
- A CFG is in GNF if and only if all of its production rules are of the form: `A → aA1A2...An`, where `A, A1, A2, ..., An` are non-terminal symbols and `a` is a terminal symbol .
- GNF is useful for parsing algorithms, such as the top-down parsing algorithm, that require the first symbol of the right-hand side to be a terminal .
- GNF can also be used to prove that every context-free language can be accepted by a pushdown automaton.
- Every CFG can be converted to an equivalent GNF using a systematic algorithm . The algorithm consists of the following steps:
  - Step 1: If the start symbol `S` occurs on some right side, create a new start symbol `S'` and a new production `S' → S`.
  - Step 2: Remove null productions (productions of the form `A → ε`, where `ε` is the empty word) using the null production removal algorithm.
  - Step 3: Remove unit productions (productions of the form `A → B`, where `A` and `B` are non-terminal symbols) using the unit production removal algorithm.
  - Step 4: Eliminate terminals that are not at the beginning of the right-hand side using the following procedure:
    - For each production of the form `A → u1u2...un`, where `ui` is either a terminal or a non-terminal symbol, do the following:
      - If `u1` is a terminal, then leave the production unchanged.
      - If `u1` is a non-terminal, say `B`, then replace the production with `A → v1Av2...Avn`, where `v1, v2, ..., vn` are the first symbols of the right-hand sides of the productions for `B`.
  - Step 5: Eliminate non-terminals that are not at the end of the right-hand side using the following procedure:
    - For each production of the form `A → aB1B2...Bn`, where `a` is a terminal and `Bi` are non-terminal symbols, do the following:
      - If `n = 0` or `n = 1`, then leave the production unchanged.
      - If `n > 1`, then replace the production with `A → aB1C`, where `C` is a new non-terminal symbol, and add a new production `C → B2B3...Bn`.
- The algorithm terminates when no more changes can be made to the grammar, and the resulting grammar is in GNF.