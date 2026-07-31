## Unit 5 - Creating cursor

- A cursor is a temporary work area created in the system memory when a SQL statement is executed.
- A cursor contains information on a select statement and the rows of data accessed by it.
- A cursor can be used to manipulate data in a row-by-row manner.
- There are two types of cursors: implicit and explicit.
- An implicit cursor is automatically created by Oracle whenever a SQL statement is executed, when there is no explicit cursor for the statement.
- An explicit cursor is a cursor that is defined by the programmer in the declaration section of a PL/SQL block.
- An explicit cursor can be used to process multiple rows returned by a select statement.
- An explicit cursor has four attributes: %FOUND, %NOTFOUND, %ROWCOUNT, and %ISOPEN, which provide information about the execution of a data manipulation statement.
- To create an explicit cursor, use the following syntax:

```sql
CURSOR cursor_name IS select_statement;
```

- To open an explicit cursor, use the following syntax:

```sql
OPEN cursor_name;
```

- To fetch data from an explicit cursor, use the following syntax:

```sql
FETCH cursor_name INTO variable_list;
```

- To close an explicit cursor, use the following syntax:

```sql
CLOSE cursor_name;
```

- To loop through the rows of data returned by an explicit cursor, use a cursor FOR loop, which has the following syntax:

```sql
FOR record_name IN cursor_name LOOP
  --statements;
END LOOP;
```