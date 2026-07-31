### Unit 5 - Creating Cursor

A cursor is a database object that allows us to retrieve data from a result set one row at a time. It provides us with the ability to iterate over the rows of a result set and perform some operation on each row.

#### Types of Cursors

There are two types of cursors:

1. Implicit Cursors
2. Explicit Cursors

#### Implicit Cursors

Implicit cursors are created by the database automatically whenever a SQL statement is executed. They are used to retrieve data from a single row or a single value only.

#### Explicit Cursors

Explicit cursors are created by the user in a PL/SQL block. They provide more control over the retrieval of data, allowing us to fetch multiple rows at once and to specify the order in which the rows are retrieved.

#### Creating a Cursor

To create a cursor, we first need to declare a cursor variable using the `CURSOR` keyword. We then need to associate the cursor variable with a SQL statement using the `SELECT` statement. Finally, we need to open the cursor using the `OPEN` statement.

Here is an example of how to create a cursor:

```sql
DECLARE
  cursor_name CURSOR IS
    SELECT column1, column2, ...
    FROM table_name
    WHERE condition;

  variable1 datatype;
  variable2 datatype;
  ...
BEGIN
  OPEN cursor_name;
  LOOP
    FETCH cursor_name INTO variable1, variable2, ...;
    EXIT WHEN cursor_name%NOTFOUND;
    -- do something with the retrieved data
  END LOOP;
  CLOSE cursor_name;
END;
```

#### Fetching Data with a Cursor

To retrieve data from a cursor, we use the `FETCH` statement. This statement retrieves the next row from the result set and stores the values in the variables specified in the `INTO` clause.

Here is an example of how to fetch data from a cursor:

```sql
FETCH cursor_name INTO variable1, variable2, ...;
```

#### Closing a Cursor

Once we have finished using a cursor, we need to close it using the `CLOSE` statement. This frees up any resources that were used by the cursor.

Here is an example of how to close a cursor:

```sql
CLOSE cursor_name;
```

Overall, cursors are a powerful tool for working with result sets in a database. They allow us to iterate over the rows of a result set and perform some operation on each row. By using explicit cursors, we have more control over the retrieval of data, allowing us to fetch multiple rows at once and to specify the order in which the rows are retrieved.