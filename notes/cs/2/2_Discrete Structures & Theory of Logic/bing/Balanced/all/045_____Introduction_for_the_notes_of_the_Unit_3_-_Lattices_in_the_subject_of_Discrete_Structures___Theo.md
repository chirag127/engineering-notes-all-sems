# Introduction for the notes of the Unit 3 - Lattices in the subject of Discrete Structures & Theory of Logic

- A **lattice** is a partially ordered set (poset) in which every pair of elements has a unique least upper bound (lub) and a unique greatest lower bound (glb).
- A **poset** is a set with a binary relation that is reflexive, antisymmetric, and transitive.
- A **least upper bound** of a pair of elements x and y in a poset is an element z such that x ≤ z, y ≤ z, and z ≤ w for any other upper bound w of x and y.
- A **greatest lower bound** of a pair of elements x and y in a poset is an element z such that z ≤ x, z ≤ y, and w ≤ z for any other lower bound w of x and y.
- A **bounded lattice** is a lattice that has a minimum element (0) and a maximum element (1) such that 0 ≤ x ≤ 1 for any element x in the lattice.
- A **complete lattice** is a lattice in which every subset has a lub and a glb.
- A **distributive lattice** is a lattice that satisfies the distributive laws: x ∧ (y ∨ z) = (x ∧ y) ∨ (x ∧ z) and x ∨ (y ∧ z) = (x ∨ y) ∧ (x ∨ z) for any elements x, y, and z in the lattice, where ∧ denotes the glb and ∨ denotes the lub.
- A **complemented lattice** is a bounded lattice in which every element has a complement, that is, an element y such that x ∧ y = 0 and x ∨ y = 1 for any element x in the lattice.
- A **Boolean algebra** is a distributive and complemented lattice. It is also a Boolean ring, that is, a ring with identity in which every element is idempotent, that is, x + x = x and x · x = x for any element x in the ring, where + denotes the symmetric difference and · denotes the intersection.
- A **sublattice** of a lattice is a subset that is also a lattice with respect to the same partial order.
- A **homomorphism** of lattices is a function that preserves the lub and the glb operations, that is, f(x ∨ y) = f(x) ∨ f(y) and f(x ∧ y) = f(x) ∧ f(y) for any elements x and y in the domain lattice.
- An **isomorphism** of lattices is a bijective homomorphism that has an inverse homomorphism, that is, f and g are isomorphisms of lattices if f(g(x)) = x and g(f(x)) = x for any element x in the domain and codomain lattices.
- A **lattice diagram** is a graphical representation of a lattice using dots and lines, where each dot represents an element and each line represents the partial order relation. The lub and the glb of two elements are the lowest and the highest common ancestors of the corresponding dots in the diagram, respectively.
- A **Hasse diagram** is a simplified lattice diagram that omits the reflexive and transitive edges, that is, the loops and the redundant lines. A Hasse diagram shows only the immediate predecessors and successors of each element in the lattice.