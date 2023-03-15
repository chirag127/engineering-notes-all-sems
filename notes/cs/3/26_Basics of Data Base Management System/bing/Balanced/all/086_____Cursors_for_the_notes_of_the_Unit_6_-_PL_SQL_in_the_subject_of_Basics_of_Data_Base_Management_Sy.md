# Cursors

- A cursor is a pointer to a result set, or the data that results from a query .
- A cursor allows you to fetch one or more rows from the database into memory, process them, and then either commit or roll back those changes.
- A cursor also holds information about the context area, which is a memory area that contains the execution state of a SQL statement .
- PL/SQL has two types of cursors: implicit cursors and explicit cursors.

## Implicit Cursors

- Implicit cursors are automatically created by Oracle whenever an SQL statement such as SELECT INTO, INSERT, UPDATE, or DELETE is executed.
- Implicit cursors are also known as SQL cursors, and they have attributes such as %FOUND, %ISOPEN, %NOTFOUND, and %ROWCOUNT that can be used to check the status and outcome of the SQL statement.
- Implicit cursors are useful for simple queries that return only one row or perform a single data manipulation operation.

## Explicit Cursors

- Explicit cursors are user-defined cursors that are declared and controlled by the programmer .
- Explicit cursors are used for complex queries that return more than one row or require more processing logic.
- Explicit cursors have four steps: declaration, opening, fetching, and closing .
- Declaration: The cursor is declared using the CURSOR keyword, followed by a name and a query .
- Opening: The cursor is opened using the OPEN statement, which allocates the context area and executes the query .
- Fetching: The cursor is fetched using the FETCH statement, which retrieves one or more rows from the result set and assigns them to variables or records .
- Closing: The cursor is closed using the CLOSE statement, which frees the context area and releases the resources .
- Explicit cursors can also have parameters, which are variables that are passed to the query when the cursor is opened .
- Explicit cursors can also be used with cursor FOR loops, which simplify the fetching and processing of the rows in the result set .