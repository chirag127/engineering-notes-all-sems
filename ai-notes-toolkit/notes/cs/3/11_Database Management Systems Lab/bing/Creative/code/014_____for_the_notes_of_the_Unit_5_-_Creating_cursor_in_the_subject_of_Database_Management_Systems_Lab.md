# Unit 5 - Creating cursor in the subject of Database Management Systems Lab

- A cursor is a temporary memory area that holds the result set of a query and allows row-by-row processing of the data.
- A cursor can be used to perform complex calculations, validations, or manipulations on the data that cannot be done using a single SQL statement.
- A cursor can be either implicit or explicit. An implicit cursor is automatically created and managed by the database system for each SQL statement. An explicit cursor is created and controlled by the user using the cursor commands.
- The steps involved in creating an explicit cursor are:
  - Declare: This step defines the name and the query of the cursor. The syntax is:

    ```sql
    DECLARE cursor_name CURSOR FOR SELECT * FROM table_name;
    ```

  - Open: This step executes the query and populates the cursor with the result set. The syntax is:

    ```sql
    OPEN cursor_name;
    ```

  - Fetch: This step retrieves one row at a time from the cursor and assigns the values to the variables. The syntax is:

    ```sql
    FETCH cursor_name INTO variable1, variable2, ...;
    ```

  - Close: This step releases the memory allocated for the cursor and closes it. The syntax is:

    ```sql
    CLOSE cursor_name;
    ```

- A cursor can have different attributes, such as:
  - Type: A cursor can be either forward-only or scrollable. A forward-only cursor can only move from the first row to the last row. A scrollable cursor can move in any direction and to any position in the result set.
  - Sensitivity: A cursor can be either sensitive or insensitive to the changes made to the underlying data. A sensitive cursor reflects the changes in the result set. An insensitive cursor does not reflect the changes in the result set.
  - Concurrency: A cursor can be either read-only or updatable. A read-only cursor can only fetch the data from the result set. An updatable cursor can modify, insert, or delete the data in the result set.
- A cursor can be used for different purposes, such as:
  - To perform row-level validations or calculations that cannot be done using a single SQL statement.
  - To perform complex business logic or data manipulation that requires multiple SQL statements.
  - To handle exceptions or errors that occur during the execution of a query.
  - To generate dynamic SQL statements based on the data in the result set.