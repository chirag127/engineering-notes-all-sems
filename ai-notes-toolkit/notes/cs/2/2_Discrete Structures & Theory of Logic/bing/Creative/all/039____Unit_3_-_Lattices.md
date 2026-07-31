# Unit 3 - Lattices

- A lattice is a partially ordered set (L, ≤) in which every pair of elements has a least upper bound and a greatest lower bound .
- A least upper bound of a pair {a, b} is an element c such that a ≤ c and b ≤ c, and there is no other element d such that a ≤ d and b ≤ d and d ≤ c. It is denoted by a ∨ b or lub(a, b).
- A greatest lower bound of a pair {a, b} is an element c such that c ≤ a and c ≤ b, and there is no other element d such that d ≤ a and d ≤ b and c ≤ d. It is denoted by a ∧ b or glb(a, b).
- A lattice is also an algebraic structure with two binary, commutative and associative operations ∨ and ∧ that satisfy the absorption laws: a ∨ (a ∧ b) = a and a ∧ (a ∨ b) = a for all elements a and b.
- A lattice can be represented by a Hasse diagram, which is a graphical representation of the partial order relation. The elements are drawn as points, and a line segment is drawn between two elements a and b if a ≤ b and there is no other element c such that a ≤ c and c ≤ b. The lower elements are drawn below the higher elements.
- A lattice is called bounded if it has a least element 0 and a greatest element 1, such that 0 ≤ a and a ≤ 1 for all elements a. The least and greatest elements are also called the bottom and the top of the lattice, respectively.
- A lattice is called distributive if it satisfies the distributive laws: a ∨ (b ∧ c) = (a ∨ b) ∧ (a ∨ c) and a ∧ (b ∨ c) = (a ∧ b) ∨ (a ∧ c) for all elements a, b and c. A lattice is distributive if and only if it does not contain a sublattice isomorphic to M3 or N5, where M3 and N5 are the following lattices:

![M3 and N5](https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/Lattice_M3.svg/1200px-Lattice_M3.svg.png)

- A lattice is called complemented if every element a has a complement a', such that a ∨ a' = 1 and a ∧ a' = 0. A complemented lattice is called uniquely complemented if every element has a unique complement. A lattice is uniquely complemented if and only if it is distributive and bounded.
- A lattice is called modular if it satisfies the modular law: a ≤ c implies a ∨ (b ∧ c) = (a ∨ b) ∧ c for all elements a, b and c. A modular lattice is also called a Dedekind lattice. A modular lattice is distributive if and only if it does not contain a sublattice isomorphic to M3.
- A lattice is called complete if every subset of L has a least upper bound and a greatest lower bound. A complete lattice is bounded, and every bounded lattice is complete if it is finite. A complete lattice is distributive if and only if it satisfies the infinite distributive laws: ∨ S ∧ T = ∧ {∨ {s, t} | s ∈ S, t ∈ T} and ∧ S ∨ T = ∨ {∧ {s, t} | s ∈ S, t ∈ T} for all subsets S and T of L.
- A lattice is called a Boolean algebra if it is a distributive, complemented and bounded lattice. A Boolean algebra is also a complete lattice, and every complete lattice is a Boolean algebra if it is finite. A Boolean algebra has the following properties:
  - a ∨ 0 = a and a ∧ 1 = a for all elements a (identity laws).
  - a ∨ a = a and a ∧ a = a for all elements a (idempotent laws).
  - a ∨ b = b ∨ a and a ∧ b = b ∧ a for all elements a and b (commutative laws).
  - a ∨ (b ∨ c) = (a ∨ b) ∨ c and a ∧ (b ∧ c) = (