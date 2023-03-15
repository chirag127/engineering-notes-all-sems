### Unit 5 - Creating cursor in the subject of Database Management Systems Lab

- A cursor is a temporary memory area that holds the result set of a query and allows row-by-row processing of the data.
- Cursors can be classified into two types: implicit and explicit.
- Implicit cursors are automatically created and managed by the database system for each query statement. They are not visible to the user and have limited functionality.
- Explicit cursors are user-defined and can be customized to perform various operations on the result set. They are visible to the user and have more functionality.
- To create an explicit cursor, the following steps are required:
  - Declare the cursor name and the query that populates it.
  - Open the cursor to execute the query and store the result set in the memory.
  - Fetch the rows from the cursor one by one or in batches and perform the desired actions on them.
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

- Some examples of creating and using cursors in different database systems are:

```sql
-- SQL Server
DECLARE employee_cursor CURSOR FOR
SELECT name, salary FROM employee;

OPEN employee_cursor;

FETCH NEXT FROM employee_cursor INTO @name, @salary;

WHILE @@FETCH_STATUS = 0
BEGIN
  -- Do something with @name and @salary
  FETCH NEXT FROM employee_cursor INTO @name, @salary;
END

CLOSE employee_cursor;
DEALLOCATE employee_cursor;
```

```sql
-- Oracle
DECLARE
  name VARCHAR2(50);
  salary NUMBER;
  CURSOR employee_cursor IS
  SELECT name, salary FROM employee;
BEGIN
  OPEN employee_cursor;
  LOOP
    FETCH employee_cursor INTO name, salary;
    EXIT WHEN employee_cursor%NOTFOUND;
    -- Do something with name and salary
  END LOOP;
  CLOSE employee_cursor;
END;
```

```sql
-- MySQL
DECLARE employee_cursor CURSOR FOR
SELECT name, salary FROM employee;

OPEN employee_cursor;

read_loop: LOOP
  FETCH employee_cursor INTO name, salary;
  IF done THEN
    LEAVE read_loop;
  END IF;
  -- Do something with name and salary
END LOOP;

CLOSE employee_cursor;
```

```sql
-- PostgreSQL
DECLARE employee_cursor CURSOR FOR
SELECT name, salary FROM employee;

OPEN employee_cursor;

LOOP
  FETCH employee_cursor INTO name, salary;
  EXIT WHEN NOT FOUND;
  -- Do something with name and salary
END LOOP;

CLOSE employee_cursor;
```