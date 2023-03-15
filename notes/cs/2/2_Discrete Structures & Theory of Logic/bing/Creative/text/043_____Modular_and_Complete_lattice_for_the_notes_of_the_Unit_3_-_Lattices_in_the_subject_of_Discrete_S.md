### Modular and Complete Lattice

- A **lattice** is a partially ordered set (poset) in which every pair of elements has a **greatest lower bound** (glb) and a **least upper bound** (lub). The glb and lub are also called the **meet** and the **join** of the elements, and are denoted by ∧ and ∨ respectively. A lattice is denoted by [L; ∧, ∨].
- A **complete lattice** is a lattice in which **all subsets** have a glb and a lub. The glb and lub of the whole set are called the **minimum** and the **maximum** of the lattice, and are denoted by 0 and 1 respectively. A complete lattice is also called a **bounded lattice**.
- A **modular lattice** is a lattice that satisfies the **modular law**: a ∨ (b ∧ c) = (a ∨ b) ∧ c whenever a ≤ c. This law is an abstraction of the **second isomorphism theorem** in algebra, which states that for any submodules A, B, C of a module M, if A ⊆ C, then A + (B ∩ C) ≅ (A + B) ∩ C.
- A modular lattice has a **composition sequence**, which is a finite sequence of elements x1, x2, ..., xn such that x1 = 0, xn = 1, and xi ∧ xi+1 = 0 for all i. The length of the composition sequence is called the **dimension** of the modular lattice, and is denoted by d(L).
- A modular lattice has a **dimension function**, which is an integer-valued function d such that d(x ∨ y) + d(x ∧ y) = d(x) + d(y) and such that if the interval [a, b] is prime, it follows that d(b) = d(a) + 1. A prime interval is an interval that contains no other elements except its endpoints.
- Examples of modular lattices are:
  - The **subspaces** of a vector space (or more generally the **submodules** of a module over a ring).
  - The **ideals** of a principal ideal domain (or more generally a Dedekind domain).
  - The **subgroups** of a finite abelian group (or more generally a finite solvable group).
  - The **faces** of a convex polytope (or more generally a matroid).
  - The **subsets** of a finite set (or more generally a distributive lattice).