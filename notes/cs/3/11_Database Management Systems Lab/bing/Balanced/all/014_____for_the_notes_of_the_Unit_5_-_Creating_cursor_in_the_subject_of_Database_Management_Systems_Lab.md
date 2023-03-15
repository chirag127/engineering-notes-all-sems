# Unit 5 - Creating Cursor in Database Management Systems Lab

- A cursor is a temporary memory area that holds the result set of a query and allows row-by-row processing of the data.
- Cursors can be classified into two types: implicit and explicit.
- Implicit cursors are automatically created and managed by the database system for each query statement. They are not visible to the user and have limited functionality.
- Explicit cursors are user-defined and can be customized to suit the needs of the application. They are visible to the user and have more functionality and flexibility.
- To create an explicit cursor, the following steps are required:
  - Declare the cursor name and the query that populates it.
  - Open the cursor to execute the query and store the result set in the cursor.
  - Fetch the rows from the cursor one by one or in batches and perform the desired operations on them.
  - Close the cursor to release the memory and resources associated with it.
- The syntax for declaring a cursor may vary slightly depending on the database system, but the general form is:

```sql
DECLARE cursor_name CURSOR FOR SELECT * FROM table_name;
```

- The syntax for opening a cursor is:

```sql
OPEN cursor_name;
```

- The syntax for fetching a row from a cursor is:

```sql
FETCH cursor_name INTO variable_list;
```

- The syntax for closing a cursor is:

```sql
CLOSE cursor_name;
```

- Some examples of creating and using cursors in different databases are:

  - SQL Server:

  ```sql
  -- Declare a cursor
  DECLARE employee_cursor CURSOR FOR
  SELECT name, salary FROM employee;

  -- Open the cursor
  OPEN employee_cursor;

  -- Declare variables to hold the fetched data
  DECLARE @name VARCHAR(50), @salary INT;

  -- Fetch the first row
  FETCH NEXT FROM employee_cursor INTO @name, @salary;

  -- Loop through the cursor until no more rows are available
  WHILE @@FETCH_STATUS = 0
  BEGIN
    -- Perform some operation on the fetched data
    PRINT 'Name: ' + @name + ', Salary: ' + CAST(@salary AS VARCHAR);

    -- Fetch the next row
    FETCH NEXT FROM employee_cursor INTO @name, @salary;
  END

  -- Close the cursor
  CLOSE employee_cursor;

  -- Deallocate the cursor
  DEALLOCATE employee_cursor;
  ```

  - Oracle:

  ```sql
  -- Declare a cursor
  DECLARE
    CURSOR employee_cursor IS
    SELECT name, salary FROM employee;

    -- Declare variables to hold the fetched data
    name VARCHAR(50);
    salary NUMBER;
  BEGIN
    -- Open the cursor
    OPEN employee_cursor;

    -- Loop through the cursor until no more rows are available
    LOOP
      -- Fetch the next row
      FETCH employee_cursor INTO name, salary;

      -- Exit the loop if no more rows are available
      EXIT WHEN employee_cursor%NOTFOUND;

      -- Perform some operation on the fetched data
      DBMS_OUTPUT.PUT_LINE('Name: ' || name || ', Salary: ' || salary);
    END LOOP;

    -- Close the cursor
    CLOSE employee_cursor;
  END;
  ```

  - MySQL:

  ```sql
  -- Declare a cursor
  DECLARE employee_cursor CURSOR FOR
  SELECT name, salary FROM employee;

  -- Declare a variable to indicate the end of the cursor
  DECLARE done INT DEFAULT FALSE;

  -- Declare a handler to set the done variable to true when no more rows are available
  DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

  -- Declare variables to hold the fetched data
  DECLARE name VARCHAR(50), salary INT;

  -- Open the cursor
  OPEN employee_cursor;

  -- Loop through the cursor until no more rows are available
  read_loop: LOOP
    -- Fetch the next row
    FETCH employee_cursor INTO name, salary;

    -- Exit the loop if no more rows are available
    IF done THEN
      LEAVE read_loop;
    END IF;

    -- Perform some operation on the fetched data
    SELECT CONCAT('Name: ', name, ', Salary: ', salary);
  END LOOP;

  -- Close the cursor
  CLOSE employee_cursor;
  ```

  - PostgreSQL:

  ```sql
  -- Declare a cursor
  DECLARE employee_cursor CURSOR FOR
  SELECT name, salary FROM employee;

  -- Declare variables to hold the fetched data
  name VARCHAR(50);
  salary INT;

  -- Open the cursor
  OPEN