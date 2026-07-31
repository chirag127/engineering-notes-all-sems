### Lossless Join Decomposition

- Lossless join decomposition is a process of splitting a relation R into two or more relations R1, R2, ... such that the natural join of the smaller relations gives back the original relation R  .
- Lossless join decomposition is desirable because it eliminates redundancy and anomalies from the relation R without losing any information .
- Lossless join decomposition can be verified by using the following criteria:
  - Let F be the set of functional dependencies that hold on R, and F+ be the closure of F.
  - The decomposition of R into R1, R2, ... is lossless if and only if for every pair of relations Ri and Rj, one of the following functional dependencies is in F+:
    - Ri ∩ Rj → Ri
    - Ri ∩ Rj → Rj
    - Ri ∩ Rj → Ri ∪ Rj
- Lossless join decomposition can also be achieved by using decomposition algorithms based on normal forms, such as BCNF and 3NF. These algorithms ensure that the decomposed relations are free of redundancy and preserve the dependencies of the original relation.