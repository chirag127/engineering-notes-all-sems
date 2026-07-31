### Properties of lattices – Bounded

- A lattice is a poset (L, ⪯) for which every pair of elements has a greatest lower bound and least upper bound.
- A bounded lattice is a lattice that additionally has a greatest element (also called maximum, or top element, and denoted by 1, or by ⊤) and a least element (also called minimum, or bottom, denoted by 0 or by ⊥), which satisfy:
  - for all x in L, x ∧ 1 = x and x ∨ 1 = 1
  - for all x in L, x ∧ 0 = 0 and x ∨ 0 = x
- The element 1 is called the upper bound, or top of L and the element 0 is called the lower bound or bottom of L.
- A bounded lattice is also called a complemented lattice if every element has a complement, that is, an element y such that x ∧ y = 0 and x ∨ y = 1.
- A bounded lattice is also called a distributive lattice if for all elements in the poset the distributive property holds, that is, x ∧ (y ∨ z) = (x ∧ y) ∨ (x ∧ z) and x ∨ (y ∧ z) = (x ∨ y) ∧ (x ∨ z).
- Every finite lattice is bounded, since the least upper bound of all elements is the greatest element and the greatest lower bound of all elements is the least element .
- An example of a bounded lattice is the power set of a finite set, ordered by inclusion, with the empty set as the least element and the whole set as the greatest element.