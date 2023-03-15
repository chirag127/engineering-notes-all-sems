# Unit 5 - Creating cursor in the subject of Database Management Systems Lab

## What is a cursor?

- A cursor is a temporary memory area that holds the result set of a query and allows row-by-row processing of the data.
- A cursor can be used to perform operations on each row of the result set, such as updating, deleting, or fetching data.
- A cursor can also be used to handle complex logic that cannot be expressed in a single SQL statement.

## Types of cursors

- There are two types of cursors: implicit and explicit.
- An implicit cursor is automatically created and managed by the database system for every SQL statement that returns a result set. For example, a SELECT statement creates an implicit cursor.
- An explicit cursor is created and controlled by the user using the DECLARE, OPEN, FETCH, and CLOSE statements. An explicit cursor can be named and customized according to the user's needs.

## How to create an explicit cursor

- The following steps are involved in creating an explicit cursor:

  1. Declare the cursor name and the SQL statement that defines the result set. For example:

     ```sql
     DECLARE cursor_name CURSOR FOR SELECT * FROM table_name;
     ```

  2. Open the cursor to execute the SQL statement and populate the result set in the memory. For example:

     ```sql
     OPEN cursor_name;
     ```

  3. Fetch the data from the cursor one row at a time and perform the desired operations on each row. For example:

     ```sql
     FETCH cursor_name INTO variable1, variable2, ...;
     ```

  4. Close the cursor to release the memory and resources associated with it. For example:

     ```sql
     CLOSE cursor_name;
     ```

## Examples of creating cursors in different databases

- The syntax and features of cursors may vary slightly depending on the database system. Here are some examples of creating cursors in different databases:

  - SQL Server:

    ```sql
    -- Declare the cursor
    DECLARE employee_cursor CURSOR FOR
    SELECT id, name, salary FROM employee;

    -- Declare variables to hold the fetched data
    DECLARE @id INT, @name VARCHAR(50), @salary DECIMAL(10,2);

    -- Open the cursor
    OPEN employee_cursor;

    -- Fetch the first row
    FETCH NEXT FROM employee_cursor INTO @id, @name, @salary;

    -- Loop through the cursor until no more rows are available
    WHILE @@FETCH_STATUS = 0
    BEGIN
      -- Perform some operation on each row, for example, print the data
      PRINT 'ID: ' + CAST(@id AS VARCHAR) + ', Name: ' + @name + ', Salary: ' + CAST(@salary AS VARCHAR);

      -- Fetch the next row
      FETCH NEXT FROM employee_cursor INTO @id, @name, @salary;
    END

    -- Close the cursor
    CLOSE employee_cursor;

    -- Deallocate the cursor
    DEALLOCATE employee_cursor;
    ```

  - Oracle:

    ```sql
    -- Declare the cursor
    DECLARE
      CURSOR employee_cursor IS
      SELECT id, name, salary FROM employee;

      -- Declare variables to hold the fetched data
      v_id employee.id%TYPE;
      v_name employee.name%TYPE;
      v_salary employee.salary%TYPE;
    BEGIN
      -- Open the cursor
      OPEN employee_cursor;

      -- Loop through the cursor until no more rows are available
      LOOP
        -- Fetch the next row
        FETCH employee_cursor INTO v_id, v_name, v_salary;

        -- Exit the loop if no more rows are available
        EXIT WHEN employee_cursor%NOTFOUND;

        -- Perform some operation on each row, for example, print the data
        DBMS_OUTPUT.PUT_LINE('ID: ' || v_id || ', Name: ' || v_name || ', Salary: ' || v_salary);
      END LOOP;

      -- Close the cursor
      CLOSE employee_cursor;
    END;
    ```

  - MySQL:

    ```sql
    -- Declare the cursor
    DECLARE employee_cursor CURSOR FOR
    SELECT id, name, salary FROM employee;

    -- Declare a variable to indicate the end of the cursor
    DECLARE done INT DEFAULT FALSE;

    -- Declare variables to hold the fetched data
    DECLARE v_id INT;
    DECLARE v_name VARCHAR(50);
    DECLARE v_salary DECIMAL(10,2);

    -- Declare a handler to set the done variable to true when no more rows are available
    DECLARE CONTINUE HANDLER