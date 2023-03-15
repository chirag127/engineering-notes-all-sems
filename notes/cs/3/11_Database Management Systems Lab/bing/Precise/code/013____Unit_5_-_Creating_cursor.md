## Unit 5 - Creating cursor

A cursor is a control structure that enables traversal over the records in a database. Cursors allow you to iterate over a set of rows returned by a query and process each row individually. Here are the steps to create a cursor:

1. Declare the cursor: This defines the cursor and associates it with a SELECT statement that retrieves the rows to be traversed.
2. Open the cursor: This executes the SELECT statement associated with the cursor and populates the result set.
3. Fetch the data: This retrieves the rows from the result set, one at a time. You can perform operations on the data as you retrieve it.
4. Close the cursor: This releases the resources associated with the cursor.
5. Deallocate the cursor: This removes the cursor definition and releases the associated resources.

It is important to properly manage the resources associated with a cursor, including closing and deallocating the cursor when it is no longer needed. Failing to do so can result in memory leaks and reduced performance.