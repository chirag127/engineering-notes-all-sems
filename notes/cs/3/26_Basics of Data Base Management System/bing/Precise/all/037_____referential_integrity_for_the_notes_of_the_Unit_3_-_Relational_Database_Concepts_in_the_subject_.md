### Referential Integrity

Referential integrity is a property of a relational database that ensures that relationships between tables remain consistent. It is a key concept in the subject of Basics of Database Management System, specifically in Unit 3 - Relational Database Concepts.

Here are some key points to remember about referential integrity:

1. Referential integrity is enforced through the use of foreign keys. A foreign key is a column or set of columns in one table that refers to the primary key of another table.

2. The purpose of a foreign key is to ensure that the data in the referring table corresponds to the data in the referred table. This means that if a record in the referring table contains a value in its foreign key column, that value must also exist in the primary key column of the referred table.

3. If referential integrity is enforced, it is not possible to enter a value in the foreign key column of the referring table that does not exist in the primary key column of the referred table. This helps to prevent orphaned records and ensures that the data in the database remains consistent.

4. Referential integrity can be enforced through the use of constraints. A constraint is a rule that is defined on a table to ensure that the data in the table adheres to certain conditions.

5. There are several types of constraints that can be used to enforce referential integrity, including primary key constraints, unique constraints, and foreign key constraints.

6. In addition to constraints, referential integrity can also be enforced through the use of triggers. A trigger is a special type of stored procedure that is automatically executed in response to certain events, such as the insertion, update, or deletion of data in a table.

7. Enforcing referential integrity helps to ensure the accuracy and consistency of data in a relational database. It is an important concept to understand when designing and working with relational databases.