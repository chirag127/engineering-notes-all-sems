# The Canonical Collection of LR(0) Items

- An **LR(0) item** is a production of a grammar G with a dot at some position on the right side of the production .
- The dot indicates how much of the input has been scanned up to a given point in the process of parsing.
- For example, the production `S -> XYZ` yields four items: `S -> .XYZ`, `S -> X.YZ`, `S -> XY.Z`, `S -> XYZ.`.
- A **canonical collection of LR(0) items** is a set of sets of LR(0) items that is used to construct the SLR functions closure and goto.
- The canonical collection of LR(0) items for a grammar G is obtained by the following algorithm :

  - Start with the augmented grammar G' that has a new start symbol S' and a production S' -> S.
  - Compute the closure of the set containing the item S' -> .S and add it to the collection as I0.
  - For each set of items I in the collection and each grammar symbol X, compute the goto of I on X and add it to the collection if it is not empty and not already present.
  - Repeat the previous step until no new sets of items can be added to the collection.

- The **closure** of a set of items I is the set of items that can be derived from I by adding items that have the dot before a nonterminal and expanding that nonterminal with its productions .
- For example, if I contains the item `A -> a.Bc` and B has the productions `B -> b` and `B -> d`, then the closure of I will also contain the items `B -> .b` and `B -> .d`.
- The **goto** of a set of items I on a symbol X is the set of items that can be obtained by moving the dot one position to the right in the items of I that have the dot before X .
- For example, if I contains the items `A -> a.Bc` and `B -> .b`, then the goto of I on B will contain the items `A -> aB.c` and `B -> b.`.
- The canonical collection of LR(0) items can be represented by a **DFA** where each state corresponds to a set of items and each transition corresponds to a goto operation on a grammar symbol .
- The DFA can be used to construct the **SLR parsing table** by assigning actions to each state and symbol pair based on the items in the state .
- The actions can be shift, reduce, accept, or error, depending on whether the item has the dot at the end, the beginning, or in the middle of the right side, or if there is no item for the symbol .
- A grammar is **SLR** if its canonical collection of LR(0) items has no conflicts, that is, no state has more than one action for the same symbol .
- A grammar is **LR(0)** if it is SLR and it has no epsilon productions, that is, no productions with an empty right side.