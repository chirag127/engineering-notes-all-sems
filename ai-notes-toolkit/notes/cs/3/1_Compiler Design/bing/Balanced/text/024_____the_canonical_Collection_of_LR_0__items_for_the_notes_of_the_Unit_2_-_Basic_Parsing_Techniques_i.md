### The canonical collection of LR(0) items

- An **LR(0) item** is a production of a grammar G with a dot at some position on the right side of the production .
- The dot indicates how much of the input has been scanned up to a given point in the process of parsing.
- For example, the production `S -> XYZ` yields four items:

  - `S -> .XYZ`
  - `S -> X.YZ`
  - `S -> XY.Z`
  - `S -> XYZ.`

- A **canonical collection of LR(0) items** is a set of sets of LR(0) items that are obtained by applying two functions: **closure** and **goto** .
- The **closure** function takes a set of LR(0) items and adds all the items that can be derived from the given items by following the productions whose left side is the symbol after the dot .
- For example, if the grammar is:

  - `S' -> S`
  - `S -> AB`
  - `A -> aA | b`
  - `B -> c`

  Then the closure of the set `{S' -> .S}` is:

  - `S' -> .S`
  - `S -> .AB`
  - `A -> .aA`
  - `A -> .b`

- The **goto** function takes a set of LR(0) items and a grammar symbol, and returns a new set of LR(0) items that are obtained by moving the dot over the given symbol in the original set .
- For example, using the same grammar as above, the goto of the set `{S' -> .S}` and the symbol `S` is:

  - `S' -> S.`

- The canonical collection of LR(0) items is constructed by starting with the closure of the item `S' -> .S`, where `S'` is a new start symbol, and then applying the goto function recursively on all the symbols that appear after the dot in any item .
- The canonical collection of LR(0) items is used to construct a **DFA** that recognizes the viable prefixes of the grammar, which are the prefixes of right sentential forms that can appear on the stack of a shift-reduce parser .
- The canonical collection of LR(0) items also determines the **action** and **goto** tables of an **LR(0) parser**, which is a bottom-up parser that uses the DFA to decide whether to shift or reduce at each step .
- A grammar is **LR(0)** if the canonical collection of LR(0) items does not contain any **conflicts**, which are situations where the parser has more than one possible action for a given state and input symbol .
- No grammar with **epsilon productions** can be LR(0), because the presence of epsilon productions leads to reduce-reduce conflicts.