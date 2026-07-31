# Unit 5 - Creating cursor in the subject of Database Management Systems Lab

## What is a cursor?

- A cursor is a temporary memory area that stores the result set of a query and allows row-by-row processing of the data.
- A cursor can be used to perform operations on each row of the result set, such as updating, deleting, or fetching data.
- A cursor can be either implicit or explicit, depending on how it is created and used.

## What is an implicit cursor?

- An implicit cursor is a cursor that is automatically created and managed by the database system whenever a SQL statement is executed.
- An implicit cursor is not explicitly declared or opened by the user, but it can be accessed by using some predefined attributes, such as %FOUND, %NOTFOUND, %ROWCOUNT, and %ISOPEN.
- An implicit cursor is closed automatically after the SQL statement is executed.

## What is an explicit cursor?

- An explicit cursor is a cursor that is explicitly declared and opened by the user using the CURSOR keyword and the OPEN, FETCH, and CLOSE statements.
- An explicit cursor is used when the user needs more control over the processing of the result set, such as when the query returns more than one row or when the user needs to perform some logic on each row.
- An explicit cursor can have parameters and a return type, and it can be used in loops, conditional statements, and exception handling blocks.

## How to create an explicit cursor?

- There are four steps involved in creating and using an explicit cursor:

  - Declare the cursor using the CURSOR keyword, followed by the cursor name, optional parameters, optional return type, and the SQL query that populates the cursor.
  - Open the cursor using the OPEN statement, followed by the cursor name and optional arguments. This allocates memory for the cursor and executes the query.
  - Fetch data from the cursor using the FETCH statement, followed by the cursor name and the variables or record that store the data. This retrieves one row at a time from the cursor and assigns the values to the variables or record. The FETCH statement can be used in a loop to process all the rows in the cursor.
  - Close the cursor using the CLOSE statement, followed by the cursor name. This releases the memory allocated for the cursor and terminates the query.

- The syntax for declaring a cursor is:

  ```sql
  CURSOR cursor_name [(parameter, [parameter...])] [RETURN return_type] IS
  sql_statement [FOR UPDATE [OF column_list]];
  ```

- The syntax for opening a cursor is:

  ```sql
  OPEN cursor_name [(argument, [argument...])];
  ```

- The syntax for fetching data from a cursor is:

  ```sql
  FETCH cursor_name INTO variable_list | record_name;
  ```

- The syntax for closing a cursor is:

  ```sql
  CLOSE cursor_name;
  ```

## Example of creating an explicit cursor

- Suppose we have a table called STUDENTS with the following columns and data:

  | ID | NAME | AGE | GRADE |
  | -- | ---- | --- | ----- |
  | 1  | Alice | 20  | A     |
  | 2  | Bob   | 21  | B     |
  | 3  | Charlie | 19 | C     |
  | 4  | David | 22  | D     |

- We want to create a cursor that selects the name and grade of all the students whose age is greater than 20, and print them on the screen.

- We can use the following PL/SQL code to create and use the cursor:

  ```sql
  -- Declare the cursor
  CURSOR c_students IS
  SELECT name, grade FROM students WHERE age > 20;

  -- Declare variables to store the data
  v_name VARCHAR2(20);
  v_grade CHAR(1);

  BEGIN
    -- Open the cursor
    OPEN c_students;

    -- Loop through the cursor
    LOOP
      -- Fetch data from the cursor
      FETCH c_students INTO v_name, v_grade;

      -- Exit the loop when there are no more rows
      EXIT WHEN c_students%NOTFOUND;

      -- Print the data on the screen
      DBMS_OUTPUT.PUT_LINE(v_name || ' - ' || v_grade);
    END LOOP;

    -- Close the cursor
    CLOSE c_students;
  END;
  ```

- The output of the code will be:

  ```
  Bob - B
  David - D
  ```