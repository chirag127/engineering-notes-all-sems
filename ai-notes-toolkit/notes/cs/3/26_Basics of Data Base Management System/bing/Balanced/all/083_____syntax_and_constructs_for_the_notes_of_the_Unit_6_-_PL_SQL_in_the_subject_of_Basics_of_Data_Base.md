# PL/SQL Syntax and Constructs

- PL/SQL is a procedural extension of SQL that allows you to write complex and modular programs that interact with Oracle databases .
- The basic unit of PL/SQL is a block, which consists of three sections: declaration, execution, and exception .
- The declaration section is optional and contains the definitions of constants, variables, cursors, exceptions, and other identifiers .
- The execution section is mandatory and contains the executable statements that perform the logic of the program .
- The exception section is optional and contains the handlers for the errors that may occur during the execution of the program .
- The syntax of a PL/SQL block is as follows:

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

- A PL/SQL block can be anonymous or named. An anonymous block is not stored in the database and is executed once. A named block is stored in the database and can be invoked repeatedly. A named block can be a procedure, a function, a package, or a trigger.
- PL/SQL supports many procedural constructs, such as variables, constants, data types, operators, expressions, assignments, conditional statements, loops, cursors, exceptions, subprograms, and packages  .
- PL/SQL also supports SQL statements, such as SELECT, INSERT, UPDATE, DELETE, and MERGE, which can be embedded in the execution section of a PL/SQL block .
- PL/SQL uses the compatibility collation USING_NLS_COMP for all data processed in PL/SQL expressions, which instructs collation-sensitive operators to behave in the same way as in previous Oracle Database releases.