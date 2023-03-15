# Unit 7 - Creating packages and triggers in the subject of Database Management Systems Lab

## Packages
- A package is a collection of related procedures, functions, variables, constants, and cursors that are stored together in the database.
- A package has two parts: a specification and a body.
- The specification declares the public elements of the package, such as the procedures and functions that can be called by other programs.
- The body defines the implementation of the package, such as the code for the procedures and functions, and the private elements of the package, such as the variables and cursors that are only accessible within the package.
- Packages allow modular design, code reuse, information hiding, and performance improvement.

## Triggers
- A trigger is a special type of stored procedure that is executed automatically when a specific event occurs in the database, such as inserting, updating, or deleting data from a table.
- A trigger can perform various actions, such as enforcing business rules, auditing data changes, maintaining derived data, or sending notifications.
- A trigger has three main components: a name, a triggering event, and a trigger action.
- The name identifies the trigger and must be unique within the schema.
- The triggering event specifies when the trigger should fire, such as before or after an insert, update, or delete statement on a table or view.
- The trigger action defines the logic to execute when the trigger fires, such as a block of SQL or PL/SQL statements.
- Triggers can be classified into two types: row-level triggers and statement-level triggers.
- A row-level trigger fires once for each row affected by the triggering event, and can access the old and new values of the row using the :OLD and :NEW pseudorecords.
- A statement-level trigger fires once for the whole statement that caused the triggering event, and cannot access the individual row values.