### Syntax and Constructs for the Notes of the Unit 6 - PL/SQL in the Subject of Basics of Data Base Management System

- PL/SQL stands for Procedural Language/Structured Query Language. It is an extension of SQL that adds procedural features to the relational database language .
- PL/SQL is designed to work with Oracle Database, and allows users to create applications that manipulate data, handle errors, and perform complex calculations.
- PL/SQL is a block-structured language, which means that the basic unit of PL/SQL code is a block. A block consists of three sections: declaration, execution, and exception .
- The declaration section is optional and contains the definitions of constants, variables, cursors, exceptions, and other identifiers that can be used in the block .
- The execution section is mandatory and contains the executable statements that perform the logic of the block. At least one executable statement is required in this section .
- The exception section is optional and contains the handlers that deal with the errors or exceptions that may occur during the execution of the block .
- The end of the block is marked by the keyword END, followed by an optional block label and a semicolon. The block can be executed as a whole by using a slash (/) or the keyword EXECUTE .
- The syntax of a PL/SQL block is as follows:

```
[<<block_label>>]
DECLARE
   -- optional declarations
BEGIN
   -- mandatory executable statements
EXCEPTION
   -- optional exception handlers
END [block_label];
/
```

- PL/SQL blocks can be nested within each other, meaning that a block can contain another block as a part of its execution section. The inner block can access the identifiers declared in the outer block, but not vice versa .
- PL/SQL supports many constructs that are common in procedural languages, such as variables, constants, data types, operators, expressions, assignments, control structures, loops, cursors, subprograms, packages, triggers, and object types  .
- PL/SQL also integrates with SQL, allowing users to embed SQL statements within PL/SQL blocks, and use PL/SQL variables and expressions in SQL statements  .
- PL/SQL is a powerful and flexible language that can be used to create complex and robust applications that work with Oracle Database. It is also a highly structured and readable language that expresses the intent of the code clearly .