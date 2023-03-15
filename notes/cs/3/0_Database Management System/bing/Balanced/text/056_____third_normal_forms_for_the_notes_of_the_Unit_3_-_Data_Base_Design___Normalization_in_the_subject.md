### Third Normal Form

- Third normal form (3NF) is a database design principle that aims to reduce data redundancy and improve data integrity.
- A relation is in 3NF if it is in second normal form (2NF) and every non-key attribute is non-transitively dependent on the primary key.
- Non-transitive dependency means that there is no functional dependency between two non-key attributes that is mediated by another non-key attribute.
- For example, consider a relation R(A, B, C, D) with the following functional dependencies: A -> B, B -> C, C -> D. This relation is not in 3NF because C is transitively dependent on A through B, and D is transitively dependent on A through C.
- To convert a relation to 3NF, we need to decompose it into smaller relations that eliminate the transitive dependencies. In this case, we can decompose R into R1(A, B), R2(B, C), and R3(C, D).
- The benefits of 3NF are that it reduces data duplication, avoids update anomalies, and preserves the dependencies in the original relation.