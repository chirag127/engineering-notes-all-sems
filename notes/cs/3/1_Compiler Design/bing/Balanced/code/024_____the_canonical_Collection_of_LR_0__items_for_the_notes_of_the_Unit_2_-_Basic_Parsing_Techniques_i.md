# The canonical collection of LR(0) items

- An LR(0) item is a production of a grammar G with a dot at some position on the right side of the production .
- The dot indicates how much of the input has been scanned up to a given point in the process of parsing.
- For example, the production S -> XYZ yields four items:
  - S -> .XYZ
  - S -> X.YZ
  - S -> XY.Z
  - S -> XYZ.
- A collection of sets of LR(0) items is called a canonical collection of LR(0) items.
- The canonical collection of LR(0) items is used to construct the SLR functions closure and goto, which in turn are used to construct the SLR parsing table.
- The closure function computes the set of LR(0) items that are valid for a given grammar symbol.
- The goto function computes the set of LR(0) items that are valid after seeing a given input symbol.
- The algorithm to construct the canonical collection of LR(0) items for a grammar G is as follows:
  - Start with the augmented grammar G' with a new start symbol S' defined by S' -> S.
  - Compute the closure of the set containing the item S' -> .S and call it I0.
  - For each set of items I and each grammar symbol X, compute the goto of I on X and call it I1, I2, ..., In.
  - If any of the sets I1, I2, ..., In is not already in the collection, add it and repeat the process for the new sets.
  - The collection of sets of items obtained at the end is the canonical collection of LR(0) items for G.
- For example, consider the following grammar G:
  - S -> AA
  - A -> aA | b
- The augmented grammar G' is:
  - S' -> S
  - S -> AA
  - A -> aA | b
- The canonical collection of LR(0) items for G is:
  - I0: S' -> .S, S -> .AA, A -> .aA, A -> .b
  - I1: S' -> S., S -> A.A, A -> .aA, A -> .b
  - I2: S -> AA., A -> a.A, A -> aA.
  - I3: A -> b.
  - I4: A -> aA.
- The following diagram shows the transitions between the sets of items using the goto function:

![LR(0) items diagram](https://www.i2tutorials.com/wp-content/uploads/2019/05/Compiler-Design-Canonical-collection-of-LR0-items-i2tutorials.jpg)