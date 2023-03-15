# DML

DML stands for Data Manipulation Language. It is a family of computer languages that are used to manipulate data in a database. DML includes commands that allow users to:

- Insert data into database tables
- Retrieve data from database tables
- Delete data from database tables
- Update data in database tables

Some of the main DML statements are:

- SELECT: This statement is used to query data from one or more tables or views. It can specify the columns, conditions, order, and grouping of the data to be retrieved.
- INSERT: This statement is used to add new rows of data to a table. It can specify the values for each column or use a subquery to get the values from another table.
- DELETE: This statement is used to remove existing rows of data from a table. It can specify the conditions for the rows to be deleted or use a subquery to get the rows from another table.
- UPDATE: This statement is used to modify existing rows of data in a table. It can specify the new values for each column or use a subquery to get the values from another table. It can also specify the conditions for the rows to be updated.

DML is mostly incorporated in SQL databases, which are relational databases that use the Structured Query Language (SQL) as the standard language for accessing and manipulating data. SQL is a declarative language, which means that it specifies what data to get or change, but not how to do it. The database system is responsible for executing the DML statements and returning the results to the user or application.

DML is different from DDL (Data Definition Language), which is used to define the structure and schema of the database, such as tables, columns, constraints, indexes, etc. DML is also different from DCL (Data Control Language), which is used to control the access and permissions of the database, such as granting or revoking privileges, roles, etc.

DML triggers are a special type of stored procedure that automatically takes effect when a DML event occurs on a table or view. DML triggers can be used to enforce business rules, audit data changes, perform cascading actions, etc. DML triggers can be defined for INSERT, UPDATE, or DELETE statements, and can be executed before or after the statement. DML triggers can also access the inserted and deleted tables, which contain the rows affected by the DML statement. DML triggers are written in Transact-SQL, which is an extension of SQL that adds procedural features and database-specific functions.