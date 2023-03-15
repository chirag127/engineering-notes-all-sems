# Lossless Join Decomposition

- Lossless join decomposition is a process of splitting a relation R into two or more relations R1, R2, ... such that the natural join of the smaller relations gives back the original relation R.
- Lossless join decomposition is important for database design and normalization, as it helps to remove redundancy and anomalies from the database while preserving the original data .
- A decomposition of R into R1 and R2 is lossless if and only if one of the following functional dependencies holds in the closure of the set of functional dependencies F of R :
  - R1 ∩ R2 → R1
  - R1 ∩ R2 → R2
- The above condition can be checked using Armstrong's axioms or by constructing a table with the attributes of R as columns and the attributes of R1 and R2 as rows. The table is then filled with the values of R1 and R2, and the natural join of R1 and R2 is obtained by combining the rows with the same values in the common attributes.
- Lossless join decomposition can be achieved by using decomposition algorithms such as BCNF or 3NF, which ensure that the decomposed relations are in a higher normal form and satisfy the lossless join property.