### Complemented for the notes of the Unit 3 - Lattices in the subject of Discrete Structures & Theory of Logic

A lattice is a partially ordered set (poset) in which every pair of elements has a unique least upper bound (lub) and a unique greatest lower bound (glb).

Some important concepts and properties of lattices are:

- A **bounded lattice** is a lattice that has a minimum element (denoted by 0) and a maximum element (denoted by 1).
- A **distributive lattice** is a lattice that satisfies the distributive laws: for any elements x, y, and z in the lattice, x ∧ (y ∨ z) = (x ∧ y) ∨ (x ∧ z) and x ∨ (y ∧ z) = (x ∨ y) ∧ (x ∨ z), where ∧ and ∨ denote the glb and lub operations, respectively.
- A **complemented lattice** is a bounded lattice that has a complement for every element, i.e., for any element x in the lattice, there exists an element y such that x ∧ y = 0 and x ∨ y = 1. A complemented lattice is always distributive.
- A **Boolean algebra** is a complemented lattice that has two additional operations: negation (denoted by ¬) and exclusive or (denoted by ⊕). Negation is defined as ¬x = y, where y is the complement of x. Exclusive or is defined as x ⊕ y = (x ∨ y) ∧ ¬(x ∧ y). A Boolean algebra satisfies the following laws:

  - Commutative laws: x ∧ y = y ∧ x and x ∨ y = y ∨ x
  - Associative laws: x ∧ (y ∧ z) = (x ∧ y) ∧ z and x ∨ (y ∨ z) = (x ∨ y) ∨ z
  - Identity laws: x ∧ 1 = x and x ∨ 0 = x
  - Complement laws: x ∧ ¬x = 0 and x ∨ ¬x = 1
  - Idempotent laws: x ∧ x = x and x ∨ x = x
  - Absorption laws: x ∧ (x ∨ y) = x and x ∨ (x ∧ y) = x
  - De Morgan's laws: ¬(x ∧ y) = ¬x ∨ ¬y and ¬(x ∨ y) = ¬x ∧ ¬y
  - Distributive laws: x ∧ (y ∨ z) = (x ∧ y) ∨ (x ∧ z) and x ∨ (y ∧ z) = (x ∨ y) ∧ (x ∨ z)
  - Involution law: ¬(¬x) = x
  - Exclusive or laws: x ⊕ y = ¬x ⊕ ¬y and x ⊕ x = 0

- A **sublattice** of a lattice is a subset of the lattice that is also a lattice under the same glb and lub operations.
- A **homomorphism** between two lattices is a function that preserves the glb and lub operations, i.e., for any elements x and y in the domain lattice, f(x ∧ y) = f(x) ∧ f(y) and f(x ∨ y) = f(x) ∨ f(y) in the codomain lattice. A homomorphism is **injective** if it maps distinct elements to distinct elements, **surjective** if it maps the domain lattice onto the codomain lattice, and **bijective** if it is both injective and surjective. A bijective homomorphism is also called an **isomorphism**.
- A **lattice isomorphism theorem** states that if f is a homomorphism from a lattice L to a lattice M, then the image of f, denoted by f(L), is a sublattice of M, and f is an isomorphism from L to f(L).
- A **dual lattice** of a lattice L is a lattice that has the same elements as L, but the glb and lub operations are interchanged, i.e., for any elements x and y in L, x ∧ y in L is x ∨ y in L* and x ∨ y in L is x ∧ y in L*, where L* denotes the dual lattice. A **dual isomorphism theorem** states that every lattice is isomorphic to its dual lattice.