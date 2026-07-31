## Unit 3 - Relational Database Concepts

- A relational database is a collection of data organized into tables, where each table consists of rows (records) and columns (attributes).
- A primary key is a column or a combination of columns that uniquely identifies each row in a table.
- A foreign key is a column or a combination of columns that references a primary key in another table, to establish a relationship between the tables.
- A relationship is a logical association between two or more tables, based on a common attribute or a foreign key.
- There are three types of relationships: one-to-one, one-to-many, and many-to-many.
- A one-to-one relationship occurs when each row in one table is related to exactly one row in another table.
- A one-to-many relationship occurs when each row in one table is related to zero or more rows in another table, and each row in the other table is related to at most one row in the first table.
- A many-to-many relationship occurs when each row in one table is related to zero or more rows in another table, and each row in the other table is related to zero or more rows in the first table.
- A many-to-many relationship requires a third table, called a junction table or an associative table, to store the combinations of primary keys from the two related tables.
- A relational schema is a graphical representation of the structure and relationships of a relational database, using symbols and notation to indicate the tables, columns, keys, and relationships.
- A relational model is a set of rules and constraints that define how data is stored and manipulated in a relational database, such as the entity integrity rule, the referential integrity rule, and the normalization rules.
- The entity integrity rule states that no primary key column can have a null value, to ensure the uniqueness of each row in a table.
- The referential integrity rule states that any foreign key value must either match a primary key value in the referenced table, or be null, to ensure the consistency of the data across the tables.
- Normalization is a process of organizing the data in a relational database into tables that are free of anomalies, redundancies, and dependencies, to improve the efficiency and integrity of the database.
- There are several levels of normalization, each with a specific goal and a set of criteria to meet. The most common levels are the first normal form (1NF), the second normal form (2NF), and the third normal form (3NF).
- The first normal form (1NF) requires that each table has a primary key, and that each column contains atomic values, meaning no repeating groups or nested tables.
- The second normal form (2NF) requires that each table is in 1NF, and that each non-key column is fully dependent on the primary key, meaning no partial dependencies.
- The third normal form (3NF) requires that each table is in 2NF, and that each non-key column is non-transitively dependent on the primary key, meaning no transitive dependencies.