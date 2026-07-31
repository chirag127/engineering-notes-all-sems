 Here is the content in markdown format without any emojis or external links, written in points and in a formal tone:

### Cursors for the notes of the Unit 6 - PL/SQL

1. A cursor is a pointer to the current row in the result set of a multi-row query.
2. It is used to process individual rows returned by a query.
3. The SET OF rows returned by a multi-row query can be referred to as a result set.
4. Cursors allow us to process each row of the result set, the one at a time.
5. The following steps are required to use a cursor:

- Declare the cursor
- Open the cursor
- Fetch rows from the cursor
- Process each row
- Close the cursor

6. There are two types of Cursors:

- Implicit Cursors: Used for DML statements like INSERT, UPDATE, DELETE. They are internally declared, opened, and closed by PL/SQL engine.
- Explicit Cursors: Must be declared, opened, fetched from, and closed by the programmer. They are used to query the database and process the results.

7. The syntax for declaring a cursor is:
CURSOR cursor_name IS query;

8. The FETCH statement is used to retrieve each row of data from the cursor. It returns the values into the variables specified. The syntax is:
FETCH cursor_name INTO var1, var2, ...;

9. The CLOSE statement releases the resources used by the cursor. The syntax is:
CLOSE cursor_name;