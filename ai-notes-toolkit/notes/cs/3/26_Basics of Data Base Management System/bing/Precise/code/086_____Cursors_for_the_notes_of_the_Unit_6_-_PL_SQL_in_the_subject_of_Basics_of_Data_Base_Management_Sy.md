### Cursors

Cursors are a feature of PL/SQL that allow you to retrieve and manipulate data from a database. They are used to process individual rows returned by a query. Cursors are essential when you need to update records in a database table one row at a time.

Here are some key points to remember about cursors:

1. Cursors allow you to retrieve data from a database and manipulate it on a row-by-row basis.
2. Cursors are essential when you need to update records in a database table one row at a time.
3. Cursors are declared using the `DECLARE` keyword and opened using the `OPEN` keyword.
4. Cursors must be closed using the `CLOSE` keyword when you are finished using them.
5. You can use the `FETCH` keyword to retrieve the next row from a cursor.
6. You can use the `%FOUND`, `%NOTFOUND`, `%ROWCOUNT`, and `%ISOPEN` attributes to check the status of a cursor.
7. You can use the `FOR` loop to iterate over the rows returned by a cursor.
