## Unit 5 - Creating cursor

A cursor is a temporary work area created in the system memory when a SQL statement is executed. A cursor contains information on a select statement and the rows of data accessed by it. This unit covers the following topics:

- What is a cursor and why it is used
- How to declare, open, fetch, and close a cursor
- How to use cursor attributes and parameters
- How to handle exceptions and errors in cursor operations
- How to use implicit and explicit cursors

### What is a cursor and why it is used

A cursor is a pointer to a result set of a query. A cursor allows you to process each row individually and perform operations on it. A cursor is useful when you need to perform complex logic on each row, such as calculations, validations, or transformations. A cursor is also useful when you need to manipulate data in multiple tables based on the result of a query.

### How to declare, open, fetch, and close a cursor

To use a cursor, you need to perform four steps:

- Declare the cursor: This is done by using the `CURSOR` keyword and specifying the query that returns the result set. You can also optionally define parameters for the cursor that can be passed at runtime.
- Open the cursor: This is done by using the `OPEN` statement and passing the values for the parameters if any. This allocates memory for the cursor and executes the query.
- Fetch the cursor: This is done by using the `FETCH` statement and assigning the values of the current row to variables. This moves the cursor to the next row in the result set. You can use a loop to fetch all the rows until the cursor reaches the end of the result set.
- Close the cursor: This is done by using the `CLOSE` statement and releasing the memory allocated for the cursor. This terminates the cursor and frees the resources.

### How to use cursor attributes and parameters

A cursor has four attributes that can be used to check the status of the cursor. They are:

- `%FOUND`: This returns `TRUE` if the last fetch returned a row, and `FALSE` otherwise.
- `%NOTFOUND`: This returns `TRUE` if the last fetch did not return a row, and `FALSE` otherwise.
- `%ISOPEN`: This returns `TRUE` if the cursor is open, and `FALSE` otherwise.
- `%ROWCOUNT`: This returns the number of rows fetched so far by the cursor.

A cursor can also have parameters that can be used to pass values to the query at runtime. The parameters are declared in the cursor declaration using the `IN` keyword and the data type. The values for the parameters are passed in the `OPEN` statement using the `=>` operator.

### How to handle exceptions and errors in cursor operations

A cursor can raise exceptions and errors during its operations. Some of the common exceptions and errors are:

- `NO_DATA_FOUND`: This is raised when the query returns no rows or the cursor reaches the end of the result set.
- `TOO_MANY_ROWS`: This is raised when the query returns more than one row and the result is assigned to a scalar variable.
- `INVALID_CURSOR`: This is raised when the cursor is not open or is already closed.
- `CURSOR_ALREADY_OPEN`: This is raised when the cursor is already open and the `OPEN` statement is executed again.

To handle these exceptions and errors, you can use the `EXCEPTION` block and the `WHEN` clause to specify the actions to be taken. You can also use the `RAISE` statement to propagate the exception to the calling program or the `RAISE_APPLICATION_ERROR` statement to raise a user-defined error.

### How to use implicit and explicit cursors

There are two types of cursors in SQL: implicit and explicit. An implicit cursor is automatically created and managed by the SQL engine when you execute a single-row query, such as a `SELECT INTO` or a `DML` statement. An implicit cursor has the same attributes as an explicit cursor, but they are prefixed with `SQL` instead of the cursor name. For example, `SQL%FOUND` or `SQL%ROWCOUNT`.

An explicit cursor is created and managed by the programmer when you execute a multi-row query, such as a `SELECT` statement. An explicit cursor gives you more control and flexibility over the cursor operations, such as opening, fetching, and closing. You can also use explicit cursors to perform bulk operations, such as `BULK COLLECT` or `FORALL`, to improve the performance and efficiency of the cursor operations.