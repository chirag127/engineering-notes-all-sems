 Here is the content in Markdown format without any external links or emojis and in a formal tone:

### Notes for Unit 6 - Creating procedure and functions

1. Procedures:
- Procedures are a set of SQL statements that are stored in the database and can be executed whenever required.
- They are used to encapsulate frequently performed operations/logic.
- They eliminate the need to rewrite the same logic/set of statements multiple times.
- They improve performance as the procedure execution plan can be reused.
- They can take input parameters and return values or result sets.

2. Functions:
- Functions are similar to procedures but they can return only one value.
- They take input parameters and perform certain operations on the data and return a value.
- They can be used in the SELECT and WHERE clauses along with other expressions.
- They encapsulate complex expressions/logic and make the queries concise and readable.

3. Advantages of using procedures and functions:
- Code reusability
- Modularization of logic
- Improved performance
- Simplicity and readability of queries

4. Steps to create procedures and functions:
- Use CREATE PROCEDURE or CREATE FUNCTION statement.
- Specify the input parameters (if any) along with their data types and modes (IN, OUT, INOUT).
- Include the SQL statements that implement the logic.
- For functions, include a RETURN statement to return a value.
- Test the procedure/function and call it from queries/other procedures and functions.

5. Security aspects:
- Only users with appropriate privileges can create/access/execute procedures and functions.
- Users can be granted limited privileges to only access specific procedures and functions. This enables secure data access.
- Procedures and functions can be encrypted to prevent users from viewing the underlying logic.