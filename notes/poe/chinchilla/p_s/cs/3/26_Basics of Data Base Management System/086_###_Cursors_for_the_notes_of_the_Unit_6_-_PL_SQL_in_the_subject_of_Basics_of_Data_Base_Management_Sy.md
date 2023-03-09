### Cursors for the notes of the Unit 6 - PL/SQL in the subject of Basics of Data Base Management System

In PL/SQL, cursors are used to process individual rows returned by a SELECT statement. Cursors are used to iterate through the result set of the query, enabling you to process each row returned by the query.

#### Types of Cursors

There are two types of cursors in PL/SQL:

1. Implicit Cursors: Implicit cursors are automatically created by the system when a SELECT, INSERT, UPDATE or DELETE statement is executed. They are automatically managed by the system and cannot be explicitly manipulated by the programmer.

2. Explicit Cursors: Explicit cursors are created by the programmer and provide more control over the processing of the query result set. They must be explicitly declared, opened, fetched and closed by the programmer.

#### Advantages of Cursors

- Cursors allow for processing of individual rows returned by a query, which is useful when you need to perform operations on a row-by-row basis.
- Cursors provide more control over the processing of the query result set than implicit cursors.
- Cursors can be used to process result sets that are too large to be stored in memory.

#### Disadvantages of Cursors

- Cursors can be slower than other methods of processing query result sets, especially when processing large result sets.
- Cursors can be more complex to use than other methods of processing query result sets.

#### Example of a Cursor

```
DECLARE
  CURSOR employee_cursor IS
    SELECT employee_id, first_name, last_name
    FROM employees;
  employee_rec employee_cursor%ROWTYPE;
BEGIN
  OPEN employee_cursor;
  LOOP
    FETCH employee_cursor INTO employee_rec;
    EXIT WHEN employee_cursor%NOTFOUND;
    DBMS_OUTPUT.PUT_LINE(employee_rec.employee_id || ' ' || employee_rec.first_name || ' ' || employee_rec.last_name);
  END LOOP;
  CLOSE employee_cursor;
END;
```

In this example, a cursor is declared that selects the employee_id, first_name and last_name columns from the employees table. The cursor is then opened, and a loop is used to fetch each row from the cursor and output the employee_id, first_name and last_name columns for each row.

#### Applications of Cursors

- Cursors are commonly used when processing result sets that are too large to be stored in memory.
- Cursors are useful when you need to perform operations on a row-by-row basis.
- Cursors can be used to iterate over result sets in a specific order, such as sorting by a particular column.