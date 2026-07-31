# Properties of lattices – Bounded

- A lattice is a poset (L, ⪯) for which every pair of elements has a greatest lower bound and least upper bound.
- A bounded lattice is a lattice that additionally has a greatest element (also called maximum, or top element, and denoted by 1, or by ⊤) and a least element (also called minimum, or bottom, and denoted by 0, or by ⊥), which satisfy:
  - for all x in L, x ∧ 1 = x and x ∨ 1 = 1
  - for all x in L, x ∧ 0 = 0 and x ∨ 0 = x
- The element 1 is called the upper bound, or top of L and the element 0 is called the lower bound or bottom of L.
- A bounded lattice is also called a complete lattice, since it has a least upper bound and a greatest lower bound for any subset of L.
- A complemented lattice is a bounded lattice in which every element is complemented. Namely, the complement of 1 is 0, and the complement of 0 is 1.
- A distributive lattice is a lattice in which for all elements in the poset the distributive property holds:
  - x ∧ (y ∨ z) = (x ∧ y) ∨ (x ∧ z)
  - x ∨ (y ∧ z) = (x ∨ y) ∧ (x ∨ z)
- Every finite lattice L = {a 1,a 2,a 3....a n} is bounded. This can be proved by taking the least upper bound and the greatest lower bound of all the elements in L.