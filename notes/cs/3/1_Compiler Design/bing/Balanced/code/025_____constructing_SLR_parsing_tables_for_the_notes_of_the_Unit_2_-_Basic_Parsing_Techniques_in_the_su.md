### Constructing SLR Parsing Tables

- SLR stands for Simple LR, which is a type of LR parser with small parse tables and a relatively simple parser generator algorithm.
- SLR parsers can perform bottom-up parsing of input strings using one token of lookahead to resolve conflicts .
- SLR parsers can handle a subset of LR(1) grammars, which are grammars that can be parsed by LR parsers with one token of lookahead.
- SLR parsers are similar to LR(0) parsers, except that they use the FOLLOW sets of the non-terminals to determine when to reduce.
- The steps for constructing SLR parsing tables are:

  1. Write the augmented grammar, which is the original grammar with a new start symbol and a new production of the form S' -> S, where S is the original start symbol.
  2. Find the LR(0) collection of items, which are sets of productions with a dot indicating the current position of the parser.
  3. Construct the goto function, which maps a state and a symbol to a new state by moving the dot past the symbol in the items of the state.
  4. Construct the action function, which maps a state and a terminal to a shift, reduce, accept, or error action.
  5. Fill the SLR parsing table with the action and goto functions, using the FOLLOW sets of the non-terminals to determine the reduce actions.
  6. Use the SLR parsing table to parse the input string, following the actions and transitions indicated by the table.