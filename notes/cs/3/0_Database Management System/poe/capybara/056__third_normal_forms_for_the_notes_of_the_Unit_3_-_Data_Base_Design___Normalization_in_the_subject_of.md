### Third Normal Forms for the Notes of the Unit 3 - Database Design & Normalization in the Subject of Database Management System

Here are the key points to consider regarding the third normal forms in the database design and normalization:

- The third normal form (3NF) is a database design principle that ensures the elimination of redundant data in a database table.
- In the third normal form, a table is considered to be in 3NF if it satisfies the following conditions:
  - The table must be in second normal form (2NF).
  - The table must not have any transitive dependencies.
- A transitive dependency occurs when a non-key column depends on another non-key column in a table.
- To eliminate transitive dependencies, we need to break the table into multiple tables, each containing a subset of the original table's columns.
- The new tables should be connected with foreign keys, and the original table should contain only the primary key and the foreign keys.
- The third normal form is necessary to ensure data consistency and avoid anomalies during data modification.
- However, achieving the third normal form may result in a larger number of tables and more complex queries.
- It is important to strike a balance between normalization and usability, as over-normalization can lead to performance issues and increased development time.

Remember, the third normal form is an important aspect of database design and normalization, and understanding its principles is crucial for building efficient and scalable databases.