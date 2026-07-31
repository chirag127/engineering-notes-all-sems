### Referential Integrity

Referential integrity is a property of a relational database that ensures that relationships between tables remain consistent. It is a key concept in the subject of Basics of Database Management System, specifically in Unit 3 - Relational Database Concepts.

Here are some key points to remember about referential integrity:

1. Referential integrity is enforced through the use of foreign keys. A foreign key is a column or set of columns in one table that refers to the primary key of another table.

2. The purpose of referential integrity is to prevent orphaned records. An orphaned record is a record in a child table that does not have a corresponding record in the parent table.

3. To maintain referential integrity, the database management system will not allow the user to:
    - Add a record to the child table if there is no corresponding record in the parent table.
    - Delete a record from the parent table if there are corresponding records in the child table.
    - Update the primary key of a record in the parent table if there are corresponding records in the child table.

4. Referential integrity can be enforced through the use of cascading updates and deletes. This means that when a record in the parent table is updated or deleted, the corresponding records in the child table are also updated or deleted.

5. Referential integrity is an important concept to understand when designing and maintaining a relational database. It helps to ensure data consistency and accuracy.
