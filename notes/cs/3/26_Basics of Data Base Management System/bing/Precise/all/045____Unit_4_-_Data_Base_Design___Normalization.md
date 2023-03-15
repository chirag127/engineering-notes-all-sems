## Unit 4 - Data Base Design & Normalization

Database design is the process of producing a detailed data model of a database. This data model contains all the needed logical and physical design choices and physical storage parameters needed to generate a design. The main objectives of database design include:

1. Minimizing data redundancy and dependency.
2. Ensuring data integrity and accuracy.
3. Ensuring data security and privacy.
4. Ensuring efficient data retrieval and manipulation.

Normalization is the process of organizing a database in a way that reduces redundancy and dependency. It is a technique used to design a database so that it meets certain requirements, such as minimizing duplicate data and ensuring that data is stored in the most appropriate way. Normalization typically involves dividing a database into smaller, more focused tables and defining relationships between those tables.

There are several levels of normalization, including:

1. First Normal Form (1NF): Each table has a primary key and no repeating groups.
2. Second Normal Form (2NF): Each non-key attribute is fully dependent on the primary key.
3. Third Normal Form (3NF): Each non-key attribute is non-transitively dependent on the primary key.
4. Boyce-Codd Normal Form (BCNF): Every determinant in the table is a candidate key.

Normalization helps to reduce data redundancy and improve data integrity. However, it is important to note that normalization is not always the best approach for every situation, and over-normalization can lead to performance issues. It is important to strike a balance between normalization and performance when designing a database.