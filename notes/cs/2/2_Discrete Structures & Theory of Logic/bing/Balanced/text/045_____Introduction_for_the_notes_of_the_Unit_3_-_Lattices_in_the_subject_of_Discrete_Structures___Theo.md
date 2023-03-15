### Introduction for the notes of the Unit 3 - Lattices in the subject of Discrete Structures & Theory of Logic

- A lattice is a partially ordered set (poset) in which every pair of elements has a unique least upper bound (lub) and a unique greatest lower bound (glb).
- A lattice can be represented by a Hasse diagram, which is a graphical representation of the partial order relation.
- A lattice is said to be bounded if it has a minimum element (called zero or bottom) and a maximum element (called one or top).
- A lattice is said to be distributive if it satisfies the distributive laws: for any elements x, y, and z in the lattice, x ∧ (y ∨ z) = (x ∧ y) ∨ (x ∧ z) and x ∨ (y ∧ z) = (x ∨ y) ∧ (x ∨ z), where ∧ and ∨ denote the glb and lub operations, respectively.
- A lattice is said to be complemented if every element has a unique complement, that is, an element y such that x ∧ y = 0 and x ∨ y = 1, where 0 and 1 are the bottom and top elements of the lattice, respectively.
- A lattice is said to be Boolean if it is bounded, distributive, and complemented. A Boolean lattice can be seen as an algebraic structure that models the operations of Boolean logic.
- A sublattice of a lattice is a subset that is also a lattice with respect to the same partial order relation.
- A homomorphism of lattices is a function that preserves the glb and lub operations, that is, for any elements x and y in the domain lattice, f(x ∧ y) = f(x) ∧ f(y) and f(x ∨ y) = f(x) ∨ f(y) in the codomain lattice.
- An isomorphism of lattices is a bijective homomorphism that has an inverse homomorphism. Two lattices are said to be isomorphic if there exists an isomorphism between them.