### Proofs of some general identities on sets for the notes of the Unit 1 - Set Theory in the subject of Discrete Structures & Theory of Logic

1. **Commutative Laws**: For any sets A and B, A ∪ B = B ∪ A and A ∩ B = B ∩ A.
    - Proof: Let x ∈ A ∪ B. Then x ∈ A or x ∈ B. This is equivalent to saying that x ∈ B or x ∈ A, which means that x ∈ B ∪ A. Thus, A ∪ B ⊆ B ∪ A. Similarly, B ∪ A ⊆ A ∪ B, so A ∪ B = B ∪ A. The proof for A ∩ B = B ∩ A is similar.

2. **Associative Laws**: For any sets A, B, and C, (A ∪ B) ∪ C = A ∪ (B ∪ C) and (A ∩ B) ∩ C = A ∩ (B ∩ C).
    - Proof: Let x ∈ (A ∪ B) ∪ C. Then x ∈ A ∪ B or x ∈ C. This means that (x ∈ A or x ∈ B) or x ∈ C. By the associative law for logical disjunction, this is equivalent to x ∈ A or (x ∈ B or x ∈ C), which means that x ∈ A ∪ (B ∪ C). Thus, (A ∪ B) ∪ C ⊆ A ∪ (B ∪ C). Similarly, A ∪ (B ∪ C) ⊆ (A ∪ B) ∪ C, so (A ∪ B) ∪ C = A ∪ (B ∪ C). The proof for (A ∩ B) ∩ C = A ∩ (B ∩ C) is similar.

3. **Distributive Laws**: For any sets A, B, and C, A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C) and A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C).
    - Proof: Let x ∈ A ∪ (B ∩ C). Then x ∈ A or x ∈ B ∩ C. This means that x ∈ A or (x ∈ B and x ∈ C). By the distributive law for logical disjunction over conjunction, this is equivalent to (x ∈ A or x ∈ B) and (x ∈ A or x ∈ C), which means that x ∈ (A ∪ B) ∩ (A ∪ C). Thus, A ∪ (B ∩ C) ⊆ (A ∪ B) ∩ (A ∪ C). Similarly, (A ∪ B) ∩ (A ∪ C) ⊆ A ∪ (B ∩ C), so A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C). The proof for A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C) is similar.

4. **Identity Laws**: For any set A and the empty set ∅, A ∪ ∅ = A and A ∩ ∅ = ∅.
    - Proof: Let x ∈ A ∪ ∅. Then x ∈ A or x ∈ ∅. Since ∅ has no elements, x ∈ ∅ is always false, so x ∈ A. Thus, A ∪ ∅ ⊆ A. Similarly, A ⊆ A ∪ ∅, so A ∪ ∅ = A. For the second identity, let x ∈ A ∩ ∅. Then x ∈ A and x ∈ ∅. Since ∅ has no elements, this is impossible, so A ∩ ∅ = ∅.

5. **Complement Laws**: For any set A and the universal set U, A ∪ A' = U and A ∩ A' = ∅.
    - Proof: Let x ∈ A ∪ A'. Then x ∈ A or x ∈ A'. Since A' is the set of all elements in U that are not in A, this means that x is either in A or not in A. Since every element in U is either in A or not in A, this means that x ∈ U. Thus, A ∪ A' ⊆ U. Similarly, U ⊆ A ∪ A', so A ∪ A' = U. For the second identity, let x ∈ A ∩ A'. Then x ∈ A and