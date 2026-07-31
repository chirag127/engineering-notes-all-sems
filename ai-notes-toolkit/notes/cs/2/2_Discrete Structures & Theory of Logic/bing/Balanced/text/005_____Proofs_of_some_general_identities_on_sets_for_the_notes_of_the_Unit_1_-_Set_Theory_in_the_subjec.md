### Proofs of some general identities on sets

- A set is a collection of distinct objects, such as numbers, letters, or shapes.
- An identity is a statement that is true for all possible values of the variables involved, such as x + 0 = x or x * 1 = x.
- A set identity is a statement that is true for all possible sets involved, such as A ∪ ∅ = A or A ∩ A = A.
- To prove a set identity, we need to show that the two sets on either side of the equality sign have the same elements, that is, they are subsets of each other.
- One way to prove a set identity is to use the element method, which involves taking an arbitrary element from one set and showing that it belongs to the other set, and vice versa.
- Another way to prove a set identity is to use the set algebra method, which involves manipulating the sets using the definitions and properties of set operations, such as union, intersection, complement, and difference.
- Here are some examples of set identities and their proofs using both methods:

#### Identity 1: A ∪ A = A
- Element method: Let x be an arbitrary element of A ∪ A. Then x ∈ A or x ∈ A, by the definition of union. But this implies that x ∈ A, by the law of excluded middle. Therefore, A ∪ A ⊆ A. Conversely, let x be an arbitrary element of A. Then x ∈ A and x ∈ A, by the reflexivity of equality. Therefore, x ∈ A ∪ A, by the definition of union. Hence, A ⊆ A ∪ A. Since we have shown that A ∪ A ⊆ A and A ⊆ A ∪ A, we can conclude that A ∪ A = A, by the definition of set equality.
- Set algebra method: A ∪ A = A ∪ (A ∩ A), by the identity property of intersection. Then, A ∪ A = (A ∪ A) ∩ (A ∪ A), by the distributive law of union over intersection. Finally, A ∪ A = A, by the idempotent law of union.

#### Identity 2: A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C)
- Element method: Let x be an arbitrary element of A ∩ (B ∪ C). Then x ∈ A and x ∈ B ∪ C, by the definition of intersection. This means that x ∈ A and (x ∈ B or x ∈ C), by the definition of union. Therefore, (x ∈ A and x ∈ B) or (x ∈ A and x ∈ C), by the distributive law of and over or. Hence, x ∈ (A ∩ B) ∪ (A ∩ C), by the definitions of intersection and union. Therefore, A ∩ (B ∪ C) ⊆ (A ∩ B) ∪ (A ∩ C). Conversely, let x be an arbitrary element of (A ∩ B) ∪ (A ∩ C). Then x ∈ A ∩ B or x ∈ A ∩ C, by the definition of union. This means that (x ∈ A and x ∈ B) or (x ∈ A and x ∈ C), by the definition of intersection. Therefore, x ∈ A and (x ∈ B or x ∈ C), by the distributive law of and over or. Hence, x ∈ A ∩ (B ∪ C), by the definitions of intersection and union. Thus, (A ∩ B) ∪ (A ∩ C) ⊆ A ∩ (B ∪ C). Since we have shown that A ∩ (B ∪ C) ⊆ (A ∩ B) ∪ (A ∩ C) and (A ∩ B) ∪ (A ∩ C) ⊆ A ∩ (B ∪ C), we can conclude that A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C), by the definition of set equality.
- Set algebra method: A ∩ (B ∪ C) = (A ∩ A) ∩ (B ∪ C), by the identity property of intersection. Then, A ∩ (B ∪ C) = A ∩ [(A ∩ B) ∪ (A ∩ C)], by the distributive law of intersection over union. Finally, A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C), by the absorption law of intersection.