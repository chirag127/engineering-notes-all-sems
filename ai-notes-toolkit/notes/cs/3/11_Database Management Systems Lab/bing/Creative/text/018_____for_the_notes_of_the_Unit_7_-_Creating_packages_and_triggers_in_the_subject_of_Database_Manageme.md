### Unit 7 - Creating packages and triggers in the subject of Database Management Systems Lab

- A **package** is a collection of related procedures, functions, variables, constants, and other objects that are grouped together under a common name and stored in the database.
- A **trigger** is a special kind of stored procedure that automatically executes when an event occurs in the database server, such as a data manipulation language (DML) statement or a data definition language (DDL) statement.
- The benefits of using packages and triggers are:
  - They can improve the performance, modularity, reusability, and maintainability of the database applications.
  - They can enforce business rules, data integrity, security, and auditing policies on the database level.
  - They can provide event-driven programming and custom actions for complex scenarios.
- The syntax for creating a package is:

  ```sql
  CREATE [OR REPLACE] PACKAGE package_name AS
  -- package specification
  [variable declarations]
  [constant declarations]
  [type declarations]
  [cursor declarations]
  [procedure declarations]
  [function declarations]
  END package_name;
  ```

  - The package specification defines the public interface of the package, which consists of the declarations of the variables, constants, types, cursors, procedures, and functions that can be accessed by other programs.
  - The package body, which is optional, contains the implementation of the procedures and functions declared in the package specification. The syntax for creating a package body is:

  ```sql
  CREATE [OR REPLACE] PACKAGE BODY package_name AS
  -- package body
  [variable declarations]
  [constant declarations]
  [type declarations]
  [cursor declarations]
  [procedure definitions]
  [function definitions]
  [exception handlers]
  END package_name;
  ```

- The syntax for creating a trigger is:

  ```sql
  CREATE [OR REPLACE] TRIGGER trigger_name
  [BEFORE | AFTER] event
  ON table_name
  [FOR EACH ROW]
  [WHEN condition]
  BEGIN
  -- trigger body
  [SQL statements]
  [PL/SQL statements]
  END;
  ```

  - The trigger name is a unique identifier for the trigger.
  - The event specifies when the trigger should fire, such as before or after an insert, update, delete, or truncate statement on a table or a view.
  - The table name specifies the name of the table or view that the trigger is associated with.
  - The optional FOR EACH ROW clause indicates that the trigger should fire for each row that is affected by the triggering event, rather than once for the entire statement.
  - The optional WHEN condition specifies a Boolean expression that must be true for the trigger to fire.
  - The trigger body contains the SQL and PL/SQL statements that define the actions of the trigger.