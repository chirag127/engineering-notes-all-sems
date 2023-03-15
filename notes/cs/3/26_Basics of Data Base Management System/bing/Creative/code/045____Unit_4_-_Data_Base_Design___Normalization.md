## Unit 4 - Data Base Design & Normalization

- Database design is the process of creating a logical and physical structure for storing and manipulating data in a database management system (DBMS).
- Normalization is a technique of database design that aims to reduce data redundancy and improve data integrity by organizing data into tables with well-defined relationships and constraints.
- The main steps of database design and normalization are:

  - **Requirement analysis**: Identify the purpose, scope, and objectives of the database, as well as the data sources, users, and applications that will interact with it.
  - **Conceptual design**: Create a high-level model of the database using an entity-relationship (ER) diagram or a unified modeling language (UML) class diagram. Define the entities, attributes, and relationships that represent the data and the business rules.
  - **Logical design**: Translate the conceptual model into a logical model using a specific data model, such as the relational model, the hierarchical model, or the network model. Define the tables, columns, keys, and constraints that will store the data in the DBMS.
  - **Physical design**: Optimize the logical model for performance, security, and usability by considering the physical characteristics of the DBMS, the hardware, the network, and the expected workload. Define the indexes, views, partitions, storage structures, and access methods that will support the data access and manipulation.
  - **Normalization**: Apply the rules of normalization to the logical model to eliminate or minimize the anomalies and dependencies that may cause data inconsistency, duplication, or loss. The most common normal forms are:

    - **First normal form (1NF)**: Ensure that each table has a primary key and that each column contains atomic values, i.e., values that cannot be further decomposed into smaller parts.
    - **Second normal form (2NF)**: Ensure that each table is in 1NF and that each non-key column depends on the whole primary key, i.e., there are no partial dependencies.
    - **Third normal form (3NF)**: Ensure that each table is in 2NF and that each non-key column depends only on the primary key, i.e., there are no transitive dependencies.
    - **Boyce-Codd normal form (BCNF)**: Ensure that each table is in 3NF and that each determinant (a column or a set of columns that determines the value of another column) is a candidate key, i.e., there are no non-trivial functional dependencies that violate the key constraint.
    - **Fourth normal form (4NF)**: Ensure that each table is in BCNF and that there are no multi-valued dependencies, i.e., dependencies that involve more than one value for a single attribute.
    - **Fifth normal form (5NF)**: Ensure that each table is in 4NF and that there are no join dependencies, i.e., dependencies that require joining two or more tables to reconstruct the original data.