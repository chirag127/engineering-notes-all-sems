### Referential Integrity

Referential integrity is a property of a relational database that ensures that relationships between tables remain consistent. It is a key concept in the subject of Basics of Database Management System, specifically in Unit 3 - Relational Database Concepts.

Here are some key points to remember about referential integrity:

1. Referential integrity is enforced through the use of foreign keys. A foreign key is a column or a set of columns in a table that refers to the primary key of another table.

2. The table that contains the foreign key is called the referencing table, while the table that is referred to by the foreign key is called the referenced table.

3. When a record is inserted or updated in the referencing table, the database management system checks that the value of the foreign key matches the value of the primary key in the referenced table. If the value does not match, the operation is not allowed.

4. Referential integrity also applies to deletion. If a record is deleted from the referenced table, any records in the referencing table that refer to the deleted record must also be deleted or updated to remove the reference.

5. Referential integrity can be enforced through the use of cascading updates and deletes. This means that when a record is updated or deleted in the referenced table, any related records in the referencing table are automatically updated or deleted as well.

6. Referential integrity helps to maintain the consistency and accuracy of data in a relational database. It ensures that relationships between tables are always valid and that data is not accidentally lost or corrupted.
