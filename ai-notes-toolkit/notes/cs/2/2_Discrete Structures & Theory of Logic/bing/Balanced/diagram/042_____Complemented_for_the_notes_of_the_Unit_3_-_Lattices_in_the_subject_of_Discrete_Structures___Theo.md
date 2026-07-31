Hello, I am Sydney, your AI assistant. I can help you with your study material for the Unit 3 - Lattices in the subject of Discrete Structures & Theory of Logic. Here are some notes for you:

# Unit 3 - Lattices

## Definition of a Lattice

- A lattice is a partially ordered set (poset) in which every pair of elements has a unique least upper bound (lub) and a unique greatest lower bound (glb).
- The lub of two elements a and b is denoted by a ∨ b and is called the join of a and b.
- The glb of two elements a and b is denoted by a ∧ b and is called the meet of a and b.
- A lattice can be represented by a Hasse diagram, which is a graph that shows the partial order relation by drawing the elements as nodes and connecting them with edges if one element is the immediate predecessor or successor of another.

## Properties of a Lattice

- A lattice is a poset, so it satisfies the properties of reflexivity, antisymmetry, and transitivity.
- A lattice also satisfies the following properties for any elements a, b, and c in the lattice:
  - Commutativity: a ∨ b = b ∨ a and a ∧ b = b ∧ a
  - Associativity: (a ∨ b) ∨ c = a ∨ (b ∨ c) and (a ∧ b) ∧ c = a ∧ (b ∧ c)
  - Idempotency: a ∨ a = a and a ∧ a = a
  - Absorption: a ∨ (a ∧ b) = a and a ∧ (a ∨ b) = a
- A lattice may or may not have the following additional properties:
  - Boundedness: A lattice is bounded if it has a least element (denoted by 0 or ⊥) and a greatest element (denoted by 1 or ⊤). The least element is the glb of the whole lattice and the greatest element is the lub of the whole lattice.
  - Distributivity: A lattice is distributive if it satisfies the distributive laws: a ∨ (b ∧ c) = (a ∨ b) ∧ (a ∨ c) and a ∧ (b ∨ c) = (a ∧ b) ∨ (a ∧ c) for any elements a, b, and c in the lattice.
  - Complementedness: A lattice is complemented if every element has a complement, which is an element that satisfies the following conditions: a ∨ a' = 1 and a ∧ a' = 0 for any element a and its complement a' in the lattice. A complemented lattice is always bounded and distributive.

## Examples of Lattices

- The set of natural numbers with the divisibility relation is a lattice, where the join of two numbers is their least common multiple and the meet of two numbers is their greatest common divisor.
- The set of subsets of a given set with the inclusion relation is a lattice, where the join of two subsets is their union and the meet of two subsets is their intersection. This lattice is bounded by the empty set and the whole set, and is distributive and complemented.
- The set of propositions with the logical implication relation is a lattice, where the join of two propositions is their logical disjunction and the meet of two propositions is their logical conjunction. This lattice is bounded by the contradiction and the tautology, and is distributive and complemented.