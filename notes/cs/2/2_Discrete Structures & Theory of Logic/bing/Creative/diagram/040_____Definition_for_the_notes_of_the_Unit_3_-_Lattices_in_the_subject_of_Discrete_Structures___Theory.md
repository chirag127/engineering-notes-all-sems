### Definition for the notes of the Unit 3 - Lattices in the subject of Discrete Structures & Theory of Logic

- A **lattice** is a partially ordered set (poset) in which every pair of elements has a **greatest lower bound** and a **least upper bound**.
- A **greatest lower bound** of a pair of elements x and y in a poset is an element z such that z ≤ x and z ≤ y, and there is no other element w that satisfies w ≤ x, w ≤ y and w > z. It is also called the **meet** or the **infimum** of x and y, and denoted by x ∧ y.
- A **least upper bound** of a pair of elements x and y in a poset is an element z such that x ≤ z and y ≤ z, and there is no other element w that satisfies x ≤ w, y ≤ w and w < z. It is also called the **join** or the **supremum** of x and y, and denoted by x ∨ y.
- A lattice can be represented by a **Hasse diagram**, which is a graphical representation of the partial order relation. In a Hasse diagram, each element of the lattice is represented by a node, and a line is drawn between two nodes if and only if one element is the immediate predecessor or successor of the other.
- A lattice is an **algebraic system** with two binary operations, namely the meet and the join, which satisfy certain properties such as commutativity, associativity, idempotency, absorption and distributivity.
- A lattice can be classified into different types based on its properties, such as **bounded**, **complete**, **distributive**, **modular**, **complemented** and **Boolean** lattices.
- A **bounded lattice** is a lattice that has a **maximum** and a **minimum** element, denoted by 1 and 0 respectively, such that 1 is the least upper bound of any subset of the lattice, and 0 is the greatest lower bound of any subset of the lattice.
- A **complete lattice** is a lattice in which every subset, not just every pair, has a least upper bound and a greatest lower bound.
- A **distributive lattice** is a lattice that satisfies the **distributive law**, which states that for any three elements x, y and z in the lattice, x ∧ (y ∨ z) = (x ∧ y) ∨ (x ∧ z) and x ∨ (y ∧ z) = (x ∨ y) ∧ (x ∨ z).
- A **modular lattice** is a lattice that satisfies the **modular law**, which states that for any four elements x, y, z and w in the lattice, if x ≤ w, then x ∨ (y ∧ w) = (x ∨ y) ∧ w.
- A **complemented lattice** is a lattice in which every element has a **complement**, which is an element y such that x ∧ y = 0 and x ∨ y = 1.
- A **Boolean lattice** is a lattice that is bounded, distributive and complemented. It is also called a **Boolean algebra**, and it can be used to model the logic of propositions, sets, circuits and other applications.

: 13.2: Lattices - Mathematics LibreTexts