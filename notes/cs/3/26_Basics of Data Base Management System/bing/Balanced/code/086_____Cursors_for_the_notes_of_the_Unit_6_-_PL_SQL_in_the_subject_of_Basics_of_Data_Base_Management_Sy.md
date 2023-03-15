### Cursors

A cursor is a pointer to a result set, or the data that results from a query. Cursors let you fetch one or more rows from the database into memory, process them, and then either commit or roll back those changes.

There are two types of cursors in PL/SQL: implicit cursors and explicit cursors.

- Implicit cursors are automatically created by Oracle whenever an SQL statement is executed. You can access the attributes of an implicit cursor using the SQL prefix. For example, SQL%ROWCOUNT returns the number of rows affected by the last SQL statement.
- Explicit cursors are user-defined cursors that allow you to name and control the result set of a query. You can declare, open, fetch, and close an explicit cursor using PL/SQL statements. You can also define parameters for an explicit cursor and use them in the query.

Some advantages of using cursors are:

- You can process each row individually and perform complex logic on it.
- You can avoid errors such as too many rows or no data found by handling exceptions.
- You can improve the performance of your queries by using cursor attributes and bulk operations.

Some disadvantages of using cursors are:

- You need to write more code to declare and manipulate cursors.
- You may consume more memory and CPU resources by fetching and processing large result sets.
- You may encounter locking issues if you update the data in the cursor and other sessions try to access the same data.