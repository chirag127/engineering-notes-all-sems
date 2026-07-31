### Stored Procedures in PL/SQL

- A stored procedure in PL/SQL is a named block of code that performs one or more specific tasks and can be stored in the database catalog .
- A stored procedure can be thought of as a function or a method that can be invoked by triggers, other procedures, or applications on Java, PHP, etc .
- A stored procedure has a header and a body. The header contains the name of the procedure and the parameters passed to the procedure. The body contains the declarative, executable, and exception-handling parts of the procedure .
- A stored procedure can be created using the CREATE PROCEDURE statement, which has the following syntax :

```sql
CREATE [OR REPLACE] PROCEDURE schema.procedure_name
[(parameter1 [mode] datatype [DEFAULT value], ...)]
IS
  --declarative part
BEGIN
  --executable part
EXCEPTION
  --exception-handling part
END [procedure_name];
```

- The OR REPLACE option allows to modify an existing procedure. The schema is the optional name of the schema that the procedure belongs to. The mode can be IN, OUT, or IN OUT, which specifies the parameter passing mechanism. The DEFAULT value is the optional default value for the parameter  .
- A stored procedure can be executed using the EXECUTE or EXEC command, which has the following syntax :

```sql
EXECUTE [schema.]procedure_name[(parameter1, ...)];
```

- A stored procedure can be dropped using the DROP PROCEDURE statement, which has the following syntax:

```sql
DROP PROCEDURE [schema.]procedure_name;
```

- A stored procedure can also be dropped using SQL Developer, by right-clicking on the procedure name and choosing the Drop menu option.
- A stored procedure can have advantages such as modularity, reusability, maintainability, security, and performance .