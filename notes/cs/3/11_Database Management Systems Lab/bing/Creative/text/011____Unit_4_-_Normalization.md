## Unit 4 - Normalization

- Normalization is a process of organizing the data in a database to reduce redundancy and improve data integrity.
- Normalization also simplifies the database design so that it achieves the optimal structure composed of atomic elements (i.e. elements that cannot be broken down into smaller parts).
- There are different levels of normalization, called normal forms, that a database can achieve. Each normal form has a set of rules or criteria that must be met in order to qualify for that level.
- The most common normal forms are:

  - First Normal Form (1NF): A table is in 1NF if it contains no repeating groups of data and every cell contains only one value.
  - Second Normal Form (2NF): A table is in 2NF if it is in 1NF and every non-key attribute is fully dependent on the primary key.
  - Third Normal Form (3NF): A table is in 3NF if it is in 2NF and every non-key attribute is non-transitively dependent on the primary key.
  - Boyce-Codd Normal Form (BCNF): A table is in BCNF if it is in 3NF and every determinant is a candidate key.
  - Fourth Normal Form (4NF): A table is in 4NF if it is in BCNF and it has no multi-valued dependencies.
  - Fifth Normal Form (5NF): A table is in 5NF if it is in 4NF and it has no join dependencies.

- The benefits of normalization are:

  - It eliminates data anomalies, such as insertion, deletion, and update anomalies, that can cause data inconsistency and corruption.
  - It reduces data redundancy, which saves storage space and improves performance.
  - It makes the database more flexible and easier to maintain and query.
  - It ensures data integrity and accuracy by enforcing referential integrity and domain constraints.

- The drawbacks of normalization are:

  - It can increase the number of tables and joins, which can make the queries more complex and slow.
  - It can reduce data availability and security, as some data may be split into multiple tables and require more permissions and access controls.
  - It can introduce some redundancy in the form of foreign keys, which can increase the size of the tables and indexes.