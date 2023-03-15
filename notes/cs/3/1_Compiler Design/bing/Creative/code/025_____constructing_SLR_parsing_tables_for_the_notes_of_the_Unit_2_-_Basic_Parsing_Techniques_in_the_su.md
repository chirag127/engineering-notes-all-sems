### Constructing SLR Parsing Tables

- SLR stands for Simple LR, which is a type of LR parser with small parse tables and a relatively simple parser generator algorithm.
- SLR parsers can perform bottom-up parsing of input strings using one token of lookahead to resolve conflicts .
- SLR parsers can handle a subset of LR(1) grammars, which are grammars that can be parsed by LR parsers with one token of lookahead.
- SLR parsers are similar to LR(0) parsers, except that they use the FOLLOW sets of the non-terminals to determine when to reduce .
- The steps for constructing SLR parsing tables are:

  1. Write the augmented grammar, which is the original grammar with a new start symbol and a new production of the form S' -> S, where S is the original start symbol.
  2. Find the LR(0) collection of items, which are sets of productions with a dot indicating the current position of the parser.
  3. Find the FOLLOW sets of the non-terminals, which are sets of terminals that can appear immediately after the non-terminals in a derivation.
  4. Define two functions: GOTO and ACTION, which are used to fill the parsing table.
     - GOTO is a function that takes a state and a symbol and returns the next state after shifting the symbol.
     - ACTION is a function that takes a state and a terminal and returns one of the following actions:
       - SHIFT s, which means to shift the terminal and go to state s.
       - REDUCE A -> B, which means to reduce by the production A -> B and go to the state given by GOTO of the previous state and A.
       - ACCEPT, which means to accept the input as valid.
       - ERROR, which means to report an error and reject the input.
  5. Fill the parsing table using the following rules:
     - For each state i and terminal a, if GOTO(i, a) = j, then ACTION(i, a) = SHIFT j.
     - For each state i and production A -> B with a dot at the end, if b is in FOLLOW(A), then ACTION(i, b) = REDUCE A -> B.
     - For the state containing S' -> S., ACTION(i, $) = ACCEPT, where $ is the end-of-input marker.
     - For any other entry, ACTION(i, a) = ERROR.

- An example of constructing SLR parsing table for the grammar:

  ```
  S -> CC
  C -> cC | d
  ```

  is given below:

  1. The augmented grammar is:

     ```
     S' -> S
     S -> CC
     C -> cC | d
     ```

  2. The LR(0) collection of items is:

     ```
     I0: S' -> .S
         S -> .CC
     I1: S' -> S.
     I2: S -> C.C
         C -> .cC
         C -> .d
     I3: S -> CC.
     I4: C -> c.C
         C -> .cC
         C -> .d
     I5: C -> d.
     I6: C -> cC.
     ```

  3. The FOLLOW sets of the non-terminals are:

     ```
     FOLLOW(S') = {$}
     FOLLOW(S) = {$}
     FOLLOW(C) = {c, d, $}
     ```

  4. The GOTO and ACTION functions are:

     ```
     GOTO(0, S) = 1
     GOTO(0, C) = 2
     GOTO(2, C) = 3
     GOTO(2, c) = 4
     GOTO(2, d) = 5
     GOTO(4, C) = 6
     GOTO(4, c) = 4
     GOTO(4, d) = 5

     ACTION(0, c) = SHIFT 4
     ACTION(0, d) = SHIFT 5
     ACTION(1, $) = ACCEPT
     ACTION(2