## Unit 3 - Data Base Design & Normalization

- Database design is the process of creating a logical and physical structure for storing and manipulating data in a database management system (DBMS).
- Database design involves identifying the data requirements, defining the entities and attributes, establishing the relationships and constraints, and choosing the appropriate data models and schemas.
- Normalization is a technique of database design that aims to reduce data redundancy and improve data integrity by organizing the data into smaller and well-defined tables.
- Normalization involves applying a series of rules or normal forms to decompose a table into simpler tables that have minimal functional dependencies and anomalies.
- The main normal forms are:
  - First normal form (1NF): A table is in 1NF if every attribute is atomic, meaning it cannot be further subdivided, and there are no repeating groups of attributes.
  - Second normal form (2NF): A table is in 2NF if it is in 1NF and every non-key attribute is fully functionally dependent on the primary key, meaning it cannot be determined by a subset of the primary key.
  - Third normal form (3NF): A table is in 3NF if it is in 2NF and every non-key attribute is non-transitively dependent on the primary key, meaning it cannot be determined by another non-key attribute.
  - Boyce-Codd normal form (BCNF): A table is in BCNF if it is in 3NF and every determinant is a candidate key, meaning there are no partial or transitive dependencies on non-key attributes.
  - Fourth normal form (4NF): A table is in 4NF if it is in BCNF and there are no multi-valued dependencies, meaning there are no attributes that depend on a set of attributes rather than a single attribute.
  - Fifth normal form (5NF): A table is in 5NF if it is in 4NF and there are no join dependencies, meaning there are no subsets of attributes that can be reconstructed from other subsets by joining tables.
- Normalization has some advantages and disadvantages, such as:
  - Advantages: It reduces data duplication, improves data consistency, facilitates data manipulation, and enhances data security and integrity.
  - Disadvantages: It increases the number of tables and joins, which may affect performance and complexity, and it may lose some information or business rules that are not captured by the normal forms.