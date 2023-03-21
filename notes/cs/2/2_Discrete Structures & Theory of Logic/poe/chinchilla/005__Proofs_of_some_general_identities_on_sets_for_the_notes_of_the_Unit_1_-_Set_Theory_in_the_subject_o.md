### Proofs of Some General Identities on Sets

In the study of set theory, it is important to be able to prove various identities and properties of sets. Here are some general identities on sets that are commonly used, along with their proofs:

#### Union and Intersection Distributivity

- **Identity:** For any sets A, B, and C, we have:
  - A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C)
  - A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C)
  
- **Proof of the first identity:**
  - Let x be an arbitrary element of A ∪ (B ∩ C).
  - Then, either x ∈ A or x ∈ B ∩ C.
  - If x ∈ A, then x ∈ A ∪ B and x ∈ A ∪ C, so x ∈ (A ∪ B) ∩ (A ∪ C).
  - If x ∈ B ∩ C, then x ∈ B and x ∈ C, so x ∈ A ∪ B and x ∈ A ∪ C, and again x ∈ (A ∪ B) ∩ (A ∪ C).
  - Therefore, A ∪ (B ∩ C) ⊆ (A ∪ B) ∩ (A ∪ C).
  
  - Now, let y be an arbitrary element of (A ∪ B) ∩ (A ∪ C).
  - Then, y ∈ A ∪ B and y ∈ A ∪ C.
  - If y ∈ A, then y ∈ A ∪ (B ∩ C).
  - If y ∈ B, then y ∈ A ∪ B, so y ∉ A ∩ C, and therefore y ∉ B ∩ C, which means y ∉ A ∪ (B ∩ C).
  - If y ∈ C, then y ∈ A ∪ C, so y ∉ A ∩ B, and therefore y ∉ B ∩ C, which means y ∉ A ∪ (B ∩ C).
  - Therefore, (A ∪ B) ∩ (A ∪ C) ⊆ A ∪ (B ∩ C).
  
  - Since we have shown both directions of the inclusion, we can conclude that A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C).
  
- **Proof of the second identity:** (similar to the first one)

#### De Morgan's Laws

- **Identity:** For any sets A and B, we have:
  - (A ∪ B)' = A' ∩ B'
  - (A ∩ B)' = A' ∪ B'
  
- **Proof of the first identity:**
  - Let x be an arbitrary element of (A ∪ B)'.
  - Then, x ∉ A ∪ B, which means x ∉ A and x ∉ B.
  - Therefore, x ∈ A' and x ∈ B', so x ∈ A' ∩ B'.
  - Therefore, (A ∪ B)' ⊆ A' ∩ B'.
  
  - Now, let y be an arbitrary element of A' ∩ B'.
  - Then, y ∈ A' and y ∈ B'.
  - Therefore, y ∉ A and y ∉ B, so y ∉ A ∪ B, which means y ∈ (A ∪ B)'.
  - Therefore, A' ∩ B' ⊆ (A ∪ B)'.
  
  - Since we have shown both directions of the inclusion, we can conclude that (A ∪ B)' = A' ∩ B'.
  
- **Proof of the second identity:** (similar to the first one)

#### Set Difference

- **Identity:** For any sets A, B, and C, we have:
  - A \ (B ∪ C) = (A \ B) ∩ (A \ C)
  
- **Proof:**
  - Let x be an arbitrary element of A \ (B ∪ C).
  - Then, x ∈ A and x ∉ B ∪ C.
  - Therefore, x ∉ B and x ∉ C, so x ∈ A \ B and x ∈ A \ C.
  - Therefore, x ∈ (A \ B) ∩ (A \ C).
  - Therefore, A \ (B ∪ C) ⊆ (A \ B) ∩ (A \ C).
  
  - Now, let y be an arbitrary element of (A \ B) ∩ (A \ C).
  - Then, y ∈ A \ B and y ∈ A \ C.
  - Therefore, y ∈ A and y ∉ B ∪ C, so y ∈ A \ (B