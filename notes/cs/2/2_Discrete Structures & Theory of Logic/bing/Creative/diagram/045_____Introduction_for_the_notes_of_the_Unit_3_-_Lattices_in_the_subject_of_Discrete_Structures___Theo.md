### Introduction for the notes of the Unit 3 - Lattices in the subject of Discrete Structures & Theory of Logic

- A **lattice** is a partially ordered set (poset) in which every pair of elements has a unique least upper bound (lub) and a unique greatest lower bound (glb).
- A **bounded lattice** is a lattice that has a minimum element (denoted by 0) and a maximum element (denoted by 1).
- A **distributive lattice** is a lattice that satisfies the distributive laws: for any elements x, y, and z in the lattice, x ∧ (y ∨ z) = (x ∧ y) ∨ (x ∧ z) and x ∨ (y ∧ z) = (x ∨ y) ∧ (x ∨ z), where ∧ and ∨ denote the glb and lub operations, respectively.
- A **complemented lattice** is a bounded lattice in which every element has a unique complement, that is, an element y such that x ∧ y = 0 and x ∨ y = 1 for any element x in the lattice.
- A **Boolean algebra** is a distributive complemented lattice. It is also a special case of an algebraic structure that consists of a set, two binary operations, a unary operation, and two constants, satisfying certain axioms.
- A **sublattice** of a lattice is a subset of the lattice that is also a lattice under the same glb and lub operations.
- A **homomorphism** between two lattices is a function that preserves the glb and lub operations, that is, f(x ∧ y) = f(x) ∧ f(y) and f(x ∨ y) = f(x) ∨ f(y) for any elements x and y in the domain lattice.
- An **isomorphism** between two lattices is a bijective homomorphism that has an inverse homomorphism, that is, f and f^-1 are both homomorphisms.
- A **direct product** of two lattices is a lattice that consists of the Cartesian product of the two sets, and the glb and lub operations are defined componentwise, that is, (x1, x2) ∧ (y1, y2) = (x1 ∧ y1, x2 ∧ y2) and (x1, x2) ∨ (y1, y2) = (x1 ∨ y1, x2 ∨ y2) for any elements (x1, x2) and (y1, y2) in the product lattice.
- A **lattice isomorphism theorem** states that any finite distributive lattice is isomorphic to a direct product of a finite number of simple lattices, where a simple lattice is a lattice that has no proper sublattices other than 0 and 1.