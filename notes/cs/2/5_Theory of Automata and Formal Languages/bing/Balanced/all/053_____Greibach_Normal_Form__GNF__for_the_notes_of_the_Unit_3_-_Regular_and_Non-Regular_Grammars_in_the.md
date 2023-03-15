# Greibach Normal Form (GNF)

- Greibach Normal Form (GNF) is a special form of context-free grammar (CFG) that has some restrictions on the right-hand side of the production rules.
- A CFG is in GNF if and only if all of its production rules are of the form: A → aA1A2...An, where A, A1, A2, ..., An are non-terminal symbols and a is a terminal symbol .
- GNF is useful for parsing algorithms, such as the top-down parsing algorithm, that require the first symbol of the right-hand side to be a terminal symbol .
- Any CFG can be converted into an equivalent GNF using a systematic algorithm that involves the following steps :
  - Step 1: If the start symbol S occurs on some right side, create a new start symbol S' and a new production S' → S.
  - Step 2: Remove null productions (productions of the form A → ε) using the null production removal algorithm.
  - Step 3: Remove unit productions (productions of the form A → B) using the unit production removal algorithm.
  - Step 4: Eliminate left recursion (direct or indirect) using the left recursion elimination algorithm.
  - Step 5: For each production of the form A → u1 | u2 | ... | un, where ui are strings of terminals and non-terminals, do the following:
    - If ui starts with a terminal symbol, say ai, then replace ui with aiBi, where Bi is a new non-terminal symbol, and add a new production Bi → ui / ai.
    - If ui starts with a non-terminal symbol, say Aj, then replace ui with the right-hand side of Aj, and repeat this process until ui starts with a terminal symbol.
  - Step 6: Simplify the grammar by removing any useless symbols or productions.