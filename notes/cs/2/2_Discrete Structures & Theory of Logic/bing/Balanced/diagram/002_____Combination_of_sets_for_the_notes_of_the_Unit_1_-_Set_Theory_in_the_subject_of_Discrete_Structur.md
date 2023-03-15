### Combination of sets

- A combination of sets is a new set that is formed by applying some operation on two or more given sets.
- There are four basic operations on sets: union, intersection, difference and complement.
- The union of two sets A and B, denoted by A ∪ B, is the set of all elements that belong to either A or B or both. For example, if A = {1, 2, 3} and B = {3, 4, 5}, then A ∪ B = {1, 2, 3, 4, 5}.
- The intersection of two sets A and B, denoted by A ∩ B, is the set of all elements that belong to both A and B. For example, if A = {1, 2, 3} and B = {3, 4, 5}, then A ∩ B = {3}.
- The difference of two sets A and B, denoted by A - B, is the set of all elements that belong to A but not to B. For example, if A = {1, 2, 3} and B = {3, 4, 5}, then A - B = {1, 2}.
- The complement of a set A, denoted by A', is the set of all elements that do not belong to A. The complement of a set is relative to some universal set U, which contains all the elements under consideration. For example, if U = {1, 2, 3, 4, 5, 6} and A = {1, 2, 3}, then A' = {4, 5, 6}.
- The operations on sets can be represented by Venn diagrams, which are circles that show the relationship between sets. For example, the following diagram shows the union, intersection, difference and complement of two sets A and B.

```text
    A ∪ B     A ∩ B     A - B     A' 
   _____     _____     _____     _____
  |     |   |     |   |     |   |     |
  |  A  |   |  A  |   |  A  |   |  U  |
  | /\  |   | /\  |   | /\  |   | /\  |
  |/  \ |   |/  \ |   |/  \ |   |/  \ |
  |  B  |   |  B  |   |  B  |   |  B  |
  |_____|   |_____|   |_____|   |_____|
```
- The operations on sets are associative, commutative and distributive. For example, for any sets A, B and C, we have:

  - (A ∪ B) ∪ C = A ∪ (B ∪ C) and (A ∩ B) ∩ C = A ∩ (B ∩ C) (associative laws)
  - A ∪ B = B ∪ A and A ∩ B = B ∩ A (commutative laws)
  - A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C) and A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C) (distributive laws)

- The operations on sets also obey some other properties, such as:

  - A ∪ A = A and A ∩ A = A (idempotent laws)
  - A ∪ U = U and A ∩ U = A (identity laws)
  - A ∪ A' = U and A ∩ A' = ∅ (complement laws)
  - A ∪ ∅ = A and A ∩ ∅ = ∅ (empty set laws)
  - (A ∪ B)' = A' ∩ B' and (A ∩ B)' = A' ∪ B' (De Morgan's laws)
  - (A')' = A (double complement law)