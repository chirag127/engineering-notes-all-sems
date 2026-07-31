## Unit 4 - Data Base Design & Normalization

- Database design is the process of creating a logical and physical structure for storing and manipulating data in a database system.
- Normalization is a technique of database design that aims to reduce data redundancy and improve data integrity by organizing data into tables with well-defined relationships and constraints.
- The main steps of database design and normalization are:

  - **Requirement analysis**: Identify the purpose, scope, and objectives of the database system, and gather the data requirements from the users and stakeholders.
  - **Conceptual design**: Create a high-level abstract model of the data using an entity-relationship (ER) diagram, which shows the entities, attributes, and relationships involved in the database system.
  - **Logical design**: Map the conceptual model to a logical model using a data model, such as the relational model, which defines the tables, columns, keys, and constraints for the database system.
  - **Normalization**: Apply the rules of normalization to the logical model to eliminate any anomalies, such as update, insertion, or deletion anomalies, that may arise due to data redundancy or dependency.
  - **Physical design**: Implement the logical model in a specific database management system (DBMS), and optimize the performance, security, and usability of the database system.

- The main rules of normalization are:

  - **First normal form (1NF)**: A table is in 1NF if every column contains only atomic values, and there are no repeating groups or arrays within a column.
  - **Second normal form (2NF)**: A table is in 2NF if it is in 1NF and every non-key column is fully functionally dependent on the primary key, and not on any subset of the primary key.
  - **Third normal form (3NF)**: A table is in 3NF if it is in 2NF and every non-key column is non-transitively dependent on the primary key, and not on any other non-key column.
  - **Boyce-Codd normal form (BCNF)**: A table is in BCNF if it is in 3NF and every determinant is a candidate key, and not a proper subset of any candidate key.
  - **Fourth normal form (4NF)**: A table is in 4NF if it is in BCNF and there are no multi-valued dependencies, which occur when a column depends on another column that has more than one value for a given key.
  - **Fifth normal form (5NF)**: A table is in 5NF if it is in 4NF and there are no join dependencies, which occur when a table can be decomposed into two or more tables that can be joined back together without losing any information.