### Lossless join decomposition

- Lossless join decomposition is a process of decomposing a relation R into two or more relations R1, R2, ... such that a natural join of the smaller relations yields back the original relation R  .
- This property guarantees that no information is lost from the original relation during the decomposition and that no spurious tuples are generated .
- Lossless join decomposition is essential for removing redundancy safely from databases while preserving the original data .
- A decomposition of R into R1 and R2 is lossless if and only if the common attributes of R1 and R2 form a candidate key for either R1 or R2  .
- This condition can be checked by using the closure of functional dependencies or by using a table construction algorithm .

: Lossless join decomposition - Wikipedia
: What is lossless join decomposition in DBMS - tutorialspoint.com
: Lossless Decomposition in DBMS - GeeksforGeeks
: relational database - Lossless Join Property - Stack Overflow