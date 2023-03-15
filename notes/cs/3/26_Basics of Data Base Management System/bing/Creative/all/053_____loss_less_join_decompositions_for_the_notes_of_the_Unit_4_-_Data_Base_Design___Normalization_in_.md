# Lossless Join Decomposition

- Lossless join decomposition is a process of splitting a relation R into two or more relations R1, R2, ... such that the natural join of R1, R2, ... gives back the original relation R. 
- Lossless join decomposition is important for removing redundancy and anomalies from databases while preserving the original data.  
- Lossless join decomposition is also known as non-additive join decomposition. 
- A decomposition of R into R1 and R2 is lossless if and only if one of the following functional dependencies holds in the closure of the set of functional dependencies of R:  
  - R1 ∩ R2 → R1
  - R1 ∩ R2 → R2
- The above condition can be checked using the chase algorithm, which is a method of applying the functional dependencies to a test relation until a fixed point is reached.  
- If the decomposition is lossless, the test relation will have the same number of tuples as the original relation R. Otherwise, the decomposition is lossy and some tuples will be added or deleted.  

## Examples

- Consider the relation R(A, B, C) with the functional dependencies A → B and B → C. A possible decomposition of R is R1(A, B) and R2(B, C). This decomposition is lossless because R1 ∩ R2 = B and B → R1.  
- Consider the relation R(A, B, C, D) with the functional dependencies A → B and C → D. A possible decomposition of R is R1(A, B) and R2(C, D). This decomposition is lossy because R1 ∩ R2 = ∅ and there is no functional dependency involving the empty set.