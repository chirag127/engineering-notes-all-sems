# Unit 7 - Creating packages and triggers in the subject of Database Management Systems Lab

## Packages

- A package is a collection of related procedures, functions, variables, constants, cursors, and other program elements that are stored together in the database.
- A package has two parts: a specification and a body.
- The specification declares the public elements of the package that are visible and accessible to other programs.
- The body defines the implementation of the package elements and can also contain private elements that are only visible within the package.
- A package can be created using the CREATE PACKAGE and CREATE PACKAGE BODY statements.
- A package can be modified using the ALTER PACKAGE statement and dropped using the DROP PACKAGE statement.
- A package can be compiled using the COMPILE PACKAGE and COMPILE PACKAGE BODY statements.
- A package element can be referenced using the dot notation: package_name.element_name.

## Triggers

- A trigger is a special type of stored procedure that is executed automatically when a specific event occurs on a table or view in the database.
- A trigger can be used to enforce business rules, audit data changes, perform complex calculations, or implement custom logic.
- A trigger can be created using the CREATE TRIGGER statement with the following syntax:

```sql
CREATE TRIGGER trigger_name [ BEFORE | AFTER] event ON table_name trigger_type
BEGIN
  -- trigger_logic
END;
```

- The trigger_name is a unique identifier for the trigger.
- The event can be one or more of the following: INSERT, UPDATE, or DELETE.
- The table_name is the name of the table or view on which the trigger is defined.
- The trigger_type can be one of the following:
  - FOR EACH ROW: The trigger is executed for each row affected by the event.
  - FOR EACH STATEMENT: The trigger is executed once for the whole statement that caused the event.
- The trigger_logic is a block of SQL or PL/SQL code that contains the logic to be executed by the trigger.
- A trigger can be modified using the ALTER TRIGGER statement and dropped using the DROP TRIGGER statement.
- A trigger can be enabled or disabled using the ENABLE TRIGGER or DISABLE TRIGGER statements.
- A trigger can be compiled using the COMPILE TRIGGER statement.