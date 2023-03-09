 Here is the content in markdown format for the given topic:

### Cursors for the notes of the Unit 2 - Relational data Model and Language in the subject of Database Management System

- A cursor is a database object which is used to retrieve data from a result set one row at a time.
- Cursors allow traversing over the rows of a result set in a controlled manner. They make it possible to process individual rows rather than the entire result set at once.
- Cursors are used when the result set is very large and we only need to process a small portion of the rows. They help in minimizing memory usage and improve performance as only a few rows are fetched into the memory at a time.
- The rows in the cursor can be updated or deleted and the updates are made to the database.
- There are two types of cursors:

1. Implicit Cursors - These are automatically defined cursors created by Oracle when executing a SQL statement that returns rows like a SELECT statement. The name of the implicit cursor is SYSTEM_CURSOR.

2. Explicit Cursors - These are user-defined cursors that are explicitly declared and named by the user. The user can define the attributes of an explicit cursor and manipulate it.

- The steps to use a cursor are:

1. Declare the cursor - Define the cursor with a SELECT statement.
2. Open the cursor - Open the cursor to execute the query and retrieve the result set.
3. Fetch the rows - Fetch the rows from the result set one by one.
4. Close the cursor - Close the cursor after processing to release the resources.

- Advantages:

1. Memory efficient - Only a small amount of data is fetched into memory at a time.
2. Performance - Avoid expensive operations of fetching large amounts of data at once.
3. Flexibility - Cursors allow great flexibility in manipulating the result set.

- Disadvantages:

1. Additional Overhead - There is some additional overhead involved in declaring, opening, fetching and closing cursors.
2. Complexity - The code to handle cursors is more complex than simply running a query and processing all rows at once.

- Examples and applications can be included with codes to demonstrate the usage of cursors.