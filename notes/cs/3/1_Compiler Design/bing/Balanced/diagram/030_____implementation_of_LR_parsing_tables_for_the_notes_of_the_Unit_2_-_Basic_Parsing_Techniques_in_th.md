### Implementation of LR Parsing Tables

LR parsing tables are a two-dimensional array in which each entry represents an action or a goto entry. LR parsing tables are used to guide the LR parser in recognizing the input string and applying the appropriate grammar rules. LR parsing tables consist of two parts: the action part and the goto part.

- The action part has columns for lookahead terminal symbols and rows for parser states. The action part specifies what the parser should do when it encounters a terminal symbol in the input buffer, depending on the current state of the parser. The possible actions are:

  - Shift: The parser shifts the terminal symbol from the input buffer to the top of the stack and transitions to a new state.
  - Reduce: The parser reduces the top symbols of the stack by applying a grammar rule and replacing them with the left-hand side symbol of the rule. The parser then consults the goto part to determine the next state.
  - Accept: The parser accepts the input string as valid and terminates the parsing process.
  - Error: The parser reports a syntax error and rejects the input string as invalid.

- The goto part has columns for nonterminal symbols and rows for parser states. The goto part specifies what the next state of the parser should be after a reduction action, depending on the current state of the parser and the nonterminal symbol that was produced by the reduction.

LR parsing tables can be constructed in different ways, depending on the type of LR parser. Some common types of LR parsers are:

- LR(0) parser: This parser uses LR(0) items, which are grammar rules with a dot indicating the position of the parser in the rule. The parser does not use any lookahead information to decide the action. LR(0) parsing tables can be constructed by finding the closure and the goto of each set of LR(0) items and assigning actions based on the following rules:

  - If [A → α•aβ] is an item in state Ii and goto(Ii, a) = Ij, then action[i, a] = shift j.
  - If [A → α•] is an item in state Ii, then action[i, a] = reduce A → α for all a in the follow set of A.
  - If [S' → S•] is an item in state Ii, then action[i, $] = accept.
  - Otherwise, action[i, a] = error.

- SLR(1) parser: This parser uses LR(0) items, but uses the follow sets of the grammar symbols to resolve shift-reduce and reduce-reduce conflicts. SLR(1) parsing tables can be constructed by finding the closure and the goto of each set of LR(0) items and assigning actions based on the following rules:

  - If [A → α•aβ] is an item in state Ii and goto(Ii, a) = Ij, then action[i, a] = shift j.
  - If [A → α•] is an item in state Ii, then action[i, a] = reduce A → α for all a in the follow set of A, except if action[i, a] is already defined as shift.
  - If [S' → S•] is an item in state Ii, then action[i, $] = accept.
  - Otherwise, action[i, a] = error.

- LR(1) parser: This parser uses LR(1) items, which are grammar rules with a dot and a lookahead terminal symbol indicating the position and the expectation of the parser in the rule. The parser uses the lookahead information to decide the action. LR(1) parsing tables can be constructed by finding the closure and the goto of each set of LR(1) items and assigning actions based on the following rules:

  - If [A → α•aβ, b] is an item in state Ii and goto(Ii, a) = Ij, then action[i, a] = shift j.
  - If [A → α•, a] is an item in state Ii, then action[i, a] = reduce A → α.
  - If [S' → S•, $] is an item in state Ii, then action[i, $] = accept.
  - Otherwise, action[i, a] = error.

- LALR(1) parser: This parser uses LR(1) items, but merges states that have the same LR(0) core