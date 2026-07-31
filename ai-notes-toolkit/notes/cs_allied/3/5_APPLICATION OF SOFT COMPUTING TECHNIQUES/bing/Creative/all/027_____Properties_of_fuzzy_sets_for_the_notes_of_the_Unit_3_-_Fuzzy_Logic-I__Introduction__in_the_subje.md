# Properties of fuzzy sets

A fuzzy set is a set where each element has a degree of membership. This degree is often represented by a number between 0 and 1, where 0 means the element is not a member of the set, and 1 means the element is a member of the set.

Fuzzy sets have many useful properties, including:

- **Closure**: A fuzzy set is closed if, for any element x, the membership degree of x is equal to the membership degree of the set.
- **Involution**: Involution states that the complement of complement is set itself. The complement of a fuzzy set A is denoted by A' and is defined by A'(x) = 1 - A(x) for all x.
- **Commutativity**: Operations are called commutative if the order of operands does not alter the result. Fuzzy sets are commutative under union, intersection, and complement operations.
- **Associativity**: Associativity allows change in the order of operations performed on an operand, however relative order of the operand can not be changed. Fuzzy sets are associative under union and intersection operations.
- **Distributivity**: Distributivity allows change in the grouping of operands. Fuzzy sets are distributive under union and intersection operations.
- **Absorption**: Absorption states that A union (A intersection B) is equal to A, and A intersection (A union B) is equal to A, for any fuzzy sets A and B.
- **Idempotency / Tautology**: Idempotency states that A union A is equal to A, and A intersection A is equal to A, for any fuzzy set A.
- **Identity**: Identity states that A union 0 is equal to A, and A intersection 1 is equal to A, for any fuzzy set A, where 0 and 1 are the empty and universal sets, respectively.
- **Transitivity**: Transitivity states that if A is a subset of B, and B is a subset of C, then A is a subset of C, for any fuzzy sets A, B, and C.

These properties are similar to those of classical sets, but they are generalized to account for the degrees of membership of fuzzy sets. Fuzzy sets can be considered as an extension and gross oversimplification of classical sets.