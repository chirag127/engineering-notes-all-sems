# Modular and Complete Lattice

- A **lattice** is a partially ordered set (poset) in which every two elements have a unique least upper bound (called their **join** or **supremum**) and a unique greatest lower bound (called their **meet** or **infimum**).
- A lattice is **complete** if every subset of the lattice has a join and a meet, not just every pair of elements. Equivalently, a lattice is complete if it has a **top** element (the join of the empty set) and a **bottom** element (the meet of the empty set).
- A lattice is **modular** if it satisfies the following self-dual condition, called the **modular law**:

  - For any elements a, b, and x in the lattice, if a ≤ b, then a ∨ (x ∧ b) = (a ∨ x) ∧ b.

- The modular law states that if a is below b, then the join of a and the meet of x and b is equal to the meet of the join of a and x and b. In other words, the order of operations of join and meet does not matter when a is below b.
- A modular lattice is a special case of a **distributive lattice**, which satisfies the stronger **distributive laws**:

  - For any elements a, b, and x in the lattice, a ∨ (x ∧ b) = (a ∨ x) ∧ (a ∨ b) and a ∧ (x ∨ b) = (a ∧ x) ∨ (a ∧ b).

- The distributive laws state that the join and meet operations distribute over each other, regardless of the order of the elements. Every distributive lattice is modular, but not every modular lattice is distributive.
- An example of a modular lattice that is not distributive is the **pentagon lattice**, which has five elements: a top element, a bottom element, and three elements in between that form a cycle. The pentagon lattice violates the distributive laws, but satisfies the modular law.
- An example of a complete lattice that is not modular is the **power set lattice**, which has the power set of a given set as its elements, ordered by inclusion. The power set lattice is complete, since every subset of the power set has a join (the union of the subsets) and a meet (the intersection of the subsets). However, the power set lattice is not modular, unless the given set has at most two elements.