### Properties of fuzzy sets

- A fuzzy set is a set where each element has a degree of membership, which is often represented by a number between 0 and 1, where 0 means the element is not a member of the set, and 1 means the element is a member of the set.
- Fuzzy sets can be considered as an extension and gross oversimplification of classical sets, which allow only binary membership (0 or 1).
- Fuzzy sets have many useful properties, such as :
  - **Involution**: The complement of the complement of a fuzzy set is the set itself, i.e., `~(~A) = A`.
  - **Commutativity**: The order of operands does not alter the result of fuzzy set operations, i.e., `A ∪ B = B ∪ A` and `A ∩ B = B ∩ A`.
  - **Associativity**: The order of operations performed on fuzzy sets can be changed, but the relative order of the operands cannot be changed, i.e., `(A ∪ B) ∪ C = A ∪ (B ∪ C)` and `(A ∩ B) ∩ C = A ∩ (B ∩ C)`.
  - **Distributivity**: Fuzzy set operations can be distributed over each other, i.e., `A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C)` and `A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C)`.
  - **Absorption**: A fuzzy set absorbs another fuzzy set if the union or intersection of them is equal to the first set, i.e., `A ∪ (A ∩ B) = A` and `A ∩ (A ∪ B) = A`.
  - **Idempotency / Tautology**: The union or intersection of a fuzzy set with itself is equal to the set itself, i.e., `A ∪ A = A` and `A ∩ A = A`.
  - **Identity**: The union or intersection of a fuzzy set with the universal set or the empty set is equal to the universal set or the fuzzy set itself, i.e., `A ∪ U = U` and `A ∪ ∅ = A`, and `A ∩ U = A` and `A ∩ ∅ = ∅`.
  - **Transitivity**: A fuzzy relation is transitive if the degree of membership of any pair of elements is equal to or greater than the minimum degree of membership of any other pair of elements that are related to the first pair, i.e., `μR(x,z) ≥ min(μR(x,y), μR(y,z))` for all `x, y, z`.