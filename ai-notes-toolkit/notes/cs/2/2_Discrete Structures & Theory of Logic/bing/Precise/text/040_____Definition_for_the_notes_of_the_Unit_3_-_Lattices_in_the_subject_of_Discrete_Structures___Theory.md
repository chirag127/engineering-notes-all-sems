### Definition for the notes of the Unit 3 - Lattices in the subject of Discrete Structures & Theory of Logic

- A **lattice** is an algebraic structure that is defined by a partially ordered set and two binary operations, called **join** and **meet**.
- The join and meet operations are used to define the **least upper bound** and **greatest lower bound** of any two elements in the set.
- A lattice must satisfy the following axioms:
  1. The join and meet operations are **commutative**, meaning that for any two elements `a` and `b` in the set, `a join b = b join a` and `a meet b = b meet a`.
  2. The join and meet operations are **associative**, meaning that for any three elements `a`, `b`, and `c` in the set, `(a join b) join c = a join (b join c)` and `(a meet b) meet c = a meet (b meet c)`.
  3. The join and meet operations are **idempotent**, meaning that for any element `a` in the set, `a join a = a` and `a meet a = a`.
  4. The join and meet operations satisfy the **absorption law**, meaning that for any two elements `a` and `b` in the set, `a join (a meet b) = a` and `a meet (a join b) = a`.
- A lattice can be represented visually using a **Hasse diagram**, which is a graph that shows the partial order relation between the elements of the set.
- Lattices have many applications in computer science, including in the design of algorithms and data structures, and in the analysis of program correctness.