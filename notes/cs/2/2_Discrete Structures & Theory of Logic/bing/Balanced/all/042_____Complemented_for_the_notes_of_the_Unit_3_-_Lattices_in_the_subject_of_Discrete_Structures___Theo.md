# Complemented for the notes of the Unit 3 - Lattices in the subject of Discrete Structures & Theory of Logic

- A **lattice** is a partially ordered set (poset) in which every pair of elements has a unique least upper bound (called the **join**) and a unique greatest lower bound (called the **meet**).
- A lattice can be represented by a **Hasse diagram**, which is a graph that shows the elements of the poset and the partial order relation between them.
- A lattice is also an **algebraic structure** with two binary operations, denoted by ∨ (join) and ∧ (meet), that satisfy the following properties for any elements a, b, and c in the lattice:
  - **Commutativity**: a ∨ b = b ∨ a and a ∧ b = b ∧ a
  - **Associativity**: a ∨ (b ∨ c) = (a ∨ b) ∨ c and a ∧ (b ∧ c) = (a ∧ b) ∧ c
  - **Idempotence**: a ∨ a = a and a ∧ a = a
  - **Absorption**: a ∨ (a ∧ b) = a and a ∧ (a ∨ b) = a
- A lattice is **bounded** if it has a least element (called the **bottom** or **zero**) and a greatest element (called the **top** or **one**). The bottom and top elements are denoted by 0 and 1, respectively.
- A lattice is **distributive** if it satisfies the following additional property for any elements a, b, and c in the lattice:
  - **Distributivity**: a ∨ (b ∧ c) = (a ∨ b) ∧ (a ∨ c) and a ∧ (b ∨ c) = (a ∧ b) ∨ (a ∧ c)
- A lattice is **complemented** if every element has a **complement**, which is an element that satisfies the following property for any element a in the lattice:
  - **Complementation**: a ∨ a' = 1 and a ∧ a' = 0, where a' is the complement of a
- A complemented lattice is **uniquely complemented** if every element has a **unique** complement.
- A complemented lattice is **orthocomplemented** if it satisfies the following additional property for any elements a and b in the lattice:
  - **Orthogonality**: If a ≤ b, then b' ≤ a', where a' and b' are the complements of a and b, respectively
- A lattice is **modular** if it satisfies the following weaker form of distributivity for any elements a, b, and c in the lattice:
  - **Modularity**: If a ≤ c, then a ∨ (b ∧ c) = (a ∨ b) ∧ c
- A lattice is **Boolean** if it is bounded, distributive, and complemented. A Boolean lattice is also uniquely complemented and orthocomplemented. A Boolean lattice is isomorphic to the power set of a finite set, with the join and meet operations corresponding to the union and intersection of sets, respectively.