### Constructing Canonical LR Parsing Tables

- A Canonical LR (CLR) parser is a type of bottom-up parser that can handle any context-free grammar that is LR(1), meaning that it can be parsed by looking at the rightmost derivation of the input and using one symbol of lookahead.
- A CLR parsing table is a table used by a CLR parser to determine its parsing actions based on the current state and the next input symbol. The table has two parts: an action part and a goto part. The action part specifies what the parser should do (shift, reduce, accept, or error) for each state and terminal symbol pair. The goto part specifies the next state for each state and nonterminal symbol pair.
- To construct a CLR parsing table, the following steps are required:

  1. Construct the canonical collection of LR(1) items for the given grammar. An LR(1) item is a pair of a production and a lookahead symbol, denoting that the parser expects to see the production followed by the lookahead symbol. The canonical collection is the set of all possible LR(1) items, grouped into sets of items that share the same core (the production without the lookahead symbol). The sets are connected by transitions based on the symbols that follow the dot in the items.
  2. Number the sets of items from 0 to n, where n is the total number of sets. These numbers will be the states of the parser.
  3. For each set of items and each terminal symbol, determine the action of the parser as follows:
     - If the set contains an item of the form A -> α.aβ, a, where a is the terminal symbol, then the action is to shift and go to the state that corresponds to the set of items obtained by moving the dot past a in the item. This is denoted by Sj, where j is the state number.
     - If the set contains an item of the form A -> α., a, where a is the terminal symbol, then the action is to reduce by the production A -> α. This is denoted by Rk, where k is the production number.
     - If the set contains an item of the form S' -> S., $, where $ is the end-of-input marker, then the action is to accept the input. This is denoted by acc.
     - If none of the above cases apply, then the action is to report an error. This is denoted by blank or err.
  4. For each set of items and each nonterminal symbol, determine the goto of the parser as follows:
     - If the set contains an item of the form A -> α.Bβ, b, where B is the nonterminal symbol, then the goto is the state that corresponds to the set of items obtained by moving the dot past B in the item. This is denoted by the state number.
     - If none of the above cases apply, then the goto is undefined. This is denoted by blank or err.

- An example of constructing a CLR parsing table for the grammar:

  S' -> S

  S -> CC

  C -> cC | d

  is shown below:

  | Set of items | State | c | d | $ | S | C |
  |--------------|-------|---|---|---|---|---|
  | S' -> .S, $  | 0     |   |   |   | 1 |   |
  | S -> .CC, $  |       |   |   |   |   | 2 |
  | C -> .cC, $  |       | S3|   |   |   |   |
  | C -> .d, $   |       |   | S4|   |   |   |
  | S' -> S., $  | 1     |   |   |acc|   |   |
  | S -> C.C, $  | 2     |   |   |   |   | 5 |
  | C -> .cC, $  |       | S3|   |   |   |   |
  | C -> .d, $   |       |   | S4|   |   |   |
  | C -> c.C, $  | 3     |   |   |   |   | 6 |
  | C -> .cC, $  |       | S3|   |   |   |   |
  | C -> .d, $   |       |   |