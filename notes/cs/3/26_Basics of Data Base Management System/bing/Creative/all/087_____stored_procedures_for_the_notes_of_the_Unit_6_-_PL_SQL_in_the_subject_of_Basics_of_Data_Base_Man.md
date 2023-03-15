# Stored Procedures in PL/SQL

- A stored procedure in PL/SQL is a named block of code that performs one or more specific tasks and can be stored in the database catalog  .
- A stored procedure can be thought of as a function or a method that can be invoked by triggers, other procedures, or applications on Java, PHP, etc  .
- A stored procedure has a header and a body   .
- The header contains the name of the procedure and the parameters passed to the procedure  .
- The body contains the declarative, executable, and exception-handling parts of the procedure .
- The syntax of a stored procedure is as follows  :

```sql
CREATE [OR REPLACE] PROCEDURE procedure_name
[(parameter_name [IN | OUT | IN OUT] type [, ...])]
IS
  [declaration_section]
BEGIN
  executable_section
[EXCEPTION
  exception_section]
END [procedure_name];
```

- The CREATE OR REPLACE option allows to modify an existing procedure .
- The parameter_name is the name of the parameter, which can be of three modes: IN, OUT, or IN OUT  .
- The IN mode is the default and indicates that the parameter is an input value that cannot be changed by the procedure  .
- The OUT mode indicates that the parameter is an output value that can be changed by the procedure and returned to the caller  .
- The IN OUT mode indicates that the parameter is both an input and an output value  .
- The type is the data type of the parameter, which can be any PL/SQL data type  .
- The declaration_section is optional and declares the variables, constants, cursors, and user-defined exceptions used in the procedure .
- The executable_section is mandatory and contains the PL/SQL statements that implement the logic of the procedure .
- The exception_section is optional and handles the errors that occur during the execution of the procedure .
- The procedure_name at the end of the block is optional and can be used to improve the readability of the code .
- To execute a stored procedure, we can use the EXECUTE or EXEC command followed by the procedure name and the arguments if any .
- To drop a stored procedure, we can use the DROP PROCEDURE command followed by the procedure name.
- Alternatively, we can use a graphical user interface such as SQL Developer to create, modify, execute, or drop a stored procedure.