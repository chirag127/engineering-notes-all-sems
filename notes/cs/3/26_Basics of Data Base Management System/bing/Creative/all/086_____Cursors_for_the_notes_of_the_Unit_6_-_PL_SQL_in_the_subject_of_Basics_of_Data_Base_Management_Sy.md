# Cursors

- A cursor is a pointer to a context area that contains information about the execution of a SQL statement .
- A cursor can hold one or more rows returned by a SQL statement.
- A cursor can be implicit or explicit .
  - An implicit cursor is automatically created by Oracle whenever a SQL statement is executed .
  - An explicit cursor is explicitly declared by the programmer to perform complex queries or to process multiple rows .
- A cursor has four attributes: `%FOUND`, `%NOTFOUND`, `%ROWCOUNT`, and `%ISOPEN`.
  - `%FOUND` returns `TRUE` if the cursor fetched at least one row, otherwise `FALSE`.
  - `%NOTFOUND` returns `TRUE` if the cursor fetched no rows, otherwise `FALSE`.
  - `%ROWCOUNT` returns the number of rows fetched by the cursor so far.
  - `%ISOPEN` returns `TRUE` if the cursor is open, otherwise `FALSE`.
- A cursor can be manipulated using the following steps :
  - Declare the cursor using the `CURSOR` keyword and specify the query .
  - Open the cursor using the `OPEN` statement to allocate the context area and execute the query .
  - Fetch the cursor using the `FETCH` statement to retrieve one or more rows from the result set .
  - Close the cursor using the `CLOSE` statement to release the context area and free the resources .
- A cursor can be declared and opened in a single statement using the `CURSOR FOR` loop.
- A cursor can be dynamic, meaning that the query can be constructed and executed at run time using the `EXECUTE IMMEDIATE` statement.