### Second

- Database design is the process of organizing the data and relationships in a database system to achieve optimal performance, accuracy, and integrity.
- Normalization is a database design technique that reduces data redundancy and eliminates undesirable characteristics like insertion, update and deletion anomalies.
- Normalization involves decomposing a table into less redundant (and smaller) tables without losing information; defining foreign keys in the old table referencing the primary keys of the new ones. The objective is to isolate data so that additions, deletions, and modifications of an attribute can be made in just one table and then propagated through the rest of the database via the defined foreign keys.
- There are different levels of normalization, called normal forms, that follow certain rules or criteria. The higher the normal form, the more normalized the database is. The most common normal forms are:

  - First normal form (1NF): A table is in 1NF if it contains no repeating groups of data and every attribute value is atomic (not divisible into smaller parts).
  - Second normal form (2NF): A table is in 2NF if it is in 1NF and every non-key attribute is fully functionally dependent on the primary key. This means that there is no partial dependency of any attribute on a part of the primary key.
  - Third normal form (3NF): A table is in 3NF if it is in 2NF and every non-key attribute is non-transitively dependent on the primary key. This means that there is no dependency of any attribute on another non-key attribute.
  - Boyce-Codd normal form (BCNF): A table is in BCNF if it is in 3NF and every determinant is a candidate key. A determinant is an attribute or a set of attributes that uniquely determines another attribute in a functional dependency.
  - Fourth normal form (4NF): A table is in 4NF if it is in BCNF and has no multi-valued dependencies. A multi-valued dependency occurs when a determinant can determine multiple values of another attribute independently of each other.
  - Fifth normal form (5NF): A table is in 5NF if it is in 4NF and has no join dependencies. A join dependency occurs when a table can be decomposed into two or more tables and then reconstructed by joining them on their primary keys without any loss or duplication of data.

- Normalization has many benefits, such as:

  - It reduces the amount of space a database consumes by eliminating duplicate data.
  - It makes it easier to maintain and update the database without causing data inconsistency or integrity problems.
  - It improves the efficiency of queries by reducing the number of joins and indexes required.
  - It ensures that the database conforms to the rules of the relational model and supports the basic relational operations.

- Normalization also has some drawbacks, such as:

  - It can increase the complexity of the database design by creating more tables and relationships.
  - It can increase the number of queries and transactions needed to perform certain operations, which can affect performance and concurrency.
  - It can make some business rules or constraints harder to enforce or implement at the database level.