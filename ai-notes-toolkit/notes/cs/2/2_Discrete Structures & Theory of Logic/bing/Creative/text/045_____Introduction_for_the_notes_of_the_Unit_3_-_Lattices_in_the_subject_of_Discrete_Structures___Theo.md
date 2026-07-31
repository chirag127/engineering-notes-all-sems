### Introduction for the notes of the Unit 3 - Lattices in the subject of Discrete Structures & Theory of Logic

- A **lattice** is a partially ordered set (poset) in which every pair of elements has a unique least upper bound (lub) and a unique greatest lower bound (glb).
- A **poset** is a set with a binary relation that is reflexive, antisymmetric, and transitive.
- A **least upper bound** of a subset S of a poset P is an element x in P such that x is greater than or equal to every element in S and there is no element y in P that is smaller than x and greater than or equal to every element in S.
- A **greatest lower bound** of a subset S of a poset P is an element x in P such that x is less than or equal to every element in S and there is no element y in P that is greater than x and less than or equal to every element in S.
- A **bounded lattice** is a lattice that has a minimum element (called **zero**) and a maximum element (called **one**).
- A **complemented lattice** is a bounded lattice in which every element has a unique complement, that is, an element x such that x and its complement have zero as their glb and one as their lub.
- A **Boolean algebra** is a complemented lattice that satisfies the distributive law, that is, for any elements x, y, and z, x ∧ (y ∨ z) = (x ∧ y) ∨ (x ∧ z) and x ∨ (y ∧ z) = (x ∨ y) ∧ (x ∨ z), where ∧ denotes the glb and ∨ denotes the lub.
- A **sublattice** of a lattice L is a subset of L that is also a lattice with respect to the same partial order.
- A **homomorphism** of lattices is a function f from one lattice L to another lattice M that preserves the glb and lub operations, that is, for any elements x and y in L, f(x ∧ y) = f(x) ∧ f(y) and f(x ∨ y) = f(x) ∨ f(y).
- An **isomorphism** of lattices is a bijective homomorphism that has an inverse that is also a homomorphism. Two lattices are **isomorphic** if there exists an isomorphism between them.