### Referential Integrity

Referential integrity is a property of a relational database that ensures that relationships between tables remain consistent. It is a key concept in the subject of Basics of Database Management System, specifically in Unit 3 - Relational Database Concepts.

Here are some key points to remember about referential integrity:

1. Referential integrity is enforced through the use of foreign keys. A foreign key is a column or set of columns in a table that refers to the primary key of another table.

2. When a foreign key is defined, the database management system checks that the values in the foreign key columns match the values in the primary key of the referenced table.

3. If a value in a foreign key column does not match any value in the primary key of the referenced table, the database management system will not allow the operation to proceed. This ensures that the relationship between the tables remains consistent.

4. Referential integrity can also be enforced through the use of cascading updates and deletes. When a record in the referenced table is updated or deleted, the corresponding records in the referencing table are also updated or deleted.

5. Referential integrity is important because it helps to maintain the accuracy and consistency of data in a relational database. Without referential integrity, it would be possible for data in the database to become inconsistent and unreliable.
