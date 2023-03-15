# Update and Delete Operations for the Notes of the Unit 5 - Structured Query Language (SQL) in the Subject of Basics of Data Base Management System

- SQL is a language that allows users to view and manage data in a relational database system.
- Data Manipulation Language (DML) is a subset of SQL that deals with inserting, updating, deleting, and selecting data from tables and views.
- The UPDATE command is used to modify the existing records in the database. The syntax is:

```sql
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```

- The SET clause specifies which columns to update and what values to assign to them.
- The WHERE clause specifies which rows to update based on a condition. If the WHERE clause is omitted, all rows in the table will be updated.
- The DELETE command is used to delete the records in the database that are no longer required. The syntax is:

```sql
DELETE FROM table_name
WHERE condition;
```

- The WHERE clause specifies which rows to delete based on a condition. If the WHERE clause is omitted, all rows in the table will be deleted.
- The SELECT command is used to retrieve data from the database. The syntax is:

```sql
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```

- The SELECT clause specifies which columns to return from the table or view.
- The FROM clause specifies which table or view to query from.
- The WHERE clause specifies which rows to return based on a condition. If the WHERE clause is omitted, all rows in the table or view will be returned.
- The INSERT command is used to add new records to the database. The syntax is:

```sql
INSERT INTO table_name (column1, column2, ...)
VALUES (value1, value2, ...);
```

- The INSERT INTO clause specifies which table to insert the data into and which columns to fill.
- The VALUES clause specifies the values to assign to each column. The number and order of values must match the number and order of columns.
- SQL best practices for deleting and updating data include:
  - Using transactions to ensure data integrity and consistency. Transactions are a set of SQL statements that are executed as a single unit. If any statement fails, the whole transaction is rolled back and the database is restored to its previous state. Transactions can be started and ended with the BEGIN TRANSACTION and COMMIT TRANSACTION commands, respectively.
  - Using backup and restore mechanisms to prevent data loss. Backup and restore are processes that allow users to save and recover the data in the database in case of a failure or a mistake. Backup and restore can be performed using the BACKUP and RESTORE commands, respectively.
  - Using primary keys and foreign keys to enforce data relationships and constraints. Primary keys are columns that uniquely identify each row in a table. Foreign keys are columns that reference the primary keys of another table. Primary keys and foreign keys can be defined using the PRIMARY KEY and FOREIGN KEY constraints, respectively.
  - Using indexes to improve the performance of queries. Indexes are data structures that store the values of one or more columns in a sorted order, allowing faster access to the data. Indexes can be created using the CREATE INDEX command.