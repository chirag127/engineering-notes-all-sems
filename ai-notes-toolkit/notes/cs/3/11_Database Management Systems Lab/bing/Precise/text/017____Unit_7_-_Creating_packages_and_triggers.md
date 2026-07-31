## Unit 7 - Creating packages and triggers

A package is a schema object that groups logically related PL/SQL types, variables, and subprograms. Packages usually have two parts, a specification and a body, although sometimes the body is unnecessary. The specification is the interface to the package. It declares the types, variables, constants, exceptions, cursors, and subprograms that can be referenced from outside the package. The body defines the queries for the cursors and the code for the subprograms.

A trigger is a special kind of stored procedure that automatically executes when an event occurs in the database server. DML triggers execute when a user tries to modify data through a data manipulation language (DML) event. DDL triggers execute in response to a variety of data definition language (DDL) events.

Here are some key points to remember when creating packages and triggers:

1. Packages allow you to encapsulate related types, variables, and subprograms into a single unit.
2. The specification of a package declares the public items that are accessible from outside the package.
3. The body of a package defines the code for the subprograms and the queries for the cursors.
4. Triggers automatically execute in response to specific events in the database.
5. DML triggers execute when data is modified through a DML event, while DDL triggers execute in response to DDL events.
6. Triggers can be used to enforce business rules and data integrity.
