### Properties of lattices – Bounded

- A lattice is a poset (L, ⪯) for which every pair of elements has a greatest lower bound and least upper bound.
- A bounded lattice is a lattice that additionally has a greatest element (also called maximum, or top element, and denoted by 1, or by ⊤) and a least element (also called minimum, or bottom, denoted by 0 or by ⊥), which satisfy:
  - 1 ⪯ x and x ⪯ 1 for all x in L
  - 0 ⪯ x and x ⪯ 0 for all x in L
- If L is a bounded lattice, then for any element a ∈ L, we have the following identities:
  - a ∨ 1 = 1
  - a ∧ 1 = a
  - a ∨ 0 = a
  - a ∧ 0 = 0
- Every finite lattice L = {a 1,a 2,a 3....a n} is bounded. This can be proved by taking the join of all the elements in L, which will be the greatest element, and the meet of all the elements in L, which will be the least element.
- A bounded lattice can be represented by a Hasse diagram, where the top element is drawn at the top and the bottom element is drawn at the bottom. For example, the following is a bounded lattice with five elements:

![Hasse diagram of a bounded lattice](https://mathworld.wolfram.com/images/eps-gif/BoundedLattice_1000.gif)