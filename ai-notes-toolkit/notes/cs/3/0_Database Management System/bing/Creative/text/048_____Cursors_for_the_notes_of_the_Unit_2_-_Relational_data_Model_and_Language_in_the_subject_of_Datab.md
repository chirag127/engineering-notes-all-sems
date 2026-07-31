### Cursors

- A cursor is a database object that allows you to manipulate data in a row-by-row manner.
- A cursor can be thought of as a pointer to a specific row within a query result .
- Cursors facilitate subsequent processing in conjunction with the traversal, such as retrieval, addition and removal of database records.
- Cursors are an extension to result sets that provide mechanisms for positioning at specific rows, retrieving one row or block of rows, and supporting data modifications.
- Cursors are useful when you need to perform complex logic on a row-by-row basis, or when you need to access the same result set multiple times.
- Cursors have four steps in their lifecycle: declare, open, fetch, and close .
  - Declare a cursor: A cursor is declared by defining a SQL statement that returns a result set.
  - Open a cursor: A cursor is opened by executing the SQL statement and allocating memory for the result set.
  - Fetch a cursor: A cursor is fetched by moving the pointer to a specific row and retrieving the data from that row.
  - Close a cursor: A cursor is closed by releasing the memory allocated for the result set and deleting the cursor object.
- Cursors can have different types and options that affect their behavior and performance .
  - Static cursor: A static cursor creates a temporary copy of the result set and works on that copy. It is not affected by any changes made to the underlying data.
  - Dynamic cursor: A dynamic cursor reflects any changes made to the underlying data in the result set. It allows scrolling forward and backward, and updating and deleting rows.
  - Forward-only cursor: A forward-only cursor only allows scrolling forward through the result set. It is faster than a static or dynamic cursor, but does not support backward scrolling or data modifications.
  - Keyset-driven cursor: A keyset-driven cursor creates a temporary set of keys that identify the rows in the result set. It allows scrolling forward and backward, and updating rows, but not deleting or inserting rows.
  - Read-only cursor: A read-only cursor does not allow any data modifications to the result set. It is faster than an updatable cursor, but does not support updating, deleting, or inserting rows.
  - Scroll cursor: A scroll cursor allows scrolling forward and backward through the result set. It can be either static, dynamic, or keyset-driven.
  - Updatable cursor: An updatable cursor allows data modifications to the result set. It can be either dynamic or keyset-driven.