### Unit 6 - Creating Procedures and Functions in Database Management Systems Lab

#### Introduction
- A **procedure** is a named PL/SQL block that performs one or more specific tasks.
- A **function** is a named PL/SQL block that returns a value.
- Both procedures and functions are used to modularize and encapsulate operations in a database.

#### Creating Procedures
- To create a procedure, use the `CREATE PROCEDURE` statement.
- The basic syntax for creating a procedure is as follows:
```
CREATE [OR REPLACE] PROCEDURE procedure_name
[(parameter1 [mode1] datatype1,
  parameter2 [mode2] datatype2,
  ...)]
IS
  [declaration_section]
BEGIN
  executable_section
[EXCEPTION
  exception_section]
END [procedure_name];
```
- The `OR REPLACE` option allows you to modify an existing procedure.
- The `parameter` list contains the names and datatypes of the input and output parameters.
- The `mode` specifies whether the parameter is an input (`IN`), output (`OUT`), or input/output (`IN OUT`) parameter.
- The `declaration_section` is used to declare local variables and cursors.
- The `executable_section` contains the PL/SQL code that performs the desired operations.
- The `exception_section` is used to handle any exceptions that may occur during the execution of the procedure.

#### Creating Functions
- To create a function, use the `CREATE FUNCTION` statement.
- The basic syntax for creating a function is as follows:
```
CREATE [OR REPLACE] FUNCTION function_name
[(parameter1 [mode1] datatype1,
  parameter2 [mode2] datatype2,
  ...)]
RETURN datatype
IS
  [declaration_section]
BEGIN
  executable_section
[EXCEPTION
  exception_section]
END [function_name];
```
- The `OR REPLACE` option allows you to modify an existing function.
- The `parameter` list contains the names and datatypes of the input and output parameters.
- The `mode` specifies whether the parameter is an input (`IN`), output (`OUT`), or input/output (`IN OUT`) parameter.
- The `datatype` specifies the datatype of the value returned by the function.
- The `declaration_section` is used to declare local variables and cursors.
- The `executable_section` contains the PL/SQL code that performs the desired operations and returns a value.
- The `exception_section` is used to handle any exceptions that may occur during the execution of the function.

#### Conclusion
- Procedures and functions are powerful tools for modularizing and encapsulating operations in a database.
- They can be used to perform complex operations, improve code reusability, and enhance the maintainability of the database.