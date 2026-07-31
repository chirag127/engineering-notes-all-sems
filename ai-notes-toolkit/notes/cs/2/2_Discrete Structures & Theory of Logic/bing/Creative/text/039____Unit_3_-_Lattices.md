## Unit 3 - Lattices

- A lattice is a partially ordered set (poset) in which every pair of elements has a unique least upper bound (lub) and a unique greatest lower bound (glb).
- A lattice can also be defined as an algebraic structure with two binary, commutative and associative operations, usually denoted by ∧ (meet) and ∨ (join), that satisfy the absorption laws: a ∧ (a ∨ b) = a and a ∨ (a ∧ b) = a for all elements a and b.
- A lattice can be represented by a Hasse diagram, which is a graph that shows the elements and their order relation by using nodes and edges. The nodes represent the elements and the edges represent the order relation. An edge from a node x to a node y means that x ≤ y and there is no element z such that x ≤ z ≤ y. The bottom node is the minimum element and the top node is the maximum element of the lattice, if they exist.
- A lattice is called bounded if it has a minimum element (called bottom or zero) and a maximum element (called top or one). A bounded lattice can be denoted by (L, ≤, 0, 1).
- A lattice is called distributive if it satisfies the distributive laws: a ∧ (b ∨ c) = (a ∧ b) ∨ (a ∧ c) and a ∨ (b ∧ c) = (a ∨ b) ∧ (a ∨ c) for all elements a, b and c. A distributive lattice can be characterized by the absence of sublattices isomorphic to M3 (a diamond with a node inside) or N5 (a pentagon with a node above and below).
- A lattice is called complemented if every element has a complement, that is, an element x such that x ∧ y = 0 and x ∨ y = 1 for some element y. A complemented lattice is called uniquely complemented if every element has a unique complement. A complemented distributive lattice is always uniquely complemented.
- A lattice is called modular if it satisfies the modular law: a ≤ c implies a ∨ (b ∧ c) = (a ∨ b) ∧ c for all elements a, b and c. A modular lattice can be characterized by the absence of sublattices isomorphic to N5. A distributive lattice is always modular, but the converse is not true.
- A lattice is called complete if every subset of elements has a lub and a glb. A complete lattice is always bounded, since the lub of the empty set is the bottom element and the glb of the empty set is the top element. A complete lattice can be denoted by (L, ≤, ⊥, ⊤).
- A lattice is called a Boolean algebra if it is a bounded, distributive and complemented lattice. A Boolean algebra can be denoted by (B, ≤, ∨, ∧, ¬, 0, 1), where ¬ is the complement operation. A Boolean algebra can also be defined as an algebraic structure with two binary operations ∨ and ∧, a unary operation ¬, and two constants 0 and 1, that satisfy the following axioms for all elements a, b and c:

  - Commutative laws: a ∨ b = b ∨ a and a ∧ b = b ∧ a
  - Associative laws: a ∨ (b ∨ c) = (a ∨ b) ∨ c and a ∧ (b ∧ c) = (a ∧ b) ∧ c
  - Distributive laws: a ∨ (b ∧ c) = (a ∨ b) ∧ (a ∨ c) and a ∧ (b ∨ c) = (a ∧ b) ∨ (a ∧ c)
  - Identity laws: a ∨ 0 = a and a ∧ 1 = a
  - Complement laws: a ∨ ¬a = 1 and a ∧ ¬a = 0
  - Idempotent laws: a ∨ a = a and a ∧ a = a
  - Absorption laws: a ∨ (a ∧ b) = a and a ∧ (a ∨ b) = a
  - De Morgan's laws: ¬(a ∨ b) = ¬a ∧ ¬b and ¬(a ∧ b) = ¬a ∨ ¬b

- A Boolean algebra can be represented by a power set, that