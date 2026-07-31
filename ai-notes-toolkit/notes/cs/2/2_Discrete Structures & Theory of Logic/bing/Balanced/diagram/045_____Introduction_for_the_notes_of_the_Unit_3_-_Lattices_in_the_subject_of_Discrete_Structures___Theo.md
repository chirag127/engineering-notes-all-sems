### Introduction for the notes of the Unit 3 - Lattices in the subject of Discrete Structures & Theory of Logic

- A **lattice** is a partially ordered set (poset) in which every pair of elements has a unique least upper bound (lub) and a unique greatest lower bound (glb).
- A **bounded lattice** is a lattice that has a minimum element (denoted by 0) and a maximum element (denoted by 1).
- A **distributive lattice** is a lattice that satisfies the distributive laws: for any elements x, y, and z in the lattice, x ∧ (y ∨ z) = (x ∧ y) ∨ (x ∧ z) and x ∨ (y ∧ z) = (x ∨ y) ∧ (x ∨ z), where ∧ and ∨ are the lub and glb operations, respectively.
- A **complemented lattice** is a bounded lattice in which every element has a unique complement, that is, an element y such that x ∧ y = 0 and x ∨ y = 1 for any element x in the lattice.
- A **Boolean algebra** is a distributive complemented lattice. It can also be defined as a set with two binary operations, called conjunction (denoted by ∧) and disjunction (denoted by ∨), and a unary operation, called negation (denoted by ¬), that satisfy the following axioms:
  - Commutative laws: x ∧ y = y ∧ x and x ∨ y = y ∨ x for any elements x and y in the set.
  - Associative laws: x ∧ (y ∧ z) = (x ∧ y) ∧ z and x ∨ (y ∨ z) = (x ∨ y) ∨ z for any elements x, y, and z in the set.
  - Distributive laws: x ∧ (y ∨ z) = (x ∧ y) ∨ (x ∧ z) and x ∨ (y ∧ z) = (x ∨ y) ∧ (x ∨ z) for any elements x, y, and z in the set.
  - Identity laws: x ∧ 1 = x and x ∨ 0 = x for any element x in the set, where 0 and 1 are the minimum and maximum elements, respectively.
  - Complement laws: x ∧ ¬x = 0 and x ∨ ¬x = 1 for any element x in the set, where ¬x is the complement of x.
  - Idempotent laws: x ∧ x = x and x ∨ x = x for any element x in the set.
- A **sublattice** of a lattice is a subset of the lattice that is also a lattice under the same lub and glb operations.
- A **homomorphism** between two lattices is a function that preserves the lub and glb operations, that is, f(x ∨ y) = f(x) ∨ f(y) and f(x ∧ y) = f(x) ∧ f(y) for any elements x and y in the domain lattice.
- An **isomorphism** between two lattices is a bijective homomorphism, that is, a one-to-one and onto function that preserves the lub and glb operations. Two lattices are **isomorphic** if there exists an isomorphism between them.
- A **dual** of a lattice is a lattice that has the same elements as the original lattice, but with the lub and glb operations interchanged. The dual of a lattice is denoted by L^d. A lattice is **self-dual** if it is isomorphic to its dual.