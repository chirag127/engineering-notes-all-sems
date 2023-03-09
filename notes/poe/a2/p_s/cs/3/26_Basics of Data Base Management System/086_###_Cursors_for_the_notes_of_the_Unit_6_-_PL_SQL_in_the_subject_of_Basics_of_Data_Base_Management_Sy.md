 Here is the content in markdown format for the given topic:

### Cursors for the notes of the Unit 6 - PL/SQL in the subject of Basics of Data Base Management System

**What are Cursors?**

- Cursors are database objects which allow traversing over the rows of a result set one at a time.
- They are used to fetch and process each row of a query result set individually.
- Cursors allow us to process query results row-by-row so that we can apply the required logic/processing on each row.
- They are useful when we need to perform some action on each row of the result set like updating or deleting records.

**Types of Cursors:**

- Implicit Cursors: These are automatically defined and created by Oracle whenever an SQL statement is executed. We can fetch rows from it using `FETCH` statement.
- Explicit Cursors: These are user-defined cursors which are explicitly declared and defined. They allow greater flexibility and control over the query processing.

**Steps to use Explicit Cursors:**

1. Declare the cursor specifying the query
2. Open the cursor
3. Fetch rows from the cursor one by one
4. Process the rows
5. Close the cursor

**Advantages of Cursors:**

- They allow processing query results row-by-row.
- Greater control over query processing.
- Can handle complex logic on each row.

**Disadvantages of Cursors:**

- Performance can degrade if a large number of rows are being processed.
- Program logic can become complex if many cursors are used.
- Not suitable if only aggregate values are required from the query result.

**Examples and Applications of Cursors:**

[Include relevant examples and applications of cursors with code snippets and diagrams for better understanding.]