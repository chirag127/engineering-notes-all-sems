### Syntax and Constructs for the Notes of the Unit 6 - PL/SQL

PL/SQL is a procedural extension of SQL that allows you to write complex and modular programs that interact with Oracle databases. PL/SQL programs are composed of blocks, which are the basic units of execution. A block can be nested inside another block, creating a hierarchical structure. A block has the following syntax:

```sql
DECLARE --optional
  <declarations>
BEGIN --mandatory
  <executable statements>
EXCEPTION --optional
  <exception handlers>
END; --mandatory
/
```

The `DECLARE` section is where you can declare constants, variables, cursors, exceptions, and other identifiers that are local to the block. The `BEGIN` section is where you can write executable statements that perform the logic of the block. The `EXCEPTION` section is where you can handle any errors or exceptions that may occur during the execution of the block. The `END` keyword marks the end of the block, and the `/` symbol executes the block.

Some of the main constructs of PL/SQL are :

- **Conditional statements**: These are statements that control the flow of execution based on some conditions. The most common conditional statements are `IF-THEN-ELSE`, `CASE`, and `NULLIF`.
- **Looping statements**: These are statements that repeat a set of actions until a condition is met or a limit is reached. The most common looping statements are `FOR`, `WHILE`, and `LOOP`.
- **SQL statements**: These are statements that allow you to manipulate data in the database using SQL commands. You can use `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `MERGE`, and other SQL statements in PL/SQL blocks. You can also use `EXECUTE IMMEDIATE` to execute dynamic SQL statements.
- **Cursor**: This is a pointer that allows you to fetch and process data from a result set one row at a time. You can declare explicit cursors using the `CURSOR` keyword, or use implicit cursors that are automatically created for SQL statements.
- **Exception**: This is an error or abnormal condition that interrupts the normal execution of a block. You can declare user-defined exceptions using the `EXCEPTION` keyword, or use predefined exceptions that are raised by the PL/SQL engine. You can handle exceptions using the `RAISE`, `PRAGMA EXCEPTION_INIT`, and `WHEN` keywords.
- **Subprogram**: This is a named block that can be invoked from other blocks. A subprogram can be a procedure, which performs an action, or a function, which returns a value. You can declare subprograms using the `PROCEDURE` or `FUNCTION` keywords, and invoke them using the `CALL` or `EXECUTE` keywords.
- **Package**: This is a collection of related subprograms, variables, cursors, exceptions, and other identifiers that can be stored and reused in the database. You can declare packages using the `PACKAGE` and `PACKAGE BODY` keywords, and access them using the dot notation.