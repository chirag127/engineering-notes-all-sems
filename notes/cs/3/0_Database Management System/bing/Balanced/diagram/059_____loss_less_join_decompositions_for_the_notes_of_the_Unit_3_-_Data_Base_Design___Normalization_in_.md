### Lossless Join Decomposition

- Lossless join decomposition is a process of splitting a relation R into two or more relations R1, R2, ... such that the natural join of the smaller relations gives back the original relation R.
- Lossless join decomposition is desirable because it avoids the problems of extra or missing tuples that may occur in a lossy decomposition, and preserves the original information in R.
- Lossless join decomposition can be checked using the following criteria:

  - Let R be a relation with a set of functional dependencies F, and let R1 and R2 be a decomposition of R.
  - The decomposition is lossless if and only if one of the following functional dependencies holds in F+ (the closure of F):
    - R1 ∩ R2 → R1
    - R1 ∩ R2 → R2
  - Alternatively, the decomposition is lossless if and only if the common attributes of R1 and R2 form a superkey for either R1 or R2.

- Lossless join decomposition can be achieved by using decomposition algorithms based on normal forms, such as BCNF and 3NF, which ensure that the decomposed relations are free of redundancy and anomalies.