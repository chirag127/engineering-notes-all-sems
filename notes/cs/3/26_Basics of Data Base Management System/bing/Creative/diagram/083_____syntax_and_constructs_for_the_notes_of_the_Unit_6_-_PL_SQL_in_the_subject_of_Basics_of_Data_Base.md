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

The `DECLARE` section is where you can declare variables, constants, cursors, exceptions, and other identifiers that are local to the block. The `BEGIN` section is where you can write executable statements that perform actions, such as assigning values, calling procedures, looping, branching, and manipulating data. The `EXCEPTION` section is where you can handle errors that occur during the execution of the block. The `END` keyword marks the end of the block, and the `/` symbol executes the block.

Some of the important constructs in PL/SQL are:

- **Variables and constants**: These are identifiers that store values of different data types, such as numbers, strings, dates, booleans, and user-defined types. Variables can be assigned values using the `:=` operator or the `SELECT INTO` statement. Constants must be initialized with a value when they are declared and cannot be changed later. Variables and constants have a scope and a lifetime that depend on where they are declared and how they are used.
- **Cursors**: These are pointers that allow you to fetch and process data from a result set, such as a query or a table. Cursors can be implicit or explicit. Implicit cursors are automatically created and managed by PL/SQL when you execute a SQL statement that returns one or more rows. Explicit cursors are declared and controlled by the programmer using the `CURSOR`, `OPEN`, `FETCH`, `CLOSE`, and `FOR` statements. Cursors have attributes that provide information about their status, such as `%FOUND`, `%NOTFOUND`, `%ROWCOUNT`, and `%ISOPEN`.
- **Exceptions**: These are errors that occur during the execution of a PL/SQL block, such as division by zero, invalid data, or SQL errors. Exceptions can be predefined or user-defined. Predefined exceptions are already defined by PL/SQL and have names that start with `ORA-` or `PLS-`. User-defined exceptions are declared by the programmer using the `EXCEPTION` keyword and can be raised using the `RAISE` statement. Exceptions can be handled using the `EXCEPTION` section of a block, where you can write statements that perform actions, such as logging, displaying, or recovering from the error.
- **Procedures and functions**: These are subprograms that can be called from other PL/SQL blocks or programs. Procedures and functions are similar, except that functions must return a value, while procedures do not. Procedures and functions can have parameters that pass information between the caller and the callee. Parameters can be of three modes: `IN`, `OUT`, or `IN OUT`. `IN` parameters are read-only and pass values from the caller to the callee. `OUT` parameters are write-only and pass values from the callee to the caller. `IN OUT` parameters are read-write and pass values in both directions.
- **Packages**: These are collections of related procedures, functions, variables, constants, cursors, exceptions, and other identifiers that can be grouped together for modularity and reusability. Packages have two parts: the specification and the body. The specification declares the public identifiers that are visible and accessible to other programs. The body defines the private identifiers that are only used within the package and the implementation of the subprograms declared in the specification.
- **Triggers**: These are special procedures that are automatically executed when a specific event occurs on a table, view, or database. Triggers can be used to enforce business rules, audit changes, or perform actions based on the event. Triggers have three parts: the timing, the event, and the action. The timing specifies when the trigger should fire: before, after, or instead of the event. The event specifies what should cause the trigger to fire: insert, update, delete, or a combination of them. The action specifies what the trigger should do: a PL/SQL block that performs some logic.

: https://www.guru99.com/blocks