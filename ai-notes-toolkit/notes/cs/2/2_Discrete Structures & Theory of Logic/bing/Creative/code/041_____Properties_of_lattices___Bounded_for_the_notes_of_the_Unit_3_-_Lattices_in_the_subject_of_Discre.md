### Properties of lattices – Bounded

- A lattice is a partially ordered set (poset) in which every pair of elements has a least upper bound (called join or supremum) and a greatest lower bound (called meet or infimum).
- A bounded lattice is a lattice that has a greatest element (called maximum or top) and a least element (called minimum or bottom), which satisfy the following properties for any element x in the lattice:
  - x ∨ 1 = 1
  - x ∧ 1 = x
  - x ∨ 0 = x
  - x ∧ 0 = 0
- The greatest element 1 is the least upper bound of the whole lattice, and the least element 0 is the greatest lower bound of the whole lattice.
- Every finite lattice is bounded, since the join of all the elements is the maximum and the meet of all the elements is the minimum .
- A bounded lattice can be represented by a Hasse diagram, which is a graphical representation of the partial order relation. The maximum element is at the top and the minimum element is at the bottom of the diagram.
- An example of a bounded lattice is the power set of a finite set, ordered by inclusion. The maximum element is the whole set and the minimum element is the empty set.

- Here is a Hasse diagram of the power set of {a, b} as a bounded lattice:

```
  {a, b}
 /      \
{a}    {b}
 \      /
  { } 
```