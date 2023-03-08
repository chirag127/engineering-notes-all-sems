 Here is the content in markdown format for the notes of Unit 6 - Creating procedure and functions in the subject of Database Management Systems Lab:

### Creating Procedures and Functions

- Procedures and functions are blocks of SQL code that can be reused and shared.
- Procedures are used to execute a sequence of SQL statements as a unit to solve a specific problem or perform a set of related tasks.
- Functions are similar to procedures but they can return a value. Functions can be used in expressions and queries in place of literal values or expressions.
- The main benefits of procedures and functions are:

- Reusability - The code can be reused many times without rewriting it.
- Maintainability - Only need to update the procedure/function definition to fix bugs or modify logic.
- Readability - Procedures and functions can have meaningful names that describe the logic, making scripts more readable.

- To create a procedure:

USE database;
CREATE PROCEDURE procedure_name
(parameters)
BEGIN
-- procedure statements
END;

- To create a function:

USE database;
CREATE FUNCTION function_name
(parameters)
RETURNS datatype
BEGIN
-- function statements
RETURN value;
END;

- Examples:

CREATE PROCEDURE GetCustomerCount()
BEGIN
SELECT COUNT(*) FROM Customers;
END;

CALL GetCustomerCount();

CREATE FUNCTION GetCustomerCount()
RETURNS INT
BEGIN
RETURN (SELECT COUNT(*) FROM Customers);
END;

SELECT GetCustomerCount();

- Advantages: Reusability, Maintainability, Readability
- Disadvantages: Additional overhead, Dependencies between procedures/functions and tables
- Applications: Performing complex logic, Encapsulating queries, Preserving business rules