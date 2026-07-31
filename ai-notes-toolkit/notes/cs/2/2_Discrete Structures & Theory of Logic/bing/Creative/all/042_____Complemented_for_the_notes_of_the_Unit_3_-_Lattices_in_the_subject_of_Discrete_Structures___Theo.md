# Complemented for the notes of the Unit 3 - Lattices in the subject of Discrete Structures & Theory of Logic

- A **lattice** is a partially ordered set (poset) in which every pair of elements has a unique least upper bound (lub) and a unique greatest lower bound (glb).
- A **bounded lattice** is a lattice that has a minimum element (denoted by 0) and a maximum element (denoted by 1).
- A **complemented lattice** is a bounded lattice in which every element has a **complement**, that is, an element such that their lub is 1 and their glb is 0.
- A **distributive lattice** is a lattice that satisfies the **distributive laws**, that is, for any elements x, y, and z in the lattice, x ∧ (y ∨ z) = (x ∧ y) ∨ (x ∧ z) and x ∨ (y ∧ z) = (x ∨ y) ∧ (x ∨ z), where ∧ and ∨ denote the glb and lub operations, respectively.
- A **Boolean algebra** is a distributive complemented lattice. It is also called a **Boolean lattice** or a **two-element algebra**.
- A **sublattice** of a lattice L is a subset of L that is also a lattice under the same glb and lub operations.
- A **homomorphism** between two lattices L and M is a function f : L → M that preserves the glb and lub operations, that is, for any elements x and y in L, f(x ∧ y) = f(x) ∧ f(y) and f(x ∨ y) = f(x) ∨ f(y).
- An **isomorphism** between two lattices L and M is a bijective homomorphism f : L → M. Two lattices are **isomorphic** if there exists an isomorphism between them.
- A **lattice diagram** is a graphical representation of a lattice, in which the elements are represented by points and the partial order relation is represented by lines connecting the points. The lub and glb of two elements are shown by the lowest and highest points that are reachable from both elements, respectively.
- A **Hasse diagram** is a simplified lattice diagram, in which only the **covering relations** are shown, that is, the lines connecting two elements x and y such that x < y and there is no element z in the lattice such that x < z < y. The lub and glb of two elements are shown by the lowest and highest points that are directly connected to both elements, respectively.