# Unit 6 - Creating procedure and functions in the subject of Database Management Systems Lab

## Introduction

- A database management system (DBMS) is a software that allows users to create, manipulate, and manage data in a structured way.
- A DBMS consists of several components, such as data, schema, data dictionary, database engine, and database access language.
- Procedures and functions are two types of database objects that can be created and stored in a DBMS to perform specific tasks on data.
- Procedures and functions are similar in that they both contain a set of SQL statements that can be executed as a unit, and they both can accept parameters and return values.
- However, procedures and functions differ in some aspects, such as:

  - Procedures are mainly used to perform actions on data, such as insert, update, delete, or select. Functions are mainly used to return a single value or a table based on some calculations or logic.
  - Procedures can use control flow statements, such as if-else, while, or case. Functions cannot use control flow statements, but they can use conditional expressions, such as case or coalesce.
  - Procedures can affect the state of the database by modifying data or calling other procedures. Functions cannot affect the state of the database, and they can only call other functions.
  - Procedures can return multiple values or result sets using output parameters or return statements. Functions can only return one value or result set using a return statement.

## Creating procedures and functions in DBMS

- The syntax and steps for creating procedures and functions may vary depending on the DBMS and the database access language used. However, the general process is similar for most DBMSs, such as SQL Server, Oracle, MySQL, or PostgreSQL.
- To create a procedure or a function, the following steps are usually required:

  - Specify the name of the procedure or function, and optionally the schema and the parameters.
  - Specify the return type of the function, if applicable.
  - Specify the options or attributes of the procedure or function, such as security context, encryption, or recompilation.
  - Define the body of the procedure or function, which contains the SQL statements to be executed.
  - End the definition of the procedure or function with a semicolon or a delimiter, depending on the DBMS.
  - Execute the create statement to create the procedure or function in the database.

- For example, the following SQL statements create a procedure and a function in SQL Server:

  ```sql
  -- Create a procedure that inserts a new product into the Products table
  CREATE PROCEDURE dbo.InsertProduct
  @ProductName varchar(50),
  @Price decimal(18,2),
  @CategoryID int
  AS
  BEGIN
    INSERT INTO Products (ProductName, Price, CategoryID)
    VALUES (@ProductName, @Price, @CategoryID)
  END;
  GO

  -- Create a function that returns the average price of products in a given category
  CREATE FUNCTION dbo.AvgPriceByCategory
  (@CategoryID int)
  RETURNS decimal(18,2)
  AS
  BEGIN
    DECLARE @AvgPrice decimal(18,2)
    SELECT @AvgPrice = AVG(Price) FROM Products WHERE CategoryID = @CategoryID
    RETURN @AvgPrice
  END;
  GO
  ```

## Executing procedures and functions in DBMS

- To execute a procedure or a function, the following steps are usually required:

  - Specify the name of the procedure or function, and optionally the schema and the parameters.
  - Specify the output parameters or variables to receive the return values, if applicable.
  - Execute the call statement or use the function name in an expression, depending on the DBMS and the database access language used.

- For example, the following SQL statements execute the procedure and the function created in the previous example in SQL Server:

  ```sql
  -- Execute the procedure to insert a new product
  EXEC dbo.InsertProduct @ProductName = 'Laptop', @Price = 999.99, @CategoryID = 1;
  GO

  -- Execute the function to get the average price of products in category 1
  DECLARE @AvgPrice decimal(18,2)
  SELECT @AvgPrice = dbo.AvgPriceByCategory(1)
  PRINT @AvgPrice
  GO
  ```