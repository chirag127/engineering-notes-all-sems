# Fuzzy set theory and operations

## Fuzzy set theory

- Fuzzy set theory is a branch of mathematics that deals with sets whose elements have degrees of membership.
- Fuzzy sets are a generalization of crisp sets, which are sets whose elements have binary membership (either 0 or 1).
- Fuzzy sets were introduced by Lotfi A. Zadeh in 1965 as an extension of the classical notion of set.
- Fuzzy sets can be used to model uncertainty, vagueness, ambiguity, and imprecision in various domains, such as logic, control, decision making, pattern recognition, linguistics, etc. .

## Fuzzy set operations

- Fuzzy set operations are operations that can be performed on fuzzy sets, such as union, intersection, complement, algebraic product, and algebraic sum  .
- Fuzzy set operations are a generalization of crisp set operations, which are operations that can be performed on crisp sets, such as union, intersection, complement, Cartesian product, and power set.
- There are different ways to define fuzzy set operations, but the most widely used ones are called standard fuzzy set operations.
- Standard fuzzy set operations are based on the following relations, where A ~ and B ~ are fuzzy sets, U is the universe of discourse, and x is an element of U :

  - Union/Fuzzy OR: (A ~ ∪ B ~)(x) = max(A ~(x), B ~(x))
  - Intersection/Fuzzy AND: (A ~ ∩ B ~)(x) = min(A ~(x), B ~(x))
  - Complement/Fuzzy NOT: (A ~')(x) = 1 - A ~(x)
  - Algebraic product: (A ~ · B ~)(x) = A ~(x) · B ~(x)
  - Algebraic sum: (A ~ + B ~)(x) = A ~(x) + B ~(x) - A ~(x) · B ~(x)

- Fuzzy set operations can be used to combine, modify, or compare fuzzy sets, and to perform fuzzy reasoning and inference  .

: https://cse.iitkgp.ac.in/~dsamanta/courses/archive/sca/Archives/Chapter%201%20Fuzzy%20set.pdf
: https://www.tutorialspoint.com/fuzzy_logic/fuzzy_logic_set_theory.htm
: https://en.wikipedia.org/wiki/Fuzzy_set_operations
: https://en.wikipedia.org/wiki/Fuzzy_set
: https://www.geeksforgeeks.org/common-operations-on-fuzzy-set-with-example-and-code/