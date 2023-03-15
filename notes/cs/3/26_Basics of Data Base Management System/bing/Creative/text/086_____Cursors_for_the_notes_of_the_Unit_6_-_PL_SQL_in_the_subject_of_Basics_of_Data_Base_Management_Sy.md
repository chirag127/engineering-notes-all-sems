### Cursors

- A cursor is a pointer to a result set, or the data that results from a query .
- Cursors let you fetch one or more rows from the database into memory, process them, and then either commit or roll back those changes.
- Cursors are useful when you need to perform row-by-row operations on the data, such as calculations, validations, or transformations.
- PL/SQL has two types of cursors: implicit cursors and explicit cursors.
- Implicit cursors are automatically created and managed by Oracle whenever an SQL statement such as SELECT INTO, INSERT, UPDATE, or DELETE is executed .
- Implicit cursors have attributes such as %FOUND, %ISOPEN, %NOTFOUND, and %ROWCOUNT that can be used to check the status and outcome of the SQL statement.
- Explicit cursors are defined and controlled by the programmer using the CURSOR keyword .
- Explicit cursors have four steps: declaration, opening, fetching, and closing .
- Declaration: The cursor is defined with a name and a query .
- Opening: The cursor is executed and the result set is populated .
- Fetching: The cursor is moved to the next row and the data is retrieved into variables or records .
- Closing: The cursor is closed and the memory is freed .
- Explicit cursors can have parameters that can be passed at the time of opening .
- Explicit cursors can also use the FOR loop to simplify the fetching process .
- Explicit cursors can be declared in the declaration section of a block, a subprogram, or a package.
- Explicit cursors can also be declared as REF CURSORs, which are cursor variables that can point to different queries at run time.