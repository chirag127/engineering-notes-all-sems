### SQL within PL/SQL

- SQL stands for Structured Query Language, which is a standard language for accessing and manipulating data in relational databases.
- PL/SQL stands for Procedural Language/Structured Query Language, which is an extension of SQL that allows developers to write procedural code using SQL statements within its syntax .
- PL/SQL programs are composed of blocks, which are the basic units of execution. A block can contain declarations, executable statements, and exception handlers .
- PL/SQL blocks can be nested within each other, creating subprograms, functions, procedures, triggers, and packages .
- PL/SQL blocks can be compiled by the Oracle Database server and stored inside the database, or they can be executed dynamically using the EXECUTE IMMEDIATE statement or the DBMS_SQL package .
- PL/SQL blocks can interact with SQL statements in two ways: static SQL and dynamic SQL.
  - Static SQL is when the SQL statements are known at compile time and embedded within the PL/SQL block. Static SQL can use bind variables, which are placeholders for values that are supplied at run time.
  - Dynamic SQL is when the SQL statements are constructed at run time and executed using the EXECUTE IMMEDIATE statement or the DBMS_SQL package. Dynamic SQL can execute any SQL statement, including DDL (Data Definition Language) and DCL (Data Control Language) statements.
- PL/SQL blocks can also use cursor variables, which are pointers to result sets of SQL queries. Cursor variables can be passed as parameters to subprograms, allowing for modular and reusable code.
- PL/SQL blocks can output the results of SQL queries using the DBMS_OUTPUT package, which provides procedures for printing messages to the standard output device or a buffer. Alternatively, PL/SQL blocks can return the results of SQL queries using the PIPE ROW statement, which sends a row of data to a pipelined table function.