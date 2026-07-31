## Unit 7 - Creating packages and triggers

- A package is a collection of related procedures, functions, variables, constants, cursors, and exceptions that are stored together in the database.
- A package has two parts: a specification and a body. The specification declares the public elements of the package that can be referenced by other programs. The body defines the implementation of the package elements and can also contain private elements that are not visible outside the package.
- A package can provide modularity, reusability, encapsulation, and performance benefits for PL/SQL programs.
- A trigger is a special type of stored procedure that is executed automatically when a specific event occurs in the database, such as inserting, updating, or deleting a row in a table.
- A trigger can be used to enforce business rules, maintain data integrity, audit data changes, or perform complex calculations.
- A trigger has three main components: a triggering event, a trigger restriction, and a trigger action. The triggering event specifies when the trigger should fire, the trigger restriction specifies an optional condition that must be true for the trigger to fire, and the trigger action specifies the PL/SQL code that should be executed when the trigger fires.
- A trigger can be classified by its timing (before or after the triggering event), by its level (row or statement), or by its type (DML, DDL, or database).
- A trigger can access the old and new values of the affected row using the :OLD and :NEW pseudorecords. A trigger can also access the number of affected rows using the SQL%ROWCOUNT attribute.