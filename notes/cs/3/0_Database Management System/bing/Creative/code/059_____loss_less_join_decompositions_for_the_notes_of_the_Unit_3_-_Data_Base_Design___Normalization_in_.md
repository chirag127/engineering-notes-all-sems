### Lossless Join Decomposition

- Lossless join decomposition is a process of decomposing a relation R into two or more relations R1, R2, ... such that a natural join of the smaller relations yields back the original relation R  .
- Lossless join decomposition is important for removing redundancy and anomalies from databases while preserving the original data.
- Lossless join decomposition can be checked using functional dependencies or decomposition algorithms .
- A decomposition of R into R1 and R2 is lossless if at least one of the following functional dependencies holds in the closure of the given set of functional dependencies F :
  - R1 ∩ R2 → R1
  - R1 ∩ R2 → R2
- A decomposition of R into R1, R2, ... Rn is lossless if the decomposition of R into R1 and R2 is lossless, and the decomposition of R2 into R3 and R4 is lossless, and so on.
- Some decomposition algorithms that guarantee lossless join decomposition are BCNF (Boyce-Codd Normal Form) and 3NF (Third Normal Form) .