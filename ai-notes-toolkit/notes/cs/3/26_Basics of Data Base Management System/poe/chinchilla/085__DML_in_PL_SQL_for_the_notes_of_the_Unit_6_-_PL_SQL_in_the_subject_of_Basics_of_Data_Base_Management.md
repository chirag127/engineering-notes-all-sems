### DML in PL/SQL

DML or Data Manipulation Language is a subset of SQL that allows you to modify data within a database. In PL/SQL, you can use DML statements within blocks of code to manipulate data in a more customized and efficient way. Here are some important points to remember about DML in PL/SQL:

- The four basic DML operations in PL/SQL are INSERT, UPDATE, DELETE, and SELECT.
- The INSERT statement is used to add new rows to a table. You can use a VALUES clause to specify the values for each column in the new row, or you can use a SELECT statement to insert data from another table.
- The UPDATE statement is used to modify existing rows in a table. You can use a WHERE clause to specify which rows to update, and you can set multiple columns to new values within a single statement.
- The DELETE statement is used to remove rows from a table. You can use a WHERE clause to specify which rows to delete, and you can also use a subquery to delete rows from a table based on data from another table.
- The SELECT statement is used to retrieve data from one or more tables. You can use a variety of clauses to customize your query, such as WHERE, GROUP BY, and ORDER BY.
- In PL/SQL, you can use DML statements within blocks of code to manipulate data in a more customized and efficient way. You can also use variables and loops to create more complex DML operations.
- DML statements in PL/SQL can be used to manipulate data in both local and remote databases. You can use database links to connect to remote databases and execute DML statements on tables in those databases.
- When using DML statements in PL/SQL, it's important to consider the impact on performance and concurrency. For example, if you're updating a large number of rows, it may be more efficient to use bulk processing techniques like FORALL to reduce context-switching overhead.
- PL/SQL also provides a set of built-in functions and procedures for working with DML statements, such as the SQL%ROWCOUNT attribute, which returns the number of rows affected by the most recent DML statement.

Overall, DML in PL/SQL provides a powerful set of tools for manipulating data within a database. By mastering these techniques, you can create advanced data processing applications that can handle complex data manipulation tasks with ease.