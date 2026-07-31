# Syntax and Constructs for the Notes of the Unit 6 - PL/SQL

PL/SQL is a procedural extension of SQL that allows you to write complex and modular programs that interact with Oracle databases. PL/SQL programs are composed of blocks, which are the basic units of execution. A block can be nested inside another block, creating a hierarchical structure. A block has the following syntax:

```sql
[DECLARE
  --optional declarations of variables, constants, cursors, exceptions, etc.
]
BEGIN
  --mandatory executable statements. At least one statement is required.
[EXCEPTION
  --optional handlers for errors or exceptions that occur during execution
]
END;
--mandatory end of the block
[/] --optional slash to execute the block
```

Some of the main constructs and features of PL/SQL are:

- **Variables and constants**: You can declare and use scalar, composite, or reference variables and constants in PL/SQL. You can also use bind variables and host variables to pass data between PL/SQL and other environments. Variables and constants have a name, a data type, and an optional initial value. You can use the `%TYPE` and `%ROWTYPE` attributes to declare variables that match the data types of existing database objects.
- **Data types**: PL/SQL supports many data types, including SQL data types (such as `NUMBER`, `VARCHAR2`, `DATE`, etc.), PL/SQL-specific data types (such as `BOOLEAN`, `PLS_INTEGER`, `BINARY_INTEGER`, etc.), user-defined data types (such as `OBJECT`, `VARRAY`, `TABLE`, etc.), and collection data types (such as `ASSOCIATIVE ARRAY`, `NESTED TABLE`, `VARRAY`, etc.).
- **Operators and expressions**: PL/SQL supports various operators and expressions to manipulate data and perform calculations. Operators include arithmetic, comparison, logical, bitwise, string, and set operators. Expressions are combinations of operators, operands, literals, and function calls that evaluate to a single value.
- **Control structures**: PL/SQL provides control structures to alter the flow of execution based on conditions, loops, or branches. Control structures include `IF-THEN-ELSE`, `CASE`, `LOOP`, `EXIT`, `CONTINUE`, `GOTO`, `NULL`, and `RETURN` statements.
- **Cursors**: A cursor is a pointer to a result set of a SQL query. PL/SQL provides two types of cursors: implicit and explicit. An implicit cursor is automatically created and managed by PL/SQL for every SQL statement that returns a single row. An explicit cursor is declared and controlled by the programmer for SQL statements that return multiple rows. You can use cursor attributes, such as `%FOUND`, `%NOTFOUND`, `%ROWCOUNT`, and `%ISOPEN`, to check the status of a cursor. You can also use cursor variables, which are pointers to cursors, to pass cursors as parameters to subprograms or to work with multiple result sets.
- **Exceptions**: An exception is an error or an abnormal condition that occurs during the execution of a PL/SQL block. PL/SQL provides predefined exceptions, such as `NO_DATA_FOUND`, `TOO_MANY_ROWS`, `ZERO_DIVIDE`, etc., that are raised automatically by the PL/SQL runtime engine. You can also define your own user-defined exceptions and raise them explicitly with the `RAISE` statement. You can handle exceptions with the `EXCEPTION` section of a block, where you can use the `WHEN` clause to specify the actions to take for each exception.
- **Subprograms**: A subprogram is a named block of code that can be invoked from other blocks of code. PL/SQL provides two types of subprograms: procedures and functions. A procedure is a subprogram that performs a specific action and can have zero or more parameters. A function is a subprogram that returns a single value and can have zero or more parameters. You can declare subprograms in the `DECLARE` section of a block, or create them as standalone objects in the database schema. You can also use packages to group related subprograms and variables into a single unit.