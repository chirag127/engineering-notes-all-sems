# Constructing SLR Parsing Tables

- SLR stands for Simple LR, which is a type of LR parser with small parse tables and a relatively simple parser generator algorithm.
- SLR parsers can perform bottom-up parsing of input strings using one token of lookahead to resolve conflicts.
- SLR parsers can handle a subset of LR(1) grammars, which are grammars that can be parsed by LR parsers with one token of lookahead.
- SLR parsers use the same LR(0) configurating sets and have the same table structure and parser operation as LR(0) parsers.
- The difference between SLR parsers and LR(0) parsers is that SLR parsers use the FOLLOW sets of the non-terminals to determine when to reduce.
- The steps for constructing the SLR parsing table are:
  - Write the augmented grammar, which is the original grammar with a new start symbol and a new production of the form S' -> S, where S is the original start symbol.
  - Find the LR(0) collection of items, which are sets of productions with a dot indicating the position of the parser in each production. Use the closure and goto functions to generate the items and the transitions between them.
  - Find the FOLLOW sets of the left-hand sides of the productions, which are the sets of terminals that can appear immediately after the non-terminals in the derivations.
  - Define two functions: action and goto, which are the entries of the parsing table. The action function maps a state and a terminal to a shift, reduce, accept, or error action. The goto function maps a state and a non-terminal to a new state or error.
  - Fill the action and goto functions using the following rules:
    - For each item [A -> α.aβ] in state i, where a is a terminal, set action[i, a] to shift j, where j is the state obtained by applying goto to state i and symbol a.
    - For each item [A -> α.] in state i, where A is not the start symbol, set action[i, a] to reduce A -> α for all a in FOLLOW(A).
    - For the item [S' -> S.] in state i, set action[i, $] to accept, where $ is the end-of-input marker.
    - For all other entries, set them to error.