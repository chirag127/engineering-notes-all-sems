 Here is the content in markdown format for the topic ### Queries and Sub Queries for the notes of the Unit 2 - Relational data Model and Language in the subject of Database Management System:

### Queries and Subqueries

- A **query** is a request for data from a database table or combination of tables.
- A **subquery** is a query inside a query. It is used to filter records or to provide values to be used in the main query.
- Subqueries are executed first, and their output is used by the main query.
- Subqueries must be enclosed within parentheses "()".

**Types of Subqueries:**

1. Scalar Subquery: Returns a single value. Used with =, <>, >, >=, <, <=.
Example: Select Name from Employees where Salary > (Select Salary from Employees where Name = 'John');

2. Row Subquery: Returns one row. Used with =, <>, >, >=, <, <=.
Example: Select * from Employees where Salary = (Select Max(Salary) from Employees);

3. Table Subquery: Returns multiple rows and columns. Used with IN, NOT IN.
Example: Select * from Employees where Department IN (Select Department from Departments where Location = 'Delhi');

**Advantages of Subqueries:**

- Provide an efficient way to get data from related tables.
- Avoid complex joins.
- Enhance readability of queries.
- Can be used in different clauses like SELECT, WHERE, HAVING.

**Disadvantages of Subqueries:**

- Can be slower than joins.
- Complex subqueries can be difficult to understand and debug.
- Might cause issues if not properly optimized.

**Applications of Subqueries:**

- Finding minimum/maximum value
- Retrieving rows based on some condition
- Counting rows that meet some criteria
- Performing aggregate calculations