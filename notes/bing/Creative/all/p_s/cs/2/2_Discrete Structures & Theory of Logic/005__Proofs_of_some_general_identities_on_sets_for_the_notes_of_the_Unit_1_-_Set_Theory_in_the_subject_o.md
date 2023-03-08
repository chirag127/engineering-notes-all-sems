### Proofs of some general identities on sets

A set identity is a statement that two sets are equal, that is, they have the same elements. For example, one of the set identities is:

- A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C)

To prove a set identity, we need to show that every element of the left-hand side is also an element of the right-hand side, and vice versa. This is called the element method or the method of double inclusion.

Here are some examples of how to prove some general identities on sets using the element method:

- Identity: A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C)
- Proof: Let x be an arbitrary element of A ∩ (B ∪ C). Then x ∈ A and x ∈ B ∪ C. This means that x ∈ A and (x ∈ B or x ∈ C). By the distributive property of logical or, this is equivalent to (x ∈ A and x ∈ B) or (x ∈ A and x ∈ C). This means that x ∈ (A ∩ B) ∪ (A ∩ C). Therefore, A ∩ (B ∪ C) ⊆ (A ∩ B) ∪ (A ∩ C).

Conversely, let x be an arbitrary element of (A ∩ B) ∪ (A ∩ C). Then x ∈ A ∩ B or x ∈ A ∩ C. This means that (x ∈ A and x ∈ B) or (x ∈ A and x ∈ C). By the distributive property of logical or, this is equivalent to x ∈ A and (x ∈ B or x ∈ C). This means that x ∈ A and x ∈ B ∪ C. Therefore, x ∈ A ∩ (B ∪ C). Hence, (A ∩ B) ∪ (A ∩ C) ⊆ A ∩ (B ∪ C).

Since we have shown that both sets are subsets of each other, we can conclude that they are equal. QED.

- Identity: A ∪ (A ∩ B) = A
- Proof: Let x be an arbitrary element of A ∪ (A ∩ B). Then x ∈ A or x ∈ A ∩ B. This means that x ∈ A or (x ∈ A and x ∈ B). By the absorption property of logical or, this is equivalent to x ∈ A. Therefore, A ∪ (A ∩ B) ⊆ A.

Conversely, let x be an arbitrary element of A. Then x ∈ A. This means that x ∈ A or x ∈ A ∩ B. Therefore, x ∈ A ∪ (A ∩ B). Hence, A ⊆ A ∪ (A ∩ B).

Since we have shown that both sets are subsets of each other, we can conclude that they are equal. QED.

- Identity: A ∩ (A ∪ B) = A
- Proof: Let x be an arbitrary element of A ∩ (A ∪ B). Then x ∈ A and x ∈ A ∪ B. This means that x ∈ A and (x ∈ A or x ∈ B). By the absorption property of logical and, this is equivalent to x ∈ A. Therefore, A ∩ (A ∪ B) ⊆ A.

Conversely, let x be an arbitrary element of A. Then x ∈ A. This means that x ∈ A and x ∈ A ∪ B. Therefore, x ∈ A ∩ (A ∪ B). Hence, A ⊆ A ∩ (A ∪ B).

Since we have shown that both sets are subsets of each other, we can conclude that they are equal. QED.

Some possible mnemonics and learning tricks for the topic are:

- To remember the distributive property of set operations, you can use the acronym DORA, which stands for Distribute Over, Remove And. This means that when you have a set operation that involves an intersection inside a union or vice versa, you can distribute the outer operation over the inner one and remove the and symbol. For example, A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C) can be remembered as DORA: Distribute ∪ over ∩, Remove and.
- To remember the absorption property of set operations, you can use the acronym ABA, which stands for Absorb, Be, Alone. This means that when you have a set operation that involves a set and its intersection or union with another set, you can absorb the other set and be alone. For example, A ∪ (A ∩ B) = A can be remembered as ABA: Absorb A ∩ B, Be A, Alone.
- To remember the complement property of set operations, you can use the acronym CAC, which stands for Complement, And, Complement. This means that when you have a set operation that involves a complement of a set and another set, you can complement both sets and change the operation to its opposite. For example, A' ∪ B = (A ∩ B')' can be remembered as CAC: Complement A and B, And, Complement.