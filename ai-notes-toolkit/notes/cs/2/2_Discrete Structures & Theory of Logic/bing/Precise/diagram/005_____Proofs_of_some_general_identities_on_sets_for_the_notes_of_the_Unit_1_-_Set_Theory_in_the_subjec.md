### Proofs of some general identities on sets for the notes of the Unit 1 - Set Theory in the subject of Discrete Structures & Theory of Logic

1. **Commutative Laws**: For any two sets A and B, A ∪ B = B ∪ A and A ∩ B = B ∩ A.
    - Proof: Let x ∈ A ∪ B. Then x ∈ A or x ∈ B. This is equivalent to saying that x ∈ B or x ∈ A, which means x ∈ B ∪ A. Hence, A ∪ B ⊆ B ∪ A. Similarly, B ∪ A ⊆ A ∪ B. Thus, A ∪ B = B ∪ A. The proof for the intersection is similar.

2. **Associative Laws**: For any three sets A, B, and C, (A ∪ B) ∪ C = A ∪ (B ∪ C) and (A ∩ B) ∩ C = A ∩ (B ∩ C).
    - Proof: Let x ∈ (A ∪ B) ∪ C. Then x ∈ A ∪ B or x ∈ C. If x ∈ A ∪ B, then x ∈ A or x ∈ B. In either case, x ∈ A or x ∈ B ∪ C, which means x ∈ A ∪ (B ∪ C). If x ∈ C, then x ∈ B ∪ C, which means x ∈ A ∪ (B ∪ C). Hence, (A ∪ B) ∪ C ⊆ A ∪ (B ∪ C). Similarly, A ∪ (B ∪ C) ⊆ (A ∪ B) ∪ C. Thus, (A ∪ B) ∪ C = A ∪ (B ∪ C). The proof for the intersection is similar.

3. **Distributive Laws**: For any three sets A, B, and C, A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C) and A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C).
    - Proof: Let x ∈ A ∪ (B ∩ C). Then x ∈ A or x ∈ B ∩ C. If x ∈ A, then x ∈ A ∪ B and x ∈ A ∪ C, which means x ∈ (A ∪ B) ∩ (A ∪ C). If x ∈ B ∩ C, then x ∈ B and x ∈ C. In either case, x ∈ A ∪ B and x ∈ A ∪ C, which means x ∈ (A ∪ B) ∩ (A ∪ C). Hence, A ∪ (B ∩ C) ⊆ (A ∪ B) ∩ (A ∪ C). Similarly, (A ∪ B) ∩ (A ∪ C) ⊆ A ∪ (B ∩ C). Thus, A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C). The proof for the intersection is similar.

4. **De Morgan's Laws**: For any two sets A and B, (A ∪ B)' = A' ∩ B' and (A ∩ B)' = A' ∪ B'.
    - Proof: Let x ∈ (A ∪ B)'. Then x ∉ A ∪ B, which means x ∉ A and x ∉ B. This is equivalent to saying that x ∈ A' and x ∈ B', which means x ∈ A' ∩ B'. Hence, (A ∪ B)' ⊆ A' ∩ B'. Similarly, A' ∩ B' ⊆ (A ∪ B)'. Thus, (A ∪ B)' = A' ∩ B'. The proof for the intersection is similar.
