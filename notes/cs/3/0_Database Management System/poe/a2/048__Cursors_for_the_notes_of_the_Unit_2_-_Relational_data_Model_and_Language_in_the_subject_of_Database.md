 Here is the content in Markdown format without any emojis or external links:

### Cursors for the notes of the Unit 2 - Relational data Model and Language in the subject of Database Management System

1. A cursor is a pointer to a location in a result set. It allows us to process the rows in a result set one by one.
2. Cursors can be used to update/delete rows in a table. This is useful when we need to process rows individually and based on some condition update or delete the rows.
3. The following are the steps to use a cursor:

- Declare the cursor: This is done using a DECLARE statement. We have to specify the query to be used for fetching the data.
- Open the cursor: This is done using an OPEN statement. This executes the query specified while declaring the cursor and positions the cursor before the first row of the result set.
- Fetch rows: This is done using a FETCH statement. This fetches the current row or the next row based on the cursor position and stores it in variables for processing. This step is repeated in a loop until all rows are processed.
- Close the cursor: This is done using a CLOSE statement. This releases all resources associated with the cursor.

4. There are two types of cursors:

- Implicit cursors: These are automatically declared by the database system to process SQL statements like INSERT, UPDATE, DELETE, etc. and return a status message.
- Explicit cursors: These are user-defined cursors that are declared and manipulated using cursor statements. These allow us to fetch rows from the result set and process them individually.

5. Advantages of cursors:

- Process rows individually: Cursors allow us to process rows one by one. This is useful when we need to evaluate rows based on some conditions and then perform operations like updating or deleting.
- Save memory: Cursors save memory as only one row is fetched into the memory at a time. For large result sets, this can reduce the memory requirements.