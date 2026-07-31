# Definition for the notes of the Unit 3 - Lattices in the subject of Discrete Structures & Theory of Logic

- A **lattice** is a partially ordered set (poset) in which every pair of elements has a **greatest lower bound** and a **least upper bound**.
- A greatest lower bound of a pair of elements `a` and `b` in a poset is an element `c` such that `c ≤ a` and `c ≤ b`, and there is no other element `d` such that `d ≤ a`, `d ≤ b` and `d > c`. A greatest lower bound is also called a **meet** or an **infimum**.
- A least upper bound of a pair of elements `a` and `b` in a poset is an element `c` such that `a ≤ c` and `b ≤ c`, and there is no other element `d` such that `a ≤ d`, `b ≤ d` and `d < c`. A least upper bound is also called a **join** or a **supremum**.
- A lattice can be represented by a **Hasse diagram**, which is a graphical representation of the partial order relation. In a Hasse diagram, each element of the lattice is represented by a node, and a line is drawn between two nodes if and only if one element is the immediate predecessor or successor of the other.
- A lattice can also be viewed as an algebraic structure with two binary operations, called **meet** and **join**, denoted by `∧` and `∨` respectively. These operations satisfy the following properties for any elements `a`, `b` and `c` in the lattice:
  - **Commutativity**: `a ∧ b = b ∧ a` and `a ∨ b = b ∨ a`
  - **Associativity**: `a ∧ (b ∧ c) = (a ∧ b) ∧ c` and `a ∨ (b ∨ c) = (a ∨ b) ∨ c`
  - **Idempotency**: `a ∧ a = a` and `a ∨ a = a`
  - **Absorption**: `a ∧ (a ∨ b) = a` and `a ∨ (a ∧ b) = a`
- A lattice is denoted by `[L; ∧, ∨]`, where `L` is the set of elements and `∧` and `∨` are the meet and join operations. If the partial order relation is also specified, the lattice is denoted by `[L; ∧, ∨, ≤]`.
- A lattice is said to be **bounded** if it has a **least element** and a **greatest element**. A least element is an element that is smaller than or equal to every other element in the lattice, and a greatest element is an element that is larger than or equal to every other element in the lattice. A bounded lattice is denoted by `[L; ∧, ∨, 0, 1]`, where `0` and `1` are the least and greatest elements respectively.
- A lattice is said to be **distributive** if it satisfies the following additional property for any elements `a`, `b` and `c` in the lattice:
  - **Distributivity**: `a ∧ (b ∨ c) = (a ∧ b) ∨ (a ∧ c)` and `a ∨ (b ∧ c) = (a ∨ b) ∧ (a ∨ c)`
- A lattice is said to be **complemented** if every element has a **complement**. A complement of an element `a` in a lattice is an element `b` such that `a ∧ b = 0` and `a ∨ b = 1`, where `0` and `1` are the least and greatest elements of the lattice. A complemented lattice is denoted by `[L; ∧, ∨, ', 0, 1]`, where `'` is the complement operation.
- A lattice is said to be **Boolean** if it is bounded, distributive and complemented. A Boolean lattice is also called a **Boolean algebra**.