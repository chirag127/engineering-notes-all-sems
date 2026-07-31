## Unit 5 - Creating cursor

- A cursor is a temporary work area created in the system memory when a SQL statement is executed.
- A cursor contains information on a select statement and the rows of data accessed by it.
- A cursor can be used to retrieve one or more rows of data and perform operations on them.
- A cursor can be either implicit or explicit.
- An implicit cursor is automatically created by Oracle whenever a SQL statement is executed, when there is no explicit cursor for the statement.
- An explicit cursor is created by the programmer to gain more control over the query execution and result processing.
- An explicit cursor can be declared, opened, fetched, and closed using PL/SQL statements.
- An explicit cursor declaration has the following syntax:

```sql
CURSOR cursor_name IS select_statement;
```

- An explicit cursor opening has the following syntax:

```sql
OPEN cursor_name;
```

- An explicit cursor fetching has the following syntax:

```sql
FETCH cursor_name INTO variable_list;
```

- An explicit cursor closing has the following syntax:

```sql
CLOSE cursor_name;
```

- An explicit cursor can also have parameters that can be used to pass values to the select statement.
- An explicit cursor with parameters has the following syntax:

```sql
CURSOR cursor_name (parameter_list) IS select_statement;
```

- An explicit cursor with parameters can be opened and fetched using the following syntax:

```sql
OPEN cursor_name (argument_list);
FETCH cursor_name INTO variable_list;
```

- An explicit cursor can also use the %ROWTYPE attribute to declare a record variable that can store an entire row fetched from the cursor.
- An explicit cursor with %ROWTYPE has the following syntax:

```sql
CURSOR cursor_name IS select_statement;
record_name cursor_name%ROWTYPE;
```

- An explicit cursor with %ROWTYPE can be fetched using the following syntax:

```sql
FETCH cursor_name INTO record_name;
```

- An explicit cursor can also use the %NOTFOUND, %FOUND, %ISOPEN, and %ROWCOUNT attributes to check the status and the number of rows fetched from the cursor.
- An explicit cursor with attributes has the following syntax:

```sql
IF cursor_name%NOTFOUND THEN
-- no more rows to fetch
ELSIF cursor_name%FOUND THEN
-- at least one row fetched
ELSIF cursor_name%ISOPEN THEN
-- cursor is open
ELSE
-- cursor is closed
END IF;

dbms_output.put_line('Number of rows fetched: ' || cursor_name%ROWCOUNT);
```