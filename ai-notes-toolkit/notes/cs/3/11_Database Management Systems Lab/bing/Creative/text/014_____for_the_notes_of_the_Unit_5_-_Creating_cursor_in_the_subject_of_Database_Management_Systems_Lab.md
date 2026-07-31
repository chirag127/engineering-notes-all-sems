# Unit 5 - Creating cursor in the subject of Database Management Systems Lab

- A cursor is a temporary memory area that holds the result set of a query and allows row-by-row processing of the data.
- Cursors can be classified into two types: implicit and explicit.
- Implicit cursors are automatically created and managed by the database system for each query statement.
- Explicit cursors are user-defined and require four steps to create and use: declare, open, fetch, and close.
- The declare step defines the name and the SQL statement of the cursor.
- The open step executes the SQL statement and populates the cursor with the result set.
- The fetch step retrieves one or more rows from the cursor and assigns them to variables or records.
- The close step releases the memory allocated for the cursor and invalidates it.
- The syntax for creating an explicit cursor may vary slightly depending on the database system, but the general form is:

```
DECLARE cursor_name CURSOR FOR select_statement;
OPEN cursor_name;
FETCH cursor_name INTO variables_or_records;
CLOSE cursor_name;
```

- Some examples of creating explicit cursors in different databases are:

  - SQL Server:

  ```
  DECLARE employee_cursor CURSOR FOR
  SELECT id, name, salary FROM employee;
  OPEN employee_cursor;
  FETCH NEXT FROM employee_cursor INTO @id, @name, @salary;
  CLOSE employee_cursor;
  DEALLOCATE employee_cursor;
  ```

  - Oracle:

  ```
  DECLARE
  CURSOR employee_cursor IS
  SELECT id, name, salary FROM employee;
  id NUMBER;
  name VARCHAR2(50);
  salary NUMBER;
  BEGIN
  OPEN employee_cursor;
  LOOP
  FETCH employee_cursor INTO id, name, salary;
  EXIT WHEN employee_cursor%NOTFOUND;
  -- do something with the fetched data
  END LOOP;
  CLOSE employee_cursor;
  END;
  ```

  - MySQL:

  ```
  DELIMITER //
  CREATE PROCEDURE employee_cursor()
  BEGIN
  DECLARE id INT;
  DECLARE name VARCHAR(50);
  DECLARE salary DECIMAL(10,2);
  DECLARE done INT DEFAULT FALSE;
  DECLARE employee_cursor CURSOR FOR
  SELECT id, name, salary FROM employee;
  DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
  OPEN employee_cursor;
  read_loop: LOOP
  FETCH employee_cursor INTO id, name, salary;
  IF done THEN
  LEAVE read_loop;
  END IF;
  -- do something with the fetched data
  END LOOP;
  CLOSE employee_cursor;
  END //
  DELIMITER ;
  ```

  - PostgreSQL:

  ```
  BEGIN;
  DECLARE employee_cursor CURSOR FOR
  SELECT id, name, salary FROM employee;
  FETCH NEXT FROM employee_cursor;
  -- do something with the fetched data
  CLOSE employee_cursor;
  COMMIT;
  ```