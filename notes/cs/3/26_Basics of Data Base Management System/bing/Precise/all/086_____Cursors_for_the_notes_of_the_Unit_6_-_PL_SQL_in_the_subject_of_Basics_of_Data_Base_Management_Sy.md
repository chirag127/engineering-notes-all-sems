# Unit 6 - PL/SQL: Cursors

- A cursor is a control structure that enables traversal over the records in a database.
- Cursors allow you to iterate over a set of rows returned by a query and process each row individually.
- There are two types of cursors: implicit and explicit.
- An implicit cursor is automatically created by Oracle when an SQL statement is executed, when there is no explicit cursor for the statement.
- An explicit cursor is created by the programmer to gain more control over the context area.
- The syntax for declaring a cursor is: `CURSOR cursor_name IS select_statement;`
- The cursor is opened using the `OPEN` statement, which executes the query and identifies the result set.
- The `FETCH` statement retrieves the current row from the result set and advances the cursor to the next row.
- The `CLOSE` statement closes the cursor and releases the context area.
- Cursors can be used to perform row-by-row processing, for example, to calculate the sum of values in a column or to update rows in a table.
