# Unit 7 - Creating Packages and Triggers in Database Management Systems Lab

## Packages
- A package is a schema object that groups logically related PL/SQL types, variables, and subprograms.
- Packages usually have two parts: a specification and a body.
- The specification is the interface to the package. It declares the types, variables, constants, exceptions, cursors, and subprograms that can be referenced from outside the package.
- The body defines the queries for the cursors and the code for the subprograms.
- Packages help you organize your application development more efficiently.

## Triggers
- A trigger is a special kind of stored procedure that automatically executes when an event occurs in the database server.
- Triggers can be used to enforce business rules, validate input data, and maintain referential integrity.
- There are three types of triggers: DML triggers, DDL triggers, and logon triggers.
- DML triggers execute when a user tries to modify data through a data manipulation language (DML) event.
- DDL triggers execute in response to a variety of data definition language (DDL) events.
- Logon triggers fire when a user session is established with an instance of SQL Server.