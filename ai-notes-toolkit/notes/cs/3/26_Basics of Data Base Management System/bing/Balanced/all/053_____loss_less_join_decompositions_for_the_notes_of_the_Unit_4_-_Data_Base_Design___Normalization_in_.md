# Lossless Join Decomposition

- Lossless join decomposition is a process of splitting a relation R into two or more relations R1, R2, ... such that the natural join of R1, R2, ... gives back the original relation R. 
- Lossless join decomposition is important for removing redundancy and anomalies from databases while preserving the original data.  
- Lossless join decomposition is also known as non-additive join decomposition. 
- A decomposition of R into R1 and R2 is lossless if at least one of the following functional dependencies holds in the closure of the set of functional dependencies F of R:  
  - R1 ∩ R2 → R1
  - R1 ∩ R2 → R2
- A decomposition of R into R1, R2, ... Rn is lossless if there exists a sequence of binary lossless decompositions from R to R1, R2, ... Rn. 
- A decomposition of R is lossless if and only if the common attributes of any two relations in the decomposition form a superkey for at least one of the relations. 
- A decomposition of R is lossless if and only if for every legal instance r of R, the projection of r on R1, R2, ... Rn is a join dependency. 

: Lossless join decomposition - Wikipedia
: What is lossless join decomposition in DBMS - tutorialspoint.com
: Lossless Decomposition in DBMS - GeeksforGeeks
: relational database - Lossless Join Property - Stack Overflow