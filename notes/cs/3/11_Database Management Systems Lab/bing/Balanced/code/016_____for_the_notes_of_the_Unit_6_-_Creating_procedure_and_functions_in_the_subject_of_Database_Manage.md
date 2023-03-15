# Unit 6 - Creating procedure and functions in the subject of Database Management Systems Lab

- A **procedure** is a set of SQL statements that can be executed as a single unit. Procedures can be used to perform common or repetitive tasks, such as inserting, updating, deleting, or selecting data from a table. Procedures can also accept parameters and return values, making them more flexible and reusable. Procedures are stored in the database and can be invoked by other SQL statements or applications. 

- A **function** is a special type of procedure that returns a single value. Functions can be used to perform calculations, manipulate strings, or convert data types. Functions can also accept parameters, but they cannot modify the database state. Functions are stored in the database and can be invoked by other SQL statements or expressions. 

- To create a procedure or a function in a database management system, you need to use the **CREATE PROCEDURE** or **CREATE FUNCTION** statement, respectively. The syntax of these statements varies depending on the database system, but generally they include the following elements:

  - The name of the procedure or function, optionally prefixed by a schema name.
  - The list of parameters, if any, enclosed in parentheses. Each parameter has a name, a data type, and a mode (IN, OUT, or INOUT).
  - The return type, if the object is a function.
  - The body of the procedure or function, which contains the SQL statements to be executed. The body can be enclosed in a BEGIN...END block, or in some cases, a single statement can be used.
  - The optional clauses, such as WITH EXECUTE AS, which specify the security context or other options for the procedure or function.  

- To execute a procedure or a function, you need to use the **EXECUTE** or **CALL** statement, or simply the name of the object followed by the arguments, if any. The syntax of these statements also varies depending on the database system, but generally they include the following elements:

  - The name of the procedure or function, optionally prefixed by a schema name.
  - The list of arguments, if any, enclosed in parentheses. Each argument can be a literal value, a variable, or an expression. The arguments must match the parameters in number, order, and data type.
  - The optional clauses, such as INTO, which specify the variables or locations where the output or return values of the procedure or function are stored.  

- Some examples of creating and executing procedures and functions in different database systems are:

  - SQL Server:

    ```sql
    -- Create a procedure that inserts a new product into the Products table
    CREATE PROCEDURE dbo.InsertProduct
      @ProductName nvarchar(40),
      @SupplierID int,
      @CategoryID int,
      @UnitPrice money
    AS
    BEGIN
      INSERT INTO Products (ProductName, SupplierID, CategoryID, UnitPrice)
      VALUES (@ProductName, @SupplierID, @CategoryID, @UnitPrice);
    END;
    GO

    -- Execute the procedure with some values
    EXECUTE dbo.InsertProduct 'Chai', 1, 1, 18.00;
    GO
    ```

    ```sql
    -- Create a function that returns the total sales for a given product
    CREATE FUNCTION dbo.GetTotalSales
      (@ProductID int)
    RETURNS money
    AS
    BEGIN
      DECLARE @TotalSales money;
      SELECT @TotalSales = SUM(UnitPrice * Quantity * (1 - Discount))
      FROM [Order Details]
      WHERE ProductID = @ProductID;
      RETURN @TotalSales;
    END;
    GO

    -- Execute the function with some values
    SELECT dbo.GetTotalSales(1) AS TotalSales;
    GO
    ```

  - MySQL:

    ```sql
    -- Create a procedure that inserts a new product into the products table
    CREATE PROCEDURE InsertProduct(
      IN p_name VARCHAR(50),
      IN p_price DECIMAL(10,2),
      IN p_category VARCHAR(50)
    )
    BEGIN
      INSERT INTO products (name, price, category)
      VALUES (p_name, p_price, p_category);
    END;

    -- Execute the procedure with some values
    CALL InsertProduct('Chai', 18.00, 'Beverages');
    ```

    ```sql
    -- Create a function that returns the total sales for a given product
    CREATE