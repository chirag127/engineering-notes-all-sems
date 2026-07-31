### SQL within PL/SQL

- SQL stands for Structured Query Language, which is a standard language for accessing and manipulating data in relational databases.
- PL/SQL stands for Procedural Language/Structured Query Language, which is an extension of SQL that allows developers to write procedural code using SQL statements within its syntax .
- PL/SQL blocks are the basic units of PL/SQL programs, which can be nested within each other. A PL/SQL block consists of three sections: declaration, executable, and exception .
- Declaration section: This section is optional and declares variables, constants, cursors, and user-defined types that are used in the block.
- Executable section: This section is mandatory and contains the logic of the block, which can include SQL statements, assignments, loops, conditional statements, and calls to other PL/SQL blocks or subprograms.
- Exception section: This section is optional and handles any errors or exceptions that occur during the execution of the block.
- PL/SQL blocks can be anonymous or named. Anonymous blocks are not stored in the database and are executed once. Named blocks are stored in the database as subprograms, such as procedures, functions, triggers, or packages, and can be invoked multiple times .
- PL/SQL supports two types of dynamic SQL, which are SQL statements that are constructed and executed at run time. Dynamic SQL is useful when the SQL statement is not known in advance or depends on user input or other variables.
- Execute Immediate: This is a simple way of executing a single dynamic SQL statement, such as INSERT, UPDATE, DELETE, or CREATE. The syntax is:

```sql
EXECUTE IMMEDIATE dynamic_string [INTO {define_variable | record}] [USING [IN | OUT | IN OUT] bind_argument]...
```

- DBMS_SQL: This is a package that provides more control and flexibility over executing dynamic SQL statements, such as SELECT, that return multiple rows or columns. The process of using DBMS_SQL involves the following steps:

  - Open a cursor: A cursor is a pointer to a memory area that holds the result set of a SQL statement. The syntax is:

  ```sql
  cursor_variable := DBMS_SQL.OPEN_CURSOR;
  ```

  - Parse the SQL statement: This step checks the syntax and validity of the SQL statement and associates it with the cursor. The syntax is:

  ```sql
  DBMS_SQL.PARSE(cursor_variable, dynamic_string, DBMS_SQL.NATIVE);
  ```

  - Bind the variables: This step binds the values of the variables to the placeholders in the SQL statement. The syntax is:

  ```sql
  DBMS_SQL.BIND_VARIABLE(cursor_variable, placeholder, bind_variable);
  ```

  - Execute the SQL statement: This step executes the SQL statement and stores the result set in the cursor. The syntax is:

  ```sql
  rows_processed := DBMS_SQL.EXECUTE(cursor_variable);
  ```

  - Fetch the result set: This step retrieves the rows and columns from the cursor and assigns them to the variables. The syntax is:

  ```sql
  DBMS_SQL.DEFINE_COLUMN(cursor_variable, column_position, define_variable);
  DBMS_SQL.FETCH_ROWS(cursor_variable);
  DBMS_SQL.COLUMN_VALUE(cursor_variable, column_position, define_variable);
  ```

  - Close the cursor: This step releases the memory and resources associated with the cursor. The syntax is:

  ```sql
  DBMS_SQL.CLOSE_CURSOR(cursor_variable);
  ```