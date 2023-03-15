# Unit 5 - Structured Query Language (SQL) in the subject of Basics of Data Base Management System

### Defining Constraints

1. Constraints are rules that are applied to the data in a table to ensure that the data is accurate and consistent.
2. Constraints can be defined at the column level or at the table level.
3. The most common types of constraints are:
    - NOT NULL: Ensures that a column cannot have a NULL value.
    - UNIQUE: Ensures that all values in a column are unique.
    - PRIMARY KEY: A combination of NOT NULL and UNIQUE. It uniquely identifies each row in a table.
    - FOREIGN KEY: Ensures that the values in a column match the values in another table's PRIMARY KEY column.
    - CHECK: Ensures that the values in a column meet a specific condition.
4. Constraints can be added to a table when the table is created using the CREATE TABLE statement, or they can be added to an existing table using the ALTER TABLE statement.
5. Constraints can be removed from a table using the ALTER TABLE statement.
6. Constraints can be temporarily disabled and then re-enabled using the ALTER TABLE statement.
7. Constraints can be named or unnamed. If a constraint is unnamed, the database system will generate a name for it.
8. It is a good practice to name constraints to make it easier to identify and manage them.
9. Constraints can be cascaded, meaning that if a row is deleted or updated in one table, the corresponding rows in related tables are also deleted or updated.
10. Constraints can be deferred, meaning that they are not checked until the end of the transaction.