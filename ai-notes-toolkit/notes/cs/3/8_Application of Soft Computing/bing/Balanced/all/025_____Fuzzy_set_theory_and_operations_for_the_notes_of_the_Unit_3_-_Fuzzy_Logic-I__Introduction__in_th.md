# Fuzzy set theory and operations

## Fuzzy set theory

- Fuzzy set theory is a branch of mathematics that deals with sets whose elements have degrees of membership.
- Fuzzy sets are a generalization of crisp sets, which are sets whose elements have binary membership (either 0 or 1).
- Fuzzy sets were introduced by Lotfi A. Zadeh in 1965 as an extension of the classical notion of set.
- Fuzzy sets can be used to model uncertainty, vagueness, ambiguity, and imprecision in various domains, such as logic, control, decision making, pattern recognition, linguistics, and so on .

## Fuzzy set operations

- Fuzzy set operations are operations that can be performed on fuzzy sets, such as union, intersection, complement, algebraic product, and algebraic sum.
- Fuzzy set operations are a generalization of crisp set operations, which are operations that can be performed on crisp sets, such as union, intersection, complement, Cartesian product, and power set.
- There are different ways to define fuzzy set operations, but the most widely used ones are called standard fuzzy set operations.
- Standard fuzzy set operations are based on the following formulas, where A ~ and B ~ are fuzzy sets, U is the universe of discourse, and x is an element of U :

  - Fuzzy union (or fuzzy OR): (A ~ ∪ B ~)(x) = max(A ~(x), B ~(x))
  - Fuzzy intersection (or fuzzy AND): (A ~ ∩ B ~)(x) = min(A ~(x), B ~(x))
  - Fuzzy complement (or fuzzy NOT): (A ~')(x) = 1 - A ~(x)
  - Fuzzy algebraic product: (A ~ · B ~)(x) = A ~(x) · B ~(x)
  - Fuzzy algebraic sum: (A ~ + B ~)(x) = A ~(x) + B ~(x) - A ~(x) · B ~(x)

- Fuzzy set operations have some properties that are similar to crisp set operations, such as commutativity, associativity, idempotency, and distributivity.
- Fuzzy set operations also have some properties that are different from crisp set operations, such as non-existence of null set, non-existence of universal set, non-existence of De Morgan's laws, and non-existence of absorption laws.

## References

: Chapter 1 Fuzzy set - IIT Kharagpur
: Fuzzy Logic - Set Theory - tutorialspoint.com
: Fuzzy set operations - Wikipedia
: Fuzzy set - Wikipedia
: Common Operations on Fuzzy Set with Example and Code - geeksforgeeks.org