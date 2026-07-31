### Lossless Join Decomposition

- Lossless join decomposition is a process of decomposing a relation R into two or more relations R1, R2, ... such that a natural join of the smaller relations yields back the original relation R  .
- This property guarantees that no information is lost from the original relation during the decomposition and that no spurious tuples are generated .
- Lossless join decomposition is essential for removing redundancy and anomalies from databases while preserving the original data .
- A decomposition of R into R1 and R2 is lossless if and only if at least one of the following functional dependencies holds in the closure of the set of functional dependencies of R  :
  - R1 ∩ R2 → R1
  - R1 ∩ R2 → R2
- The above condition can be checked using the following algorithm:
  - Create a table with R1 attributes as rows and R2 attributes as columns.
  - Mark the cells that correspond to the common attributes of R1 and R2 with the attribute name.
  - For each functional dependency X → Y in the closure of the set of functional dependencies of R, mark the cells that correspond to X and Y with the same symbol (e.g., *).
  - Repeat the previous step until no more cells can be marked.
  - If all the cells in a row or a column are marked with the same symbol, then the decomposition is lossless. Otherwise, it is lossy.