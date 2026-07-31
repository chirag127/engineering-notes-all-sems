# Stored Procedures in PL/SQL

- A stored procedure in PL/SQL is a named block of code that performs one or more specific tasks and can be stored in the database for reuse .
- A stored procedure can be invoked by other procedures, triggers, or applications written in Java, PHP, etc .
- A stored procedure has a header and a body .
  - The header contains the name of the procedure and the parameters passed to it .
  - The body contains the declarative, executable, and exception-handling parts of the procedure .
- A stored procedure can be created using the CREATE PROCEDURE statement .
  - The syntax is:

    ```sql
    CREATE [OR REPLACE] PROCEDURE [schema.]procedure_name
    (parameter1 [mode] datatype [DEFAULT value],
    parameter2 [mode] datatype [DEFAULT value],
    ...
    parameterN [mode] datatype [DEFAULT value])
    IS
    -- declarative part
    BEGIN
    -- executable part
    EXCEPTION
    -- exception-handling part
    END [procedure_name];
    ```

  - The mode of a parameter can be IN, OUT, or IN OUT .
    - IN: the parameter can be passed a value by the caller, but the procedure cannot modify it .
    - OUT: the parameter can be modified by the procedure and the new value can be returned to the caller .
    - IN OUT: the parameter can be both passed a value by the caller and modified by the procedure .
  - The DEFAULT value of a parameter is optional and specifies the value to be used if the caller does not provide one .
- A stored procedure can be executed using the EXECUTE or EXEC command .
  - The syntax is:

    ```sql
    EXECUTE [schema.]procedure_name(parameter1, parameter2, ..., parameterN);
    ```

  - The parameters can be passed by position or by name .
    - By position: the order of the parameters must match the order of the parameters in the procedure header .
    - By name: the name of the parameter must be preceded by a colon and followed by the value to be passed .
- A stored procedure can be dropped using the DROP PROCEDURE statement.
  - The syntax is:

    ```sql
    DROP PROCEDURE [schema.]procedure_name;
    ```