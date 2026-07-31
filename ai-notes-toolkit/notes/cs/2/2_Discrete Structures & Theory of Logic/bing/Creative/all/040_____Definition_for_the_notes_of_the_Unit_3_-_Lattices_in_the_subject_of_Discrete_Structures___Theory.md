# Definition for the notes of the Unit 3 - Lattices in the subject of Discrete Structures & Theory of Logic

- A **lattice** is a partially ordered set (poset) in which every pair of elements has a **greatest lower bound** and a **least upper bound** .
- A greatest lower bound of two elements a and b in a poset is an element c such that c ≤ a and c ≤ b, and there is no other element d that is lower than c and also satisfies d ≤ a and d ≤ b. It is denoted by a ∧ b or glb(a, b).
- A least upper bound of two elements a and b in a poset is an element c such that a ≤ c and b ≤ c, and there is no other element d that is higher than c and also satisfies a ≤ d and b ≤ d. It is denoted by a ∨ b or lub(a, b).
- The greatest lower bound and the least upper bound of two elements in a lattice are also called the **meet** and the **join** of the elements, respectively.
- The meet and the join of two elements in a lattice are **unique**, if they exist.
- A lattice can be represented by a **Hasse diagram**, which is a graphical representation of the partial order relation. In a Hasse diagram, the elements of the lattice are represented by points, and the partial order relation is represented by lines connecting the points. The lines are drawn such that if a ≤ b, then a is below b, and there is no other element c between a and b such that a ≤ c ≤ b.
- A lattice can also be defined as an **algebraic structure** with two binary operations, called meet and join, that satisfy certain properties. A lattice is denoted by [L; ∧, ∨], where L is the set of elements and ∧ and ∨ are the meet and join operations.
- The properties of the meet and join operations in a lattice are:

  - **Commutativity**: a ∧ b = b ∧ a and a ∨ b = b ∨ a for all a, b ∈ L.
  - **Associativity**: a ∧ (b ∧ c) = (a ∧ b) ∧ c and a ∨ (b ∨ c) = (a ∨ b) ∨ c for all a, b, c ∈ L.
  - **Idempotency**: a ∧ a = a and a ∨ a = a for all a ∈ L.
  - **Absorption**: a ∧ (a ∨ b) = a and a ∨ (a ∧ b) = a for all a, b ∈ L.
  - **Distributivity**: a ∧ (b ∨ c) = (a ∧ b) ∨ (a ∧ c) and a ∨ (b ∧ c) = (a ∨ b) ∧ (a ∨ c) for all a, b, c ∈ L.

- A lattice is called a **distributive lattice** if it satisfies the distributivity property, and a **non-distributive lattice** otherwise.
- A lattice is called a **bounded lattice** if it has a **greatest element** and a **least element**. A greatest element of a lattice is an element that is greater than or equal to every other element in the lattice. A least element of a lattice is an element that is less than or equal to every other element in the lattice. A greatest element is denoted by 1 or T, and a least element is denoted by 0 or F.
- A lattice is called a **complete lattice** if every subset of the lattice has a greatest lower bound and a least upper bound. A complete lattice is always a bounded lattice, since the greatest lower bound of the empty set is the greatest element, and the least upper bound of the empty set is the least element.
- A lattice is called a **modular lattice** if it satisfies the following property: a ≤ c implies a ∨ (b ∧ c) = (a ∨ b) ∧ c for all a, b, c ∈ L. A modular lattice is always a distributive lattice, but the converse is not true.
- A lattice is called a **complemented lattice** if every element in the lattice has a **complement**. A complement of an element a