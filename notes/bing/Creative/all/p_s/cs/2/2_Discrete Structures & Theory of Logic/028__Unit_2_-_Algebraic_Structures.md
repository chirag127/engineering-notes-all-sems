## Unit 2 - Algebraic Structures

- An algebraic structure is a set with one or more operations that obey specific laws or axioms.
- Examples of algebraic structures include groups, rings, fields, vector spaces, modules, algebras, etc.
- Each algebraic structure has a different set of properties and operations that make it useful for studying various mathematical concepts and applications.
- Here are some definitions and examples of common algebraic structures:

### Group
- A group is an algebraic structure that consists of a set G and a binary operation * that satisfies the following axioms:
  - Closure: For all a, b in G, a * b is also in G.
  - Associativity: For all a, b, c in G, (a * b) * c = a * (b * c).
  - Identity: There exists an element e in G such that for all a in G, a * e = e * a = a.
  - Inverse: For every element a in G, there exists an element b in G such that a * b = b * a = e.
- Examples of groups include:
  - The additive group of integers (Z, +), where the operation is addition and the identity element is 0.
  - The multiplicative group of nonzero rational numbers (Q\*, ×), where the operation is multiplication and the identity element is 1.
  - The symmetric group of permutations on a set S (S_n, ∘), where the operation is composition and the identity element is the identity permutation.

### Ring
- A ring is an algebraic structure that consists of a set R and two binary operations + and × that satisfy the following axioms:
  - (R, +) is an abelian group, meaning that it satisfies the group axioms and also the commutativity axiom: For all a, b in R, a + b = b + a.
  - Closure: For all a, b in R, a × b is also in R.
  - Associativity: For all a, b, c in R, (a × b) × c = a × (b × c).
  - Distributivity: For all a, b, c in R, a × (b + c) = (a × b) + (a × c) and (a + b) × c = (a × c) + (b × c).
- Examples of rings include:
  - The ring of integers (Z, +, ×), where the operations are addition and multiplication.
  - The ring of polynomials with coefficients in a field F (F[x], +, ×), where the operations are polynomial addition and multiplication.
  - The ring of matrices with entries in a field F (F_n×n, +, ×), where the operations are matrix addition and multiplication.

### Field
- A field is an algebraic structure that consists of a set F and two binary operations + and × that satisfy the following axioms:
  - (F, +) and (F\*, ×) are both abelian groups, where F\* is the set of nonzero elements of F.
  - Distributivity: For all a, b, c in F, a × (b + c) = (a × b) + (a × c) and (a + b) × c = (a × c) + (b × c).
- Examples of fields include:
  - The field of rational numbers (Q, +, ×), where the operations are addition and multiplication.
  - The field of real numbers (R, +, ×), where the operations are addition and multiplication.
  - The field of complex numbers (C, +, ×), where the operations are addition and multiplication.

### Vector Space
- A vector space is an algebraic structure that consists of a set V and two operations + and × that satisfy the following axioms:
  - (V, +) is an abelian group, meaning that it satisfies the group axioms and also the commutativity axiom: For all v, w in V, v + w = w + v.
  - There exists a field F such that for every element a in F and every element v in V, a × v is also in V. This operation is called scalar multiplication.
  - Associativity: For all a, b in F and v in V, (a × b) × v = a × (b × v).
  - Identity

Some possible mnemonics and learning tricks for the topic are:

- To remember the group axioms, you can use the acronym CAIN: Closure, Associativity, Identity, Inverse.
- To remember the ring axioms, you can use the acronym CARDS: Commutativity, Associativity, Ring, Distributivity, Subtraction (inverse under addition).
- To remember the field axioms, you can use the acronym FADS: Field, Associativity, Distributivity, Subtraction (inverse under addition) and Division (inverse under multiplication).
- To remember the vector space axioms, you can use the acronym VACID: Vector, Associativity, Commutativity, Identity, Distributivity.