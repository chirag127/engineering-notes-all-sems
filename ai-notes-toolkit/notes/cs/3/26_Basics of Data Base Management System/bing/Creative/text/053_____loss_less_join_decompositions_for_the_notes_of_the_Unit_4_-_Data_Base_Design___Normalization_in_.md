### Lossless Join Decomposition

- Lossless join decomposition is a process of splitting a relation R into two or more relations R1, R2, ... such that the natural join of the smaller relations gives back the original relation R   .
- Lossless join decomposition is important for removing redundancy and anomalies from databases while preserving the original data .
- Lossless join decomposition is based on the concept of functional dependencies, which are constraints that specify how one set of attributes determines another set of attributes in a relation.
- A decomposition of R into R1 and R2 is lossless if and only if one of the following functional dependencies holds in the closure of the set of functional dependencies F for R   :
  - R1 ∩ R2 → R1
  - R1 ∩ R2 → R2
  - where R1 ∩ R2 is the set of common attributes between R1 and R2, and → denotes functional dependency.
- A decomposition of R into R1, R2, ... Rn is lossless if and only if the decomposition of R into R1 and R2 is lossless, and the decomposition of R2 into R3 and R4 is lossless, and so on.
- Lossless join decomposition can be achieved by using decomposition algorithms such as BCNF and 3NF, which are based on the concepts of normal forms and minimal covers.