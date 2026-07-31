## Unit 6 - PL/SQL

PL/SQL is a procedural extension of SQL that allows users to write complex database applications using control structures, variables, loops, and exceptions. PL/SQL stands for Procedural Language/Structured Query Language.

Some of the main features of PL/SQL are:

- It is a block-structured language that consists of a declarative section, an executable section, and an optional exception-handling section.
- It supports variables, constants, data types, operators, expressions, and assignments.
- It provides control structures such as IF-THEN-ELSE, CASE, LOOP, EXIT, CONTINUE, and GOTO.
- It allows the creation and execution of stored procedures, functions, triggers, and packages.
- It enables the use of cursors to manipulate data in a row-by-row manner.
- It supports exception handling to deal with runtime errors and user-defined errors.
- It allows the integration of SQL statements within PL/SQL blocks, and vice versa.
- It supports dynamic SQL to execute SQL statements that are constructed at runtime.
- It provides various built-in packages, functions, and procedures to perform common tasks such as input/output, string manipulation, date and time operations, etc.

The following is an example of a PL/SQL block that calculates the factorial of a given number:

```sql
DECLARE
  n NUMBER := 5; -- input number
  f NUMBER := 1; -- factorial result
BEGIN
  FOR i IN 1..n LOOP -- loop from 1 to n
    f := f * i; -- multiply f by i
  END LOOP;
  DBMS_OUTPUT.PUT_LINE('Factorial of ' || n || ' is ' || f); -- display the result
EXCEPTION
  WHEN OTHERS THEN -- handle any error
    DBMS_OUTPUT.PUT_LINE('Error: ' || SQLERRM); -- display the error message
END;
/
```

The output of this block is:

```
Factorial of 5 is 120
```