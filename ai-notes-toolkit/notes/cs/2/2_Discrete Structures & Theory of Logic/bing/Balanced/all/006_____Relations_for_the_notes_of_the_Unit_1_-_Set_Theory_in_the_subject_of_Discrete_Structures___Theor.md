Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of Relations for the notes of the Unit 1 - Set Theory in the subject of Discrete Structures & Theory of Logic.

# Relations

- A relation R from a set A to a set B is a subset of the Cartesian product A x B.
- A relation R on a set A is a relation from A to A, or a subset of A x A.
- A relation R on a set A can be represented by a directed graph, where the vertices are the elements of A and the edges are the ordered pairs in R.
- A relation R on a set A can also be represented by a matrix, where the rows and columns are indexed by the elements of A and the entry at row i and column j is 1 if (i, j) is in R and 0 otherwise.
- A relation R on a set A is called reflexive if (a, a) is in R for every a in A.
- A relation R on a set A is called symmetric if (a, b) is in R implies (b, a) is in R for every a, b in A.
- A relation R on a set A is called antisymmetric if (a, b) is in R and (b, a) is in R implies a = b for every a, b in A.
- A relation R on a set A is called transitive if (a, b) is in R and (b, c) is in R implies (a, c) is in R for every a, b, c in A.
- A relation R on a set A is called an equivalence relation if it is reflexive, symmetric and transitive.
- An equivalence relation R on a set A partitions A into disjoint subsets called equivalence classes, where two elements are in the same equivalence class if and only if they are related by R.
- A relation R on a set A is called a partial order if it is reflexive, antisymmetric and transitive.
- A partial order R on a set A can be represented by a Hasse diagram, which is a directed graph where the edges are the minimal pairs in R and the vertices are arranged such that if (a, b) is in R, then a is below b.
- A set A with a partial order R is called a partially ordered set or a poset, denoted by (A, R).
- A poset (A, R) is called a total order or a linear order if for every a, b in A, either (a, b) is in R or (b, a) is in R.
- A poset (A, R) is called a well-order if it is a total order and every non-empty subset of A has a least element with respect to R.
- A poset (A, R) is called a lattice if for every a, b in A, there exist a least upper bound and a greatest lower bound of {a, b} with respect to R, denoted by a ∨ b and a ∧ b respectively.
- A lattice (A, R) is called a distributive lattice if for every a, b, c in A, the following distributive laws hold: a ∨ (b ∧ c) = (a ∨ b) ∧ (a ∨ c) and a ∧ (b ∨ c) = (a ∧ b) ∨ (a ∧ c).
- A lattice (A, R) is called a Boolean algebra if it is a distributive lattice and there exist a least element 0 and a greatest element 1 in A such that for every a in A, there exists a complement ¬a in A such that a ∨ ¬a = 1 and a ∧ ¬a = 0.
- A Boolean algebra (A, R) can be represented by a Boolean expression, which is a combination of elements of A and the operators ∨, ∧ and ¬, and parentheses. A Boolean expression can be simplified using the following rules:

  - Identity laws: a ∨ 0 = a and a ∧ 1 = a
  - Domination laws: a ∨ 1 = 1 and a ∧ 0 = 0
  - Idempotent laws: a ∨ a = a and a ∧ a = a
  - Commutative laws: a ∨ b = b ∨ a and a ∧ b = b ∧ a
  - Associative laws: (a ∨ b) ∨ c = a ∨ (b ∨ c) and (a ∧ b) ∧ c = a ∧ (b ∧ c