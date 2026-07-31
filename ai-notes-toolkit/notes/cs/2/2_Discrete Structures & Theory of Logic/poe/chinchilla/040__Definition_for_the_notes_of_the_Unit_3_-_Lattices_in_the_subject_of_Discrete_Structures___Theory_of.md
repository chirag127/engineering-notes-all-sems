### Definition for the notes of the Unit 3 - Lattices in the subject of Discrete Structures & Theory of Logic

A lattice is a mathematical structure that is used to study partially ordered sets. It consists of a set of elements and two binary operations, meet and join, that satisfy certain axioms. Here are some key definitions related to lattices:

1. Partial Order: A partial order is a binary relation on a set that is reflexive, antisymmetric, and transitive. In other words, for any elements a, b, and c in the set, the following properties hold:
- Reflexivity: a ≤ a
- Antisymmetry: If a ≤ b and b ≤ a, then a = b
- Transitivity: If a ≤ b and b ≤ c, then a ≤ c

2. Lattice: A lattice is a partially ordered set in which every pair of elements has a unique greatest lower bound (meet) and a unique least upper bound (join). The meet and join operations are denoted by ∧ and ∨, respectively.

3. Sublattice: A sublattice of a lattice L is a subset of L that is itself a lattice with respect to the same partial order and the same meet and join operations.

4. Distributive Lattice: A lattice is said to be distributive if it satisfies one of the following equivalent conditions:
- a ∧ (b ∨ c) = (a ∧ b) ∨ (a ∧ c) for all a, b, c in the lattice
- a ∨ (b ∧ c) = (a ∨ b) ∧ (a ∨ c) for all a, b, c in the lattice

5. Complemented Lattice: A lattice is said to be complemented if every element has a unique complement. That is, for every element a in the lattice, there exists a unique element b such that a ∧ b = 0 and a ∨ b = 1.

6. Boolean Algebra: A Boolean algebra is a complemented distributive lattice with the additional property that every element has a unique complement.

Understanding these definitions is essential for studying lattices and their applications in discrete structures and theory of logic. It is important to note that lattices have a wide range of applications in computer science, including in databases, programming languages, and artificial intelligence.