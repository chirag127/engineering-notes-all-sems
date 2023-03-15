### SQL within PL/SQL

- SQL stands for Structured Query Language, which is a standard language for accessing and manipulating data in relational databases.
- PL/SQL stands for Procedural Language/Structured Query Language, which is a procedural extension of SQL designed for Oracle Database.
- PL/SQL allows developers to embed SQL statements within its syntax, and to create and execute complex programs that interact with the database.
- PL/SQL programs are composed of blocks, which are the basic units of execution. A block can contain declarations, executable statements, and exception handlers.
- PL/SQL blocks can be nested within each other, and can be stored inside the database as procedures, functions, triggers, or packages.
- PL/SQL blocks can also be executed dynamically using the EXECUTE IMMEDIATE statement or the DBMS_SQL package, which allow the creation and execution of SQL statements at run-time.
- PL/SQL offers many advantages over SQL, such as:
  - Better performance, as PL/SQL can execute multiple SQL statements in a single round-trip to the database server, and can cache and reuse SQL cursors.
  - Better error handling, as PL/SQL can catch and handle exceptions using the RAISE, EXCEPTION_INIT, and PRAGMA EXCEPTION_INIT statements.
  - Better modularity, as PL/SQL can encapsulate business logic and data manipulation in reusable and maintainable units of code.
  - Better security, as PL/SQL can enforce access control and data validation using the AUTHID and INVOKER RIGHTS clauses.