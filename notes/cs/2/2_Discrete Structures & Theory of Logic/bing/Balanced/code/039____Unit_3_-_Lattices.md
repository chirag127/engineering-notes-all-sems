## Unit 3 - Lattices

- A lattice is a partially ordered set (L, ≤) in which every pair of elements has a least upper bound and a greatest lower bound.
- A least upper bound of a pair {a, b} is an element c such that a ≤ c and b ≤ c, and there is no other element d such that a ≤ d and b ≤ d and d < c. A least upper bound is also called a join or a supremum, and is denoted by a ∨ b.
- A greatest lower bound of a pair {a, b} is an element c such that c ≤ a and c ≤ b, and there is no other element d such that d ≤ a and d ≤ b and c < d. A greatest lower bound is also called a meet or an infimum, and is denoted by a ∧ b.
- A lattice can be represented by a Hasse diagram, which is a graphical representation of the partial order relation. In a Hasse diagram, each element of the lattice is represented by a node, and a line is drawn between two nodes if and only if one element is the immediate predecessor or successor of the other element in the partial order.
- A lattice is said to be bounded if it has a least element and a greatest element. A least element is an element 0 such that 0 ≤ a for all a in L. A greatest element is an element 1 such that a ≤ 1 for all a in L.
- A lattice is said to be distributive if it satisfies the following distributive laws for all a, b, c in L:

  - a ∨ (b ∧ c) = (a ∨ b) ∧ (a ∨ c)
  - a ∧ (b ∨ c) = (a ∧ b) ∨ (a ∧ c)

- A lattice is said to be complemented if every element has a complement, which is an element a' such that a ∨ a' = 1 and a ∧ a' = 0. A complemented lattice is distributive if and only if every element has a unique complement.
- A lattice is said to be modular if it satisfies the following modular law for all a, b, c in L:

  - If a ≤ c, then a ∨ (b ∧ c) = (a ∨ b) ∧ c

- A modular lattice is distributive if and only if it satisfies the following condition for all a, b, c in L:

  - If a ∨ b = a ∨ c and a ∧ b = a ∧ c, then b = c

- A lattice is said to be Boolean if it is bounded, distributive, and complemented. A Boolean lattice is also called a Boolean algebra, and it has the following properties for all a, b, c in L:

  - Commutative laws: a ∨ b = b ∨ a and a ∧ b = b ∧ a
  - Associative laws: a ∨ (b ∨ c) = (a ∨ b) ∨ c and a ∧ (b ∧ c) = (a ∧ b) ∧ c
  - Identity laws: a ∨ 0 = a and a ∧ 1 = a
  - Complementation laws: a ∨ a' = 1 and a ∧ a' = 0
  - Idempotent laws: a ∨ a = a and a ∧ a = a
  - Absorption laws: a ∨ (a ∧ b) = a and a ∧ (a ∨ b) = a
  - De Morgan's laws: (a ∨ b)' = a' ∧ b' and (a ∧ b)' = a' ∨ b'
  - Involution law: (a')' = a

- A sublattice of a lattice (L, ≤) is a subset S of L that is also a lattice with respect to the same partial order relation. A sublattice is said to be proper if it is not equal to the whole lattice.
- A homomorphism from a lattice (L, ≤) to a lattice (M, ≤) is a function f: L → M that preserves the join and meet operations, that is, for all a, b in L:

  - f(a ∨ b) = f(a) ∨ f(b)
  - f(a ∧ b) = f(a) ∧ f(b)

- An isomorphism from a lattice (L, ≤) to a lattice (