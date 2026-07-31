### Procedures in SQL/PL SQL

- A procedure is a named block of PL/SQL code that can be stored in the database and executed by name.
- A procedure can perform a specific task or a set of related tasks, such as validating data, performing calculations, or manipulating database objects.
- A procedure can accept input parameters and return output parameters, but it does not return a value like a function does.
- A procedure can be invoked by other PL/SQL blocks, triggers, procedures, functions, or applications written in different languages such as Java, PHP, etc.
- A procedure can be created using the CREATE PROCEDURE statement, which has the following syntax:

```sql
CREATE [OR REPLACE] PROCEDURE procedure_name
[(parameter1 [mode] datatype [DEFAULT expr],
  parameter2 [mode] datatype [DEFAULT expr],
  ...)]
IS | AS
  [declaration_section]
BEGIN
  executable_section
[EXCEPTION
  exception_section]
END [procedure_name];
```

- The procedure name is a valid identifier that follows the naming rules of PL/SQL.
- The optional parameter list contains the names, modes, data types, and default values of the parameters. The mode can be IN, OUT, or IN OUT, indicating the direction of data flow between the procedure and the caller. The default mode is IN, which means the parameter is read-only. The OUT mode means the parameter is write-only, and the IN OUT mode means the parameter is both readable and writable.
- The IS or AS keyword separates the header and the body of the procedure.
- The optional declaration section contains the declarations of local variables, constants, cursors, and other items that are used in the procedure body.
- The mandatory executable section contains the PL/SQL statements that implement the logic of the procedure. It must have at least one executable statement, and it must end with a semicolon.
- The optional exception section handles the errors that may occur during the execution of the procedure. It contains one or more exception handlers that associate an exception name with a sequence of statements to handle it.
- The optional procedure name at the end of the block is used for readability and consistency. It must match the name at the beginning of the block.
- A procedure can be modified using the CREATE OR REPLACE PROCEDURE statement, which replaces the existing definition of the procedure with the new one.
- A procedure can be deleted using the DROP PROCEDURE statement, which removes the procedure definition and its dependencies from the database.