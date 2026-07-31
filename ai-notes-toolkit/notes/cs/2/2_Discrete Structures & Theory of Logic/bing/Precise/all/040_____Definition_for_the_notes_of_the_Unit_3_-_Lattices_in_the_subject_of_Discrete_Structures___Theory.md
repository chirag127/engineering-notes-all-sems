# Unit 3 - Lattices in Discrete Structures & Theory of Logic

### Definition

- A **lattice** is an algebraic structure consisting of a partially ordered set in which every two elements have a unique supremum (also called a least upper bound or join) and a unique infimum (also called a greatest lower bound or meet).
- An element is said to **cover** another element if the first element is greater than the second element in the partial order, and there is no element in between the two in the partial order.
- A lattice is said to be **complete** if all subsets of the lattice have a supremum and an infimum.
- A lattice is said to be **distributive** if the meet and join operations distribute over each other, that is, for all elements a, b, and c in the lattice, a ∧ (b ∨ c) = (a ∧ b) ∨ (a ∧ c) and a ∨ (b ∧ c) = (a ∨ b) ∧ (a ∨ c).
- A lattice is said to be **modular** if for all elements a, b, and c in the lattice, if a ≤ c, then a ∨ (b ∧ c) = (a ∨ b) ∧ c.
- A lattice is said to be **complemented** if every element has a unique complement, that is, an element b such that a ∧ b = 0 and a ∨ b = 1, where 0 and 1 are the bottom and top elements of the lattice, respectively.
- A lattice is said to be **bounded** if it has a greatest element (also called a top element or maximum) and a least element (also called a bottom element or minimum).