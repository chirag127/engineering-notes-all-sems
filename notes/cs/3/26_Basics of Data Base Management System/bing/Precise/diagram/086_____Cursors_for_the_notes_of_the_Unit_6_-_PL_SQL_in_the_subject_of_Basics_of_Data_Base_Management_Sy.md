### Cursors

Cursors are a PL/SQL construct that allows you to retrieve and manipulate rows from a result set one at a time. They are used when a SELECT statement returns multiple rows, and you need to perform operations on each row individually.

Here are some key points to remember about cursors:

1. Cursors are used to retrieve rows from a result set one at a time.
2. A cursor must be declared and opened before it can be used.
3. A cursor must be closed when it is no longer needed.
4. There are two types of cursors: implicit and explicit.
5. An implicit cursor is automatically created and managed by PL/SQL when you execute a SELECT statement that returns multiple rows.
6. An explicit cursor is created and managed by the programmer.
7. You can use the %FOUND, %NOTFOUND, %ISOPEN, and %ROWCOUNT attributes to check the status of a cursor.
8. You can use the FETCH statement to retrieve rows from a cursor one at a time.
9. You can use the FOR loop to iterate over the rows in a cursor.

These are some of the key points to remember about cursors in PL/SQL. They are an important tool for working with result sets and performing operations on individual rows. It is important to understand how to declare, open, and close cursors, as well as how to use the various cursor attributes and statements.