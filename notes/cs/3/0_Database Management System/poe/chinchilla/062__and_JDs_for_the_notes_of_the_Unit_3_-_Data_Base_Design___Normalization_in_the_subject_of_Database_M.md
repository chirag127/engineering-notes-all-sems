### Unit 3 - Data Base Design & Normalization

Database design is a crucial aspect of building a database system. It involves the process of creating a database schema that represents the data and its relationships in a clear and efficient manner. Normalization is a technique used in database design to eliminate redundancy and ensure data integrity.

Here are some important points to consider when designing a database and applying normalization:

- **Entity-relationship modeling:** Before designing a database, it's essential to create an entity-relationship (ER) model that represents the data and its relationships. An ER model consists of entities, attributes, and relationships, which help in understanding the data and its connections.

- **Normalization:** Normalization is a technique used to eliminate redundancy and ensure data integrity. It involves breaking down a table into smaller tables and establishing relationships between them. There are several normal forms, each with its own set of rules that ensure data is organized efficiently.

- **First Normal Form (1NF):** A table is in 1NF if it has no repeating groups or arrays. Each column must contain atomic values, and each row must be unique.

- **Second Normal Form (2NF):** A table is in 2NF if it is in 1NF and every non-key attribute is dependent on the primary key. In other words, each attribute must be dependent on the entire primary key, not just a part of it.

- **Third Normal Form (3NF):** A table is in 3NF if it is in 2NF and has no transitive dependencies. A transitive dependency occurs when an attribute is dependent on another non-key attribute.

- **Boyce-Codd Normal Form (BCNF):** A table is in BCNF if it is in 3NF and every determinant is a candidate key. A determinant is an attribute that determines the value of another attribute.

- **Denormalization:** While normalization is essential for maintaining data integrity, it can sometimes lead to performance issues. Denormalization is a technique used to improve query performance by adding redundant data to a table. However, it should be used with caution as it can lead to data inconsistency.

- **Data Types:** Choosing the right data types is essential for efficient data storage and retrieval. Data types such as integers, strings, and dates should be chosen based on the type of data being stored.

- **Indexing:** Indexing is a technique used to speed up data retrieval by creating a data structure that allows for fast lookup. Indexes should be created on columns that are frequently used in queries.

- **Constraints:** Constraints are rules that ensure data integrity. They can be used to enforce business rules or prevent invalid data from being inserted into a table. Constraints include primary keys, foreign keys, unique constraints, and check constraints.

- **Normalization vs. Performance:** There is a trade-off between normalization and performance. Normalization can improve data integrity but can lead to slower query performance. Denormalization can improve query performance but can lead to data inconsistency. It's essential to strike a balance between the two based on the requirements of the application.

In summary, database design and normalization are crucial aspects of building a database system. A well-designed database can improve data integrity, query performance, and overall application efficiency. It's essential to understand the various normal forms, data types, indexing, and constraints to create an efficient and robust database system.