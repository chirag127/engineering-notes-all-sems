### Properties of lattices – Bounded

- A lattice is a poset (L, ⪯) for which every pair of elements has a greatest lower bound and least upper bound.
- A bounded lattice is a lattice that additionally has a greatest element (also called maximum, or top element, and denoted by 1, or by ⊤) and a least element (also called minimum, or bottom, and denoted by 0, or by ⊥), which satisfy:
  - for all x in L, x ∧ 1 = x and x ∨ 1 = 1
  - for all x in L, x ∧ 0 = 0 and x ∨ 0 = x
- The element 1 is called the upper bound, or top of L and the element 0 is called the lower bound or bottom of L.
- A complemented lattice is a bounded lattice in which every element is complemented. Namely, the complement of 1 is 0, and the complement of 0 is 1.
- A distributive lattice is a lattice in which for all elements in the poset the distributive property holds:
  - x ∧ (y ∨ z) = (x ∧ y) ∨ (x ∧ z)
  - x ∨ (y ∧ z) = (x ∨ y) ∧ (x ∨ z)
- Every finite lattice L = {a 1,a 2,a 3....a n} is bounded. Proof:
  - Let L = {a 1,a 2,a 3....a n} be a finite lattice.
  - Consider the element a 1 ∨ a 2 ∨ a 3....∨ a n. This element belongs to L, since L is closed under ∨.
  - For any element a i in L, we have a i ∨ (a 1 ∨ a 2 ∨ a 3....∨ a n) = a 1 ∨ a 2 ∨ a 3....∨ a n, by the idempotent law of ∨.
  - Therefore, a 1 ∨ a 2 ∨ a 3....∨ a n is the greatest element of L, and we denote it by 1.
  - Similarly, consider the element a 1 ∧ a 2 ∧ a 3....∧ a n. This element belongs to L, since L is closed under ∧.
  - For any element a i in L, we have a i ∧ (a 1 ∧ a 2 ∧ a 3....∧ a n) = a 1 ∧ a 2 ∧ a 3....∧ a n, by the idempotent law of ∧.
  - Therefore, a 1 ∧ a 2 ∧ a 3....∧ a n is the least element of L, and we denote it by 0.
  - Hence, L is a bounded lattice.