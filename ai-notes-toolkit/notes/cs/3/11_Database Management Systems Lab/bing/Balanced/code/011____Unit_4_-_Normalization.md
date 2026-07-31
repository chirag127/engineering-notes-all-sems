## Unit 4 - Normalization

- Normalization is a process of organizing the data in a database to reduce redundancy and improve data integrity.
- Normalization also simplifies the database design by ensuring that each table has a specific purpose and does not store redundant or irrelevant data.
- Normalization is based on a set of rules or principles called normal forms, which define the criteria for a well-structured table.
- The most common normal forms are first normal form (1NF), second normal form (2NF), third normal form (3NF), and Boyce-Codd normal form (BCNF).
- Each normal form has a higher degree of normalization than the previous one, meaning that it removes more anomalies and inconsistencies from the data.
- To normalize a table, we apply the normal forms in a sequence, starting from 1NF and going up to the desired level of normalization.

### First Normal Form (1NF)

- A table is in 1NF if it satisfies the following conditions:
  - Each cell contains a single value, not a list or a set of values.
  - Each column has a unique name and a specific data type.
  - The order of the rows and columns does not matter.
  - There are no duplicate rows in the table.
- 1NF eliminates repeating groups and ensures that each attribute has a single value for each record.

### Second Normal Form (2NF)

- A table is in 2NF if it satisfies the following conditions:
  - It is in 1NF.
  - It has no partial dependencies, meaning that no non-key attribute depends on a subset of the primary key.
  - A primary key is a combination of columns that uniquely identifies each row in the table.
  - A non-key attribute is any column that is not part of the primary key.
  - A partial dependency occurs when a non-key attribute depends on only some of the columns in the primary key, not the whole key.
- 2NF eliminates partial dependencies and ensures that each non-key attribute depends on the entire primary key.

### Third Normal Form (3NF)

- A table is in 3NF if it satisfies the following conditions:
  - It is in 2NF.
  - It has no transitive dependencies, meaning that no non-key attribute depends on another non-key attribute.
  - A transitive dependency occurs when a non-key attribute depends on another non-key attribute, which in turn depends on the primary key.
- 3NF eliminates transitive dependencies and ensures that each non-key attribute depends only on the primary key.

### Boyce-Codd Normal Form (BCNF)

- A table is in BCNF if it satisfies the following condition:
  - It is in 3NF.
  - It has no non-trivial functional dependencies, meaning that no non-key attribute determines another non-key attribute.
  - A functional dependency is a relationship between two sets of attributes, such that for a given value of one set, there is only one possible value of the other set.
  - A non-trivial functional dependency is one that is not implied by the primary key or by any other functional dependency in the table.
- BCNF eliminates non-trivial functional dependencies and ensures that each non-key attribute is determined only by the primary key or by a candidate key.
  - A candidate key is a subset of columns that can uniquely identify each row in the table, but is not the primary key.