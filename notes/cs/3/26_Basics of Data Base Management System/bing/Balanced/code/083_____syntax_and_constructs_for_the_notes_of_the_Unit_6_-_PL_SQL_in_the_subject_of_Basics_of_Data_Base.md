# PL/SQL Syntax and Constructs

PL/SQL is a procedural extension of SQL that allows you to write complex and modular programs that interact with Oracle databases. PL/SQL programs are composed of blocks, which are the basic units of execution. A block can contain declarations, executable statements, and exception handlers. A block can also be nested inside another block, forming a hierarchical structure.

## PL/SQL Block Structure

The general syntax of a PL/SQL block is as follows:

```
DECLARE
  -- optional section for declaring variables, constants, cursors, exceptions, etc.
BEGIN
  -- mandatory section for executable statements
  -- at least one statement is required
EXCEPTION
  -- optional section for handling errors and exceptions
END;
-- mandatory terminator
/
-- optional symbol to execute the block
```

The DECLARE section is where you can declare identifiers such as variables, constants, cursors, exceptions, etc. that are local to the block. You can also initialize them with values or expressions. The declarations must follow the rules of PL/SQL identifiers, which are:

- They must begin with a letter.
- They can contain letters, digits, underscores, dollar signs, and number signs.
- They cannot exceed 30 characters in length.
- They cannot be reserved words or keywords.

The BEGIN section is where you can write executable statements that perform actions such as assigning values, calling procedures, looping, branching, etc. You must have at least one executable statement in this section. The statements must end with a semicolon (;).

The EXCEPTION section is where you can handle errors and exceptions that may occur during the execution of the block. You can use predefined or user-defined exceptions, and specify the actions to take when they are raised. You can also use the SQLCODE and SQLERRM functions to get the error code and message of the last exception.

The END keyword marks the end of the block. It must be followed by a semicolon (;). Optionally, you can also add a label to the END keyword to match the label of the block, if any.

The / symbol is used to execute the block in SQL*Plus or SQL Developer. It is not part of the PL/SQL syntax, but a command of the interactive tool. You can also use the EXECUTE or EXEC command to run a block.

## PL/SQL Block Types

There are three types of PL/SQL blocks: anonymous, subprogram, and trigger.

- An anonymous block is a block that has no name and is not stored in the database. It is used for one-time execution of a PL/SQL code. You can write an anonymous block in SQL*Plus or SQL Developer, or embed it in a host language such as Java or C#.
- A subprogram is a named block that is stored in the database and can be invoked repeatedly. There are two types of subprograms: procedures and functions. A procedure is a subprogram that performs a specific action, and may or may not return a value. A function is a subprogram that always returns a single value, and can be used in SQL statements or expressions.
- A trigger is a named block that is stored in the database and is executed automatically when a certain event occurs on a table or view. A trigger can be used to enforce business rules, audit changes, or perform other actions related to the data manipulation.

## PL/SQL Language Elements

PL/SQL supports many language elements that are common to other procedural languages, such as:

- Data types: PL/SQL supports scalar, composite, reference, and large object (LOB) data types. Scalar data types include numeric, character, boolean, date, and interval types. Composite data types include record, collection, and table types. Reference data types include cursor and REF CURSOR types. LOB data types include BLOB, CLOB, NCLOB, and BFILE types.
- Operators: PL/SQL supports arithmetic, relational, logical, bitwise, and string operators. You can use operators to manipulate values and expressions in PL/SQL statements.
- Expressions: PL/SQL supports various types of expressions, such as arithmetic, boolean, character, date, and null expressions. You can use expressions to assign values, compare values, or perform calculations in PL/SQL statements.
- Control structures: PL/SQL supports conditional, iterative, and sequential control structures. You can use control structures to control the flow of execution in PL/SQL blocks. Conditional control structures include IF-THEN-ELSE, CASE, and NULL statements. Iterative control structures include LOOP, WHILE, FOR, and EXIT statements. Sequential control structures include GOTO and NULL statements