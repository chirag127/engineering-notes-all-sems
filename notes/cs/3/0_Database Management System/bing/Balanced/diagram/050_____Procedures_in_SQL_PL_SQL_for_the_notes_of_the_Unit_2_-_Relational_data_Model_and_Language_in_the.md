### Procedures in SQL/PL SQL

- A procedure is a named block of PL/SQL code that can be stored in the database and executed by name.
- A procedure can perform a specific task or a series of tasks, such as validating data, performing calculations, or manipulating database objects.
- A procedure can accept input parameters and return output parameters, but it cannot return a value like a function.
- A procedure can be invoked by other procedures, functions, triggers, or applications using SQL or PL/SQL.
- A procedure has a header and a body. The header contains the keyword `PROCEDURE`, the procedure name, and the parameter list. The body contains the keyword `IS` or `AS`, the declaration section, the keyword `BEGIN`, the executable section, and the keyword `END`.
- A parameter list consists of zero or more parameters, each with a name, a mode, and a data type. The mode can be `IN`, `OUT`, or `IN OUT`, indicating whether the parameter is used for input, output, or both.
- A procedure can be created using the `CREATE PROCEDURE` statement, or using a PL/SQL block with the `CREATE OR REPLACE PROCEDURE` statement.
- A procedure can be modified using the `ALTER PROCEDURE` statement, or by replacing it with a new definition using the `CREATE OR REPLACE PROCEDURE` statement.
- A procedure can be deleted using the `DROP PROCEDURE` statement.
- A procedure can be compiled using the `ALTER PROCEDURE` statement with the `COMPILE` option, or by executing it using the `EXECUTE` statement or the `EXEC` command in SQL*Plus.
- A procedure can be debugged using the `ALTER PROCEDURE` statement with the `DEBUG` option, or by using a PL/SQL debugger tool such as SQL Developer or PL/SQL Developer.
- A procedure can be documented using comments, either in the declaration section or in the executable section, using the `--` or `/* ... */` syntax.