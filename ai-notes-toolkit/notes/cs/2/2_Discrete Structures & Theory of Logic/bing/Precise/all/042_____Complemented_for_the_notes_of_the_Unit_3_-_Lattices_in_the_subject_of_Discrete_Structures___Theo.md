# Complemented for the notes of the Unit 3 - Lattices in the subject of Discrete Structures & Theory of Logic

- A **lattice** is an algebraic structure that is defined by a partially ordered set and two binary operations, called **join** and **meet**.
- The join and meet operations are defined in such a way that they satisfy the **absorption law**, which states that for any elements `a` and `b` in the lattice, `a ∨ (a ∧ b) = a` and `a ∧ (a ∨ b) = a`.
- A lattice is said to be **complemented** if for every element `a` in the lattice, there exists an element `a'` such that `a ∨ a' = 1` and `a ∧ a' = 0`, where `1` and `0` are the maximum and minimum elements of the lattice, respectively.
- A lattice can have more than one complement for a given element, but if it has a unique complement for every element, it is called a **uniquely complemented lattice**.
- A **Boolean algebra** is an example of a uniquely complemented lattice, where the complement of an element `a` is denoted by `¬a` or `~a`.
- In a Boolean algebra, the join and meet operations are usually denoted by `∨` and `∧`, respectively, and are called **disjunction** and **conjunction**, respectively.
- The **De Morgan's laws** state that for any elements `a` and `b` in a Boolean algebra, `¬(a ∨ b) = ¬a ∧ ¬b` and `¬(a ∧ b) = ¬a ∨ ¬b`.
- A **distributive lattice** is a lattice in which the join and meet operations satisfy the **distributive law**, which states that for any elements `a`, `b`, and `c` in the lattice, `a ∧ (b ∨ c) = (a ∧ b) ∨ (a ∧ c)` and `a ∨ (b ∧ c) = (a ∨ b) ∧ (a ∨ c)`.
- Every Boolean algebra is a distributive lattice, but not every distributive lattice is a Boolean algebra.
- A **bounded lattice** is a lattice that has a maximum and a minimum element, denoted by `1` and `0`, respectively.
- A **complete lattice** is a lattice in which every subset has a join and a meet.
- A **modular lattice** is a lattice that satisfies the **modular law**, which states that for any elements `a`, `b`, and `c` in the lattice, if `a ≤ c`, then `a ∨ (b ∧ c) = (a ∨ b) ∧ c`.
- A **complemented modular lattice** is a modular lattice that is also complemented.
- A **Heyting algebra** is a bounded lattice that is also a distributive lattice and has an additional binary operation called **implication**, denoted by `→`, which satisfies the property that for any elements `a` and `b` in the lattice, `a → b` is the greatest element `c` such that `a ∧ c ≤ b`.
- A **Boolean algebra** is a Heyting algebra in which the implication operation satisfies the property that for any elements `a` and `b` in the lattice, `a → b = ¬a ∨ b`.