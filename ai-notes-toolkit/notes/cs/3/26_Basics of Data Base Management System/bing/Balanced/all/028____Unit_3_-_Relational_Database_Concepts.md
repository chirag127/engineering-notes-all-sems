## Unit 3 - Relational Database Concepts

- A relational database is a collection of data organized into tables, where each table consists of rows (records) and columns (attributes).
- A primary key is a column or a combination of columns that uniquely identifies each row in a table.
- A foreign key is a column or a combination of columns that references a primary key in another table, to establish a relationship between the tables.
- A relationship is a logical association between two or more tables, based on a common attribute or a foreign key.
- There are three types of relationships: one-to-one, one-to-many, and many-to-many.
- A one-to-one relationship occurs when each row in one table is related to exactly one row in another table.
- A one-to-many relationship occurs when each row in one table is related to zero or more rows in another table, and each row in the other table is related to exactly one row in the first table.
- A many-to-many relationship occurs when each row in one table is related to zero or more rows in another table, and each row in the other table is related to zero or more rows in the first table.
- A many-to-many relationship requires a third table, called a junction table or an associative table, to store the combinations of primary keys from the two related tables.
- A relational schema is a graphical representation of the structure and relationships of a relational database, using symbols and notation to indicate the tables, columns, keys, and relationships.
- A relational model is a set of rules and constraints that define how data is stored and manipulated in a relational database, such as the entity integrity rule, the referential integrity rule, and the normalization rules.
- The entity integrity rule states that no primary key column can have null (missing or unknown) values, and that each table must have a primary key.
- The referential integrity rule states that if a foreign key exists in a table, it must either match a primary key value in another table or be null.
- Normalization is a process of organizing the data in a relational database to reduce redundancy and improve data integrity, by applying a series of normal forms or rules.
- The first normal form (1NF) states that each column in a table must have atomic values, meaning that they cannot be divided into smaller parts, and that there must be no repeating groups of columns.
- The second normal form (2NF) states that each table must be in 1NF, and that each non-key column in a table must depend on the whole primary key, not just a part of it.
- The third normal form (3NF) states that each table must be in 2NF, and that each non-key column in a table must depend only on the primary key, not on any other non-key column.