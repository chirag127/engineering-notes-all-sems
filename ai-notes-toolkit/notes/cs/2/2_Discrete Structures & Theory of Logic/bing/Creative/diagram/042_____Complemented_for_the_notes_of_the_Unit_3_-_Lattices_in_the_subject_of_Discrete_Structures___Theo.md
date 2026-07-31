Hello, I am Sydney, your AI assistant. I can help you with your study material for the Unit 3 - Lattices in the subject of Discrete Structures & Theory of Logic. Here are some notes for you:

### Lattices

- A lattice is a partially ordered set (poset) in which every pair of elements has a unique least upper bound (lub) and a unique greatest lower bound (glb).
- A lub of two elements a and b is an element c such that a ≤ c and b ≤ c, and there is no other element d such that a ≤ d and b ≤ d and d < c. A glb of two elements a and b is an element c such that c ≤ a and c ≤ b, and there is no other element d such that d ≤ a and d ≤ b and c < d.
- A lub of a and b is also called the join of a and b, denoted by a ∨ b. A glb of a and b is also called the meet of a and b, denoted by a ∧ b.
- A lattice can be represented by a Hasse diagram, which is a graph that shows the partial order relation by drawing the elements as nodes and connecting them by edges if they are comparable and there is no other element between them.
- A lattice is called bounded if it has a least element (denoted by 0 or ⊥) and a greatest element (denoted by 1 or ⊤). A bounded lattice is also called a complete lattice if every subset of it has a lub and a glb.
- A lattice is called distributive if it satisfies the following properties for any elements a, b, and c:
  - a ∨ (b ∧ c) = (a ∨ b) ∧ (a ∨ c)
  - a ∧ (b ∨ c) = (a ∧ b) ∨ (a ∧ c)
- A lattice is called modular if it satisfies the following property for any elements a, b, and c such that a ≤ c:
  - a ∨ (b ∧ c) = (a ∨ b) ∧ c
- A lattice is called complemented if every element has a complement, which is an element such that their join is the greatest element and their meet is the least element. A complemented lattice is also called a Boolean algebra if it is distributive and bounded.