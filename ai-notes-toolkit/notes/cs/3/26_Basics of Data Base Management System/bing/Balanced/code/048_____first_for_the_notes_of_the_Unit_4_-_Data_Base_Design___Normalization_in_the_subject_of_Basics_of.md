# Unit 4 - Data Base Design & Normalization

- Database design is the process of creating a logical and physical structure for storing and manipulating data in a database management system (DBMS) .
- Normalization is a database design technique that reduces data redundancy and eliminates undesirable characteristics like insertion, update and deletion anomalies .
- Normalization rules divide larger tables into smaller tables and link them using relationships .
- Normalization is based on the concept of normal forms, which are sets of conditions that a table must satisfy to be considered well-structured .
- The most common normal forms are:
  - First normal form (1NF): A table is in 1NF if every attribute is atomic, meaning it cannot be further subdivided, and every row has a unique identifier .
  - Second normal form (2NF): A table is in 2NF if it is in 1NF and every non-key attribute is fully functionally dependent on the primary key, meaning it cannot be derived from any other attribute or combination of attributes .
  - Third normal form (3NF): A table is in 3NF if it is in 2NF and every non-key attribute is non-transitively dependent on the primary key, meaning it cannot be derived from any other non-key attribute or combination of non-key attributes .
  - Boyce-Codd normal form (BCNF): A table is in BCNF if it is in 3NF and every determinant is a candidate key, meaning there are no partial or transitive dependencies .
  - Fourth normal form (4NF): A table is in 4NF if it is in BCNF and there are no multi-valued dependencies, meaning there are no attributes that depend on a set of attributes rather than a single attribute .
- A good rule to follow when doing logical database design is to arrange all the data in entities that are in fourth normal form. Then decide whether the result gives you an acceptable level of performance. If the performance is not acceptable, denormalizing your design is a good option .
- Denormalization is the process of introducing redundancy into a database design to improve query performance or simplify application logic .
- Denormalization should be done carefully and only after analyzing the trade-offs between normalization and denormalization, such as data consistency, storage space, and maintenance costs .