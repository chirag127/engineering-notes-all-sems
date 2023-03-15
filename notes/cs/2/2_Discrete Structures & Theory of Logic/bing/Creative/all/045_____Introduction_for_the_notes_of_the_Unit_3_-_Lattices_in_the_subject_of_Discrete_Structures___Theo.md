# Introduction for the notes of the Unit 3 - Lattices in the subject of Discrete Structures & Theory of Logic

- A **lattice** is a partially ordered set (poset) in which every pair of elements has a unique least upper bound (lub) and a unique greatest lower bound (glb).
- A **least upper bound** of a pair of elements x and y is an element z such that x ≤ z and y ≤ z, and there is no other element w that is smaller than z and satisfies x ≤ w and y ≤ w.
- A **greatest lower bound** of a pair of elements x and y is an element z such that z ≤ x and z ≤ y, and there is no other element w that is larger than z and satisfies w ≤ x and w ≤ y.
- The least upper bound of x and y is also called the **join** of x and y, denoted by x ∨ y.
- The greatest lower bound of x and y is also called the **meet** of x and y, denoted by x ∧ y.
- A lattice can be represented by a **Hasse diagram**, which is a graphical representation of the partial order relation. In a Hasse diagram, each element is represented by a node, and there is an edge from x to y if and only if x < y and there is no element z such that x < z < y. The edges are drawn so that the higher nodes are above the lower nodes.
- A lattice is said to be **bounded** if it has a least element and a greatest element. The least element is denoted by 0 and the greatest element by 1. A bounded lattice is also called a **complete lattice**.
- A lattice is said to be **distributive** if it satisfies the following two distributive laws for all elements x, y, and z:

  - x ∨ (y ∧ z) = (x ∨ y) ∧ (x ∨ z)
  - x ∧ (y ∨ z) = (x ∧ y) ∨ (x ∧ z)

- A lattice is said to be **complemented** if every element has a **complement**, which is an element y such that x ∨ y = 1 and x ∧ y = 0. A complemented lattice is also called a **Boolean algebra**.