### Lossless Join Decomposition

- Lossless join decomposition is a process of splitting a relation R into two or more relations R1, R2, ... such that the natural join of the smaller relations gives back the original relation R.
- Lossless join decomposition is important for removing redundancy and anomalies from databases while preserving the original data .
- Lossless join decomposition can be checked using the following criteria :
  - Let F be the set of functional dependencies that hold on R, and F+ be the closure of F.
  - Let R1 and R2 be the decomposed relations of R, and R1 ∩ R2 be the set of common attributes between them.
  - The decomposition is lossless if at least one of the following functional dependencies are in F+:
    - R1 ∩ R2 → R1
    - R1 ∩ R2 → R2
- Lossless join decomposition can also be achieved by using decomposition algorithms such as BCNF and 3NF, which are based on the concept of normal forms.