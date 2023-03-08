## Unit 3 - Lattices

- A **lattice** is a structure consisting of strips of wood or metal crossed and fastened together with square or diamond-shaped spaces left between, used as a screen or fence or as a support for climbing plants.
- A **lattice** is also an interlaced structure or pattern resembling a lattice, such as a network, a matrix, a web, or a grid.
- A **lattice** is also a regular repeated three-dimensional arrangement of atoms, ions, or molecules in a metal or other crystalline solid.
- A **lattice** is also an abstract structure studied in the mathematical subdisciplines of order theory and abstract algebra. It consists of a partially ordered set in which every pair of elements has a unique supremum (also called a least upper bound or join) and a unique infimum (also called a greatest lower bound or meet).
- A **lattice** is an algebraic structure, consisting of a set and two binary, commutative and associative operations and on satisfying the following axiomatic identities for all elements (sometimes called absorption laws):

```
a ∨ (a ∧ b) = a
a ∧ (a ∨ b) = a
```

- A **lattice** can be represented by a **Hasse diagram**, which is a graphical representation of the partial order relation on the elements of the lattice. The Hasse diagram consists of nodes representing the elements of the lattice, and edges connecting pairs of elements that are comparable and adjacent in the partial order (i.e., there is no other element between them). For example, the following is a Hasse diagram of a lattice with six elements:

```
  1
 / \
a   b
|\ /|
| / |
|/ \|
c   d
 \ /
  0
```

- A **lattice** can be classified into different types based on its properties. Some of the common types of lattices are:

  - A **complete lattice** is a lattice in which every subset has a supremum and an infimum. For example, the lattice of all subsets of a given set, ordered by inclusion, is a complete lattice.
  - A **bounded lattice** is a lattice that has a least element (also called a bottom or zero) and a greatest element (also called a top or one). For example, the lattice of natural numbers, ordered by divisibility, is a bounded lattice, with 0 as the least element and 1 as the greatest element.
  - A **distributive lattice** is a lattice that satisfies the following distributive laws for all elements:

  ```
  a ∨ (b ∧ c) = (a ∨ b) ∧ (a ∨ c)
  a ∧ (b ∨ c) = (a ∧ b) ∨ (a ∧ c)
  ```

  For example, the lattice of all subsets of a given set, ordered by inclusion, is a distributive lattice.
  - A **modular lattice** is a lattice that satisfies the following modular law for all elements:

  ```
  a ∨ (b ∧ (a ∨ c)) = (a ∨ b) ∧ (a ∨ c)
  ```

  For example, the lattice of all subspaces of a given vector space, ordered by inclusion, is a modular lattice.
  - A **complemented lattice** is a lattice that has a complement for every element, i.e., for every element , there exists an element such that:

  ```
  a ∨ a' = 1
  a ∧ a' = 0
  ```

  For example, the lattice of all subsets of a given set, ordered by inclusion, is a complemented lattice, where the complement of a subset is its set difference with the whole set.
  - A **Boolean lattice** or a **Boolean algebra** is a lattice that is bounded, distributive, and complemented. For example, the lattice of all subsets of a given set, ordered by inclusion, is a Boolean lattice, where the operations and are defined as set union and set intersection, respectively.

- A **lattice** has many applications in various fields of mathematics, computer science, physics, and engineering. Some of the applications are:

  - In **order theory**, lattices are used to study the properties and structure of partially ordered sets, such as fixed points, closure operators, Galois connections, and duality.
  - In **

Some possible mnemonics and learning tricks for the topic are:

- To remember the absorption laws, you can use the acronym **AAA** (Absorption, And, Or), and think of the phrase "Absorb And Or".
- To remember the distributive laws, you can use the acronym **DAD** (Distributive, And, Or), and think of the phrase "Distribute And Or".
- To remember the modular law, you can use the acronym **MOM** (Modular, Or, And), and think of the phrase "Modify Or And".
- To remember the types of lattices, you can use the acronym **BCDM** (Bounded, Complemented, Distributive, Modular), and think of the phrase "Be Cool, Don't Mess".
- To remember the definition of a complemented lattice, you can use the acronym **CO** (Complemented, One), and think of the phrase "Complement One".
- To remember the definition of a Boolean lattice, you can use the acronym **BDC** (Boolean, Distributive, Complemented), and think of the phrase "Be Discrete, Complement".