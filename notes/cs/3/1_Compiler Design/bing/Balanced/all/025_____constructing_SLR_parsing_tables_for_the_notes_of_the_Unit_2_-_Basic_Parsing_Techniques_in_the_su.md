# Constructing SLR Parsing Tables

- SLR stands for Simple LR, which is a type of LR parser with small parse tables and a relatively simple parser generator algorithm.
- SLR parsers can perform bottom-up parsing of input strings using one token of lookahead to resolve conflicts .
- SLR parsers can handle a subset of LR(1) grammars, which are grammars that can be parsed by LR parsers with one token of lookahead.
- SLR parsers are similar to LR(0) parsers, except that they use the FOLLOW sets of the non-terminals to determine when to reduce .
- The steps for constructing SLR parsing tables are:

  1. Write the augmented grammar, which is the original grammar with a new start symbol and a new production S' -> S, where S is the original start symbol.
  2. Find the LR(0) collection of items, which are sets of productions with a dot indicating the current position of the parser.
  3. Find the FOLLOW sets of the non-terminals, which are the sets of terminals that can appear immediately after the non-terminals in a derivation.
  4. Define two functions: GOTO and ACTION, which are the components of the parsing table.
     - GOTO is a function that maps a state and a symbol to a new state, indicating the transition of the parser after shifting the symbol.
     - ACTION is a function that maps a state and a terminal to an action, which can be shift, reduce, accept, or error.
  5. Fill the parsing table using the following rules:
     - For each item [A -> α.Bβ] in state I, set GOTO(I, B) to the state that contains the item [A -> αB.β] after the closure operation.
     - For each item [A -> α.] in state I, set ACTION(I, a) to reduce A -> α for all a in FOLLOW(A).
     - For each item [S' -> S.] in state I, set ACTION(I, $) to accept, where $ is the end-of-input marker.
     - For all other entries in the parsing table, set them to error.

- An example of constructing an SLR parsing table for the grammar S -> CC, C -> cC | d is given below:

  1. The augmented grammar is S' -> S, S -> CC, C -> cC | d.
  2. The LR(0) collection of items is:

     ```
     I0: [S' -> .S]
         [S -> .CC]
         [C -> .cC]
         [C -> .d]
     I1: [S' -> S.]
     I2: [S -> C.C]
         [C -> .cC]
         [C -> .d]
     I3: [C -> c.C]
         [C -> .cC]
         [C -> .d]
     I4: [C -> d.]
     I5: [S -> CC.]
     I6: [C -> cC.]
     ```

  3. The FOLLOW sets of the non-terminals are:

     ```
     FOLLOW(S') = {$}
     FOLLOW(S) = {$}
     FOLLOW(C) = {c, d, $}
     ```

  4. The GOTO and ACTION functions are:

     ```
     GOTO(I0, S) = I1
     GOTO(I0, C) = I2
     GOTO(I0, c) = I3
     GOTO(I0, d) = I4
     GOTO(I2, C) = I5
     GOTO(I2, c) = I3
     GOTO(I2, d) = I4
     GOTO(I3, C) = I6
     GOTO(I3, c) = I3
     GOTO(I3, d) = I4

     ACTION(I0, c) = shift
     ACTION(I0, d) = shift
     ACTION(I0, $) = error
     ACTION(I1, $) = accept
     ACTION(I2, c) = shift
     ACTION(I2, d) = shift
     ACTION(I