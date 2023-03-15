### Cursors

- A cursor is a database object that allows you to **traverse** the rows of a query result one by one or in blocks  .
- A cursor can be **declared** by defining a SQL statement that returns a result set.
- A cursor can be **opened** to execute the SQL statement and position the cursor at the first row of the result set.
- A cursor can be **fetched** to retrieve the current row or a block of rows from the result set and move the cursor to the next row or block .
- A cursor can be **closed** to release the resources associated with the cursor.
- A cursor can also be **deallocated** to remove the cursor definition from the database.
- Cursors can be used to perform **data modifications** such as insert, update, or delete on the rows of the result set.
- Cursors can also be used to perform **complex logic** or calculations on the rows of the result set that cannot be done by a single SQL statement.
- Cursors have different **types** and **options** that affect their behavior and performance  .
- Cursors are an **extension** to result sets and are not part of the relational data model or language.
- Cursors are **not recommended** for general use as they can be slow, resource-intensive, and prone to errors. They should be used only when necessary and with caution.