# Constructing LALR parsing tables

- LALR stands for lookahead LR, which is a type of bottom-up parser that can handle a large class of grammars.
- LALR parsing tables are used to guide the parsing process and determine the actions to be taken at each step.
- LALR parsing tables are constructed from the canonical collection of LR(1) items, which are pairs of production rules and lookahead symbols.
- LR(1) items represent the possible states of the parser and the expected input symbols.
- To construct the LALR parsing table, the following steps are followed:

  1. Find the canonical collection of LR(1) items by applying the closure and goto operations on the augmented grammar.
  2. Merge the LR(1) items that have the same production rule but different lookahead symbols into a single set of items. This reduces the number of states and the size of the table.
  3. Label each set of items with a unique state number and assign a start state to the set that contains the augmented production rule.
  4. For each state and terminal symbol, determine the action to be taken by the parser. The action can be one of the following:
    - Shift: move the input symbol to the stack and advance to the next state.
    - Reduce: pop the symbols from the stack that match the right-hand side of a production rule and push the left-hand side symbol to the stack. The next state is determined by the goto table.
    - Accept: terminate the parsing process successfully.
    - Error: report a syntax error and try to recover.
  5. For each state and non-terminal symbol, determine the next state to be reached by the parser. This is the goto table.
  6. Fill the entries of the parsing table with the actions and the goto values. If there is more than one entry for a given state and symbol, the grammar is not LALR and a conflict occurs.