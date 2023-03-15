# Combination of sets

- A combination of sets is a new set that is formed by applying some operation on two or more existing sets.
- There are four basic operations on sets: union, intersection, difference, and complement.
- The union of two sets A and B, denoted by A ∪ B, is the set of all elements that belong to either A or B or both.
- The intersection of two sets A and B, denoted by A ∩ B, is the set of all elements that belong to both A and B.
- The difference of two sets A and B, denoted by A - B, is the set of all elements that belong to A but not to B.
- The complement of a set A, denoted by A', is the set of all elements that do not belong to A.
- The following Venn diagrams illustrate these operations:

![Venn diagrams of set operations](https://i.imgur.com/0Q9y9XO.png)

- Some properties of these operations are:

  - Commutative laws: A ∪ B = B ∪ A and A ∩ B = B ∩ A
  - Associative laws: (A ∪ B) ∪ C = A ∪ (B ∪ C) and (A ∩ B) ∩ C = A ∩ (B ∩ C)
  - Distributive laws: A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C) and A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C)
  - De Morgan's laws: (A ∪ B)' = A' ∩ B' and (A ∩ B)' = A' ∪ B'
  - Identity laws: A ∪ ∅ = A and A ∩ U = A, where ∅ is the empty set and U is the universal set
  - Complement laws: A ∪ A' = U and A ∩ A' = ∅
  - Idempotent laws: A ∪ A = A and A ∩ A = A
  - Absorption laws: A ∪ (A ∩ B) = A and A ∩ (A ∪ B) = A
  - Domination laws: A ∪ U = U and A ∩ ∅ = ∅
  - Double complement law: (A')' = A

- A subset of a set A is a set that contains only elements of A. A proper subset of A is a subset that is not equal to A. The notation A ⊆ B means that A is a subset of B, and A ⊂ B means that A is a proper subset of B.
- The power set of a set A, denoted by P(A), is the set of all subsets of A. For example, if A = {a, b, c}, then P(A) = {∅, {a}, {b}, {c}, {a, b}, {a, c}, {b, c}, {a, b, c}}.
- The cardinality of a set A, denoted by |A|, is the number of elements in A. For example, |{a, b, c}| = 3. The cardinality of the power set of A is 2^|A|. For example, |P({a, b, c})| = 2^3 = 8.