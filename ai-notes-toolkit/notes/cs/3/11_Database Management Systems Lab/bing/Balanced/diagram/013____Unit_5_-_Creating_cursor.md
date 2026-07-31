## Unit 5 - Creating cursor

- A cursor is a temporary work area created in the system memory when a SQL statement is executed.
- A cursor contains information on a select statement and the rows of data accessed by it.
- A cursor can be used to retrieve one or more rows of data and perform operations on them.
- A cursor can be either implicit or explicit.
- An implicit cursor is automatically created by Oracle whenever a SQL statement is executed, when there is no explicit cursor for the statement.
- An explicit cursor is created by the programmer to gain more control over the query execution and result handling.
- An explicit cursor has four attributes: %FOUND, %NOTFOUND, %ROWCOUNT, and %ISOPEN, which provide information about the execution of the cursor.
- An explicit cursor is defined using the CURSOR keyword in the declaration section of a PL/SQL block.
- An explicit cursor is opened using the OPEN statement, which allocates memory for the cursor and executes the query.
- An explicit cursor is fetched using the FETCH statement, which retrieves the next row of data from the cursor into a record or a list of variables.
- An explicit cursor is closed using the CLOSE statement, which frees the memory allocated for the cursor and invalidates the cursor.
- An explicit cursor can be parameterized to accept arguments at run time and execute different queries based on the arguments.
- An explicit cursor can be used in a cursor FOR loop, which simplifies the process of opening, fetching, and closing the cursor.