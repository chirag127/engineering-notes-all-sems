# Proofs of some general identities on sets

Here are some general identities on sets and their proofs:

1. **Commutative Laws**: For any sets A and B, A ∪ B = B ∪ A and A ∩ B = B ∩ A.

Proof: Let x ∈ A ∪ B. Then x ∈ A or x ∈ B. This means that x ∈ B or x ∈ A, which implies that x ∈ B ∪ A. Hence, A ∪ B ⊆ B ∪ A. Similarly, B ∪ A ⊆ A ∪ B, so A ∪ B = B ∪ A. The proof for A ∩ B = B ∩ A is similar.

2. **Associative Laws**: For any sets A, B, and C, (A ∪ B) ∪ C = A ∪ (B ∪ C) and (A ∩ B) ∩ C = A ∩ (B ∩ C).

Proof: Let x ∈ (A ∪ B) ∪ C. Then x ∈ A ∪ B or x ∈ C. If x ∈ A ∪ B, then x ∈ A or x ∈ B. In either case, x ∈ A or x ∈ B ∪ C, which implies that x ∈ A ∪ (B ∪ C). If x ∈ C, then x ∈ B ∪ C, which implies that x ∈ A ∪ (B ∪ C). Hence, (A ∪ B) ∪ C ⊆ A ∪ (B ∪ C). Similarly, A ∪ (B ∪ C) ⊆ (A ∪ B) ∪ C, so (A ∪ B) ∪ C = A ∪ (B ∪ C). The proof for (A ∩ B) ∩ C = A ∩ (B ∩ C) is similar.

3. **Distributive Laws**: For any sets A, B, and C, A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C) and A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C).

Proof: Let x ∈ A ∪ (B ∩ C). Then x ∈ A or x ∈ B ∩ C. If x ∈ A, then x ∈ A ∪ B and x ∈ A ∪ C, which implies that x ∈ (A ∪ B) ∩ (A ∪ C). If x ∈ B ∩ C, then x ∈ B and x ∈ C, which implies that x ∈ A ∪ B and x ∈ A ∪ C, and hence x ∈ (A ∪ B) ∩ (A ∪ C). Hence, A ∪ (B ∩ C) ⊆ (A ∪ B) ∩ (A ∪ C). Similarly, (A ∪ B) ∩ (A ∪ C) ⊆ A ∪ (B ∩ C), so A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C). The proof for A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C) is similar.
