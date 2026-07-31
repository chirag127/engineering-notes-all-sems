### Second

- Normalization is a database design technique that reduces data redundancy and eliminates undesirable characteristics like insertion, update and deletion anomalies.
- Normalization rules divide larger tables into smaller tables and link them using relationships.
- Normalization helps produce database systems that are cost-effective and have better security models.
- Normalization is based on the concept of normal forms, which are sets of rules that define the level of data integrity and efficiency in a table.
- The most common normal forms are:
  - First normal form (1NF): A table is in 1NF if every attribute is atomic (cannot be further subdivided) and every row has a unique identifier (primary key).
  - Second normal form (2NF): A table is in 2NF if it is in 1NF and every non-key attribute is fully functionally dependent on the primary key (i.e., there are no partial dependencies).
  - Third normal form (3NF): A table is in 3NF if it is in 2NF and every non-key attribute is non-transitively dependent on the primary key (i.e., there are no transitive dependencies).
  - Boyce-Codd normal form (BCNF): A table is in BCNF if it is in 3NF and every determinant (a set of attributes that determines another attribute) is a candidate key (a minimal set of attributes that uniquely identifies a row).
  - Fourth normal form (4NF): A table is in 4NF if it is in BCNF and there are no multi-valued dependencies (a situation where one attribute determines a set of values for another attribute).
- To perform the normalization process, you start with a rough idea of the data you want to store, and apply certain rules to it in order to get it to a more efficient form.
- A good rule to follow when doing logical database design is to arrange all the data in entities that are in 4NF. Then decide whether the result gives you an acceptable level of performance. If the performance is not acceptable, denormalizing your design is a good option.
- Denormalization is the process of reversing the normalization steps to improve the query performance or simplify the application logic. Denormalization can introduce data redundancy and inconsistency, so it should be done carefully and selectively.
- Database design is critical to the successful implementation of a database management system that meets the data requirements of an enterprise system.