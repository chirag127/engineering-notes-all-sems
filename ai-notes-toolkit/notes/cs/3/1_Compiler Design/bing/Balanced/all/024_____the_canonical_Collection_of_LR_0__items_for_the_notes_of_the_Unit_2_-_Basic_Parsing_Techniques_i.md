# The canonical collection of LR(0) items

- An **LR(0) item** is a production of a grammar G with a dot at some position on the right side of the production .
- The dot indicates how much of the input has been scanned up to a given point in the process of parsing.
- For example, the production S -> XYZ yields four items:
  - S -> .XYZ
  - S -> X.YZ
  - S -> XY.Z
  - S -> XYZ.
- A **canonical collection of LR(0) items** is a set of sets of LR(0) items that is used to construct the SLR functions closure and goto.
- The canonical collection of LR(0) items for a grammar G is obtained by the following algorithm:
  - Start with the augmented grammar G' with a new start symbol S' and a production S' -> S.
  - Compute the closure of the set {S' -> .S} and call it I0. This is the initial state of the LR(0) automaton.
  - For each set of items I and each grammar symbol X, compute the goto function goto(I, X) and add it to the collection if it is not empty.
  - Repeat the previous step until no new sets of items are added to the collection.
- The canonical collection of LR(0) items can be represented by a DFA where each state is a set of items and each transition is labeled by a grammar symbol.
- The DFA can be used to construct the SLR parsing table by assigning actions to each state and symbol pair.
- The canonical collection of LR(0) items can be used to determine if a grammar is LR(0) or not. A grammar is LR(0) if and only if there is no state in the DFA that has a shift-reduce conflict or a reduce-reduce conflict.