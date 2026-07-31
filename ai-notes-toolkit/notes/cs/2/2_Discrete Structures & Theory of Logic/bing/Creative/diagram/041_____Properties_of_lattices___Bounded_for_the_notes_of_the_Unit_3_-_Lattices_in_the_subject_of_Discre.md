### Properties of lattices – Bounded

- A lattice is a poset (L, ⪯) for which every pair of elements has a greatest lower bound and least upper bound.
- A bounded lattice is a lattice that additionally has a greatest element (also called maximum, or top element, and denoted by 1, or by ⊤) and a least element (also called minimum, or bottom, denoted by 0 or by ⊥), which satisfy:
  - for all x in L, x ∧ 1 = x and x ∨ 1 = 1
  - for all x in L, x ∧ 0 = 0 and x ∨ 0 = x
- The element 1 is called the upper bound, or top of L and the element 0 is called the lower bound or bottom of L.
- A bounded lattice can be represented by a Hasse diagram with a top and a bottom element.
- Example: The set of all subsets of a finite set, ordered by inclusion, is a bounded lattice, where the empty set is the bottom element and the whole set is the top element.
- Properties of bounded lattices:
  - If L is a bounded lattice, then for any element a ∈ L, we have the following identities:
    - a ∨ 1 = 1
    - a ∧ 1 = a
    - a ∨ 0 = a
    - a ∧ 0 = 0
  - Every finite lattice L = {a 1,a 2,a 3....a n} is bounded, since the join of all elements is the top element and the meet of all elements is the bottom element.
  - A bounded lattice is complemented if every element has a complement, i.e., an element b such that a ∨ b = 1 and a ∧ b = 0.
  - A bounded lattice is distributive if it satisfies the distributive laws:
    - a ∨ (b ∧ c) = (a ∨ b) ∧ (a ∨ c)
    - a ∧ (b ∨ c) = (a ∧ b) ∨ (a ∧ c)
  - A bounded lattice is modular if it satisfies the modular law:
    - a ∨ (b ∧ c) = (a ∨ b) ∧ c, whenever a ⪯ c
- A Hasse diagram of a bounded lattice:

![Hasse diagram of a bounded lattice](https://mathworld.wolfram.com/images/eps-gif/BoundedLattice_1000.gif)