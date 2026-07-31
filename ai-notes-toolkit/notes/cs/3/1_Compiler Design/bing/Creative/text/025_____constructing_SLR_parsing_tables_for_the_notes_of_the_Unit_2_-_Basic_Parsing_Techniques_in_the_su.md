### Constructing SLR Parsing Tables

- SLR stands for Simple LR, which is a type of LR parser with small parse tables and a relatively simple parser generator algorithm.
- SLR parsers can perform bottom-up parsing of input strings using one token of lookahead to resolve conflicts .
- SLR parsers can handle a subset of LR(1) grammars, which are grammars that can be parsed by LR parsers with one token of lookahead.
- SLR parsers use the same LR(0) configurating sets and have the same table structure and parser operation as LR(0) parsers.
- The difference between SLR parsers and LR(0) parsers is that SLR parsers use the FOLLOW sets of the non-terminals to determine when to reduce .
- The steps for constructing the SLR parsing table are:
  - Write the augmented grammar by adding a new start symbol S' and a new production S' -> S, where S is the original start symbol.
  - Find the LR(0) collection of items by applying the closure and goto operations on the augmented grammar.
  - Find the FOLLOW sets of the non-terminals in the augmented grammar using the rules of FIRST and FOLLOW.
  - Define two functions: action and goto in the parsing table. The action function maps a state and a terminal symbol to a shift, reduce, accept or error action. The goto function maps a state and a non-terminal symbol to a new state or error.
  - For each state and terminal symbol pair, assign the action function as follows:
    - If the state contains an item [A -> α.aβ, a], where a is the terminal symbol, then assign action[state, a] = shift s, where s is the state obtained by applying goto(state, a).
    - If the state contains an item [A -> α., a], where A is not S' and a is in FOLLOW(A), then assign action[state, a] = reduce A -> α.
    - If the state contains an item [S' -> S., $], then assign action[state, $] = accept.
    - Otherwise, assign action[state, a] = error.
  - For each state and non-terminal symbol pair, assign the goto function as follows:
    - If the state contains an item [A -> α.Aβ, a], where A is the non-terminal symbol, then assign goto[state, A] = s, where s is the state obtained by applying goto(state, A).
    - Otherwise, assign goto[state, A] = error.