# Unit 6 - Creating procedure and functions in the subject of Database Management Systems Lab

## Introduction

- A database management system (DBMS) is a software that allows users to create, manipulate, and manage data in a structured way.
- A DBMS consists of several components, such as data, schema, data dictionary, database engine, and database access language.
- Procedures and functions are two types of database objects that can be created and stored in a DBMS to perform specific tasks on data.
- Procedures and functions are similar in that they both contain a set of SQL statements that can be executed as a unit, and they both can accept parameters and return values.
- Procedures and functions are different in that procedures are mainly used to perform actions on data, such as insert, update, delete, or select, while functions are mainly used to return a single value or a table based on some calculations or logic.

## Creating procedures

- A procedure is a named block of SQL statements that can be executed as a unit by calling its name.
- A procedure can accept input parameters and return output parameters or result sets.
- A procedure can also use local variables, conditional statements, loops, and error handling within its body.
- A procedure can be created using the CREATE PROCEDURE statement, followed by the procedure name, the parameter list, and the procedure body.
- The syntax for creating a procedure is:

```sql
CREATE PROCEDURE procedure_name
  [ ( { @parameter_name [ AS ] [ type_schema_name. ] parameter_data_type 
        [ = default ] [READONLY] } 
    [ ,...n ]
  ) ]
[ WITH <procedure_option> [ ,...n ] ]
AS
BEGIN
  -- procedure body
END
```

- The procedure name must be unique within the database and follow the naming rules for identifiers.
- The parameter list is optional and can contain zero or more parameters. Each parameter must have a name, a data type, and an optional default value or READONLY attribute. The READONLY attribute indicates that the parameter value cannot be modified within the procedure.
- The WITH clause is optional and can specify one or more options for the procedure, such as encryption, recompile, execute as, etc.
- The procedure body must begin with the AS keyword and end with the END keyword. It can contain one or more SQL statements that perform the desired actions on data.
- The procedure can be executed by using the EXECUTE or EXEC statement, followed by the procedure name and the optional parameter values. The syntax for executing a procedure is:

```sql
EXECUTE | EXEC procedure_name [ @parameter = ] value [ ,...n ] [ WITH RECOMPILE ];
```

- The parameter values can be specified by name or by position. If specified by name, the parameter name must be preceded by the @ sign and followed by an equal sign and the value. If specified by position, the values must be in the same order as the parameters in the procedure definition.
- The WITH RECOMPILE option is optional and indicates that the procedure should be recompiled before execution, which can improve performance if the data or schema has changed significantly since the last execution.

## Creating functions

- A function is a named block of SQL statements that returns a single value or a table based on some calculations or logic.
- A function can accept input parameters but cannot return output parameters or result sets.
- A function can also use local variables, conditional statements, loops, and error handling within its body, but it cannot modify data or use non-deterministic functions.
- A function can be created using the CREATE FUNCTION statement, followed by the function name, the parameter list, the return type, and the function body.
- The syntax for creating a function is:

```sql
CREATE FUNCTION function_name
  ( { @parameter_name [ AS ] [ type_schema_name. ] parameter_data_type } 
    [ ,...n ]
  )
RETURNS return_data_type
[ WITH <function_option> [ ,...n ] ]
AS
BEGIN
  -- function body
  RETURN value
END
```

- The function name must be unique within the database and follow the naming rules for identifiers.
- The parameter list is optional and can contain zero or more parameters. Each parameter must have a name, a data type, and an optional AS keyword.
- The RETURNS clause is mandatory and specifies the data type of the return value. The return data type can be a scalar value or a table.
- The WITH clause is optional and can specify one or more options for the function, such as encryption, schema binding, etc.
- The function body must