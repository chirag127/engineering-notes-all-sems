# SQL within PL/SQL

- SQL stands for Structured Query Language, which is a standard language for accessing and manipulating data in relational databases.
- PL/SQL stands for Procedural Language/Structured Query Language, which is an extension of SQL that allows developers to write procedural code using SQL statements within its syntax.
- PL/SQL program units are compiled by the Oracle Database server and stored inside the database. And at run-time, both PL/SQL and SQL run within the same server process, bringing optimal efficiency.
- PL/SQL offers a set of procedural commands (IF statements, loops, assignments), organized within blocks, that complement and extend the reach of SQL.
- A PL/SQL block is a basic unit of PL/SQL code that consists of three sections: declaration, executable, and exception-handling. A block can be nested inside another block, creating a hierarchical structure of code.
- PL/SQL supports two types of SQL statements: static and dynamic. Static SQL statements are known at compile time and can be embedded directly in the PL/SQL code. Dynamic SQL statements are constructed at run time and can be executed using the EXECUTE IMMEDIATE statement or the DBMS_SQL package.
- The EXECUTE IMMEDIATE statement allows you to execute a single SQL statement that is stored in a character string variable or a string literal. The syntax is:

```sql
EXECUTE IMMEDIATE dynamic_string
[INTO {define_variable[, define_variable]... | record}]
[USING [IN | OUT | IN OUT] bind_argument
[, [IN | OUT | IN OUT] bind_argument]...];
```

- The DBMS_SQL package allows you to execute multiple SQL statements that are stored in a cursor variable. The process of creating and executing the dynamic SQL using the DBMS_SQL package involves the following steps:

  - OPEN CURSOR: The dynamic SQL will execute in the same way as a cursor.
  - PARSE: The SQL statement is parsed and associated with the cursor.
  - BIND_VARIABLE: The bind variables are associated with the placeholders in the SQL statement.
  - DEFINE_COLUMN: The output columns are defined and associated with the variables.
  - EXECUTE: The SQL statement is executed.
  - FETCH_ROWS: The result set is fetched row by row.
  - CLOSE_CURSOR: The cursor is closed and released.

- The syntax for using the DBMS_SQL package is:

```sql
DECLARE
  c NUMBER; -- cursor variable
  n NUMBER; -- number of rows affected
  v VARCHAR2(20); -- output variable
BEGIN
  c := DBMS_SQL.OPEN_CURSOR; -- open cursor
  DBMS_SQL.PARSE(c, 'UPDATE emp SET sal = sal * 1.1 WHERE deptno = :x', DBMS_SQL.NATIVE); -- parse SQL statement with a bind variable :x
  DBMS_SQL.BIND_VARIABLE(c, ':x', 10); -- bind variable :x with value 10
  n := DBMS_SQL.EXECUTE(c); -- execute SQL statement and return number of rows affected
  DBMS_OUTPUT.PUT_LINE('Rows updated: ' || n); -- display number of rows affected
  DBMS_SQL.PARSE(c, 'SELECT ename FROM emp WHERE deptno = :x', DBMS_SQL.NATIVE); -- parse another SQL statement with the same bind variable :x
  DBMS_SQL.DEFINE_COLUMN(c, 1, v, 20); -- define output column 1 with variable v and size 20
  LOOP
    IF DBMS_SQL.FETCH_ROWS(c) > 0 THEN -- fetch rows until no more rows
      DBMS_SQL.COLUMN_VALUE(c, 1, v); -- get column value for column 1 into variable v
      DBMS_OUTPUT.PUT_LINE(v); -- display variable v
    ELSE
      EXIT; -- exit loop
    END IF;
  END LOOP;
  DBMS_SQL.CLOSE_CURSOR(c); -- close cursor
END;
```

- To output a SELECT statement from a PL/SQL block, you can use the DBMS_OUTPUT.PUT_LINE function to display the result on the screen. However, this requires that the server output is enabled and that the result set is small. Alternatively, you can use a cursor FOR loop or a PIPELINED function to return the result as a collection.