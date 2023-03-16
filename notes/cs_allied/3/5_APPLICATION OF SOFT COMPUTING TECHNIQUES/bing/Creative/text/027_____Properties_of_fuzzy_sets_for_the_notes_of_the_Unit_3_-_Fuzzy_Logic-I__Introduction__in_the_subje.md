### Properties of fuzzy sets

- A fuzzy set is a set where each element has a degree of membership, which is a number between 0 and 1, where 0 means the element is not a member of the set, and 1 means the element is a member of the set.
- Fuzzy sets can be considered as an extension and gross oversimplification of classical sets, which allow only binary membership (0 or 1) .
- Fuzzy sets have many useful properties, such as  :
  - **Closure**: A fuzzy set is closed if, for any element x, the membership degree of x is equal to the membership degree of the set.
  - **Involution**: Involution states that the complement of complement is set itself. The complement of a fuzzy set A is denoted by A' and is defined as A'(x) = 1 - A(x) for all x.
  - **Commutativity**: Operations are called commutative if the order of operands does not alter the result. Fuzzy sets are commutative under union, intersection, and complement operations.
  - **Associativity**: Associativity allows change in the order of operations performed on an operand, however relative order of the operand can not be changed. Fuzzy sets are associative under union and intersection operations.
  - **Distributivity**: Distributivity allows change in the grouping of operands. Fuzzy sets are distributive under union and intersection operations.
  - **Absorption**: Absorption states that union of a set with intersection of itself and any other set is the set itself. Similarly, intersection of a set with union of itself and any other set is the set itself. Fuzzy sets follow the absorption property.
  - **Idempotency / Tautology**: Idempotency states that union of a set with itself is the set itself. Similarly, intersection of a set with itself is the set itself. Fuzzy sets follow the idempotency property.
  - **Identity**: Identity states that union of a set with an empty set is the set itself. Similarly, intersection of a set with a universal set is the set itself. Fuzzy sets follow the identity property.
  - **Transitivity**: Transitivity states that if a set A is a subset of set B and set B is a subset of set C, then set A is a subset of set C. Fuzzy sets follow the transitivity property. A fuzzy set A is a subset of another fuzzy set B if A(x) <= B(x) for all x.
- A fuzzy variable is a variable that can take fuzzy values, which are fuzzy sets defined on a universe of discourse. A fuzzy variable may have three, five, or seven fuzzy values, such as NB (negative big), ZE (zero), and PB (positive big) .
- A membership function is a function that assigns a degree of membership to each element of a fuzzy set. A membership function can be represented as a graph, a table, or a mathematical expression .