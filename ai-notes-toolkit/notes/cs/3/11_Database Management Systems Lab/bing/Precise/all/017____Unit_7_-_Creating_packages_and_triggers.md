## Unit 7 - Creating packages and triggers

A package is a schema object that groups logically related PL/SQL types, variables, and subprograms. Packages usually have two parts, a specification and a body, although sometimes the body is unnecessary. The specification is the interface to the package. It declares the types, variables, constants, exceptions, cursors, and subprograms that can be referenced from outside the package. The body defines the queries for the cursors and the code for the subprograms.

A trigger is a named PL/SQL unit that is stored in the database and fired (executed) in response to a specified event. The event can be any of the following:

- A database manipulation (DML) statement (DELETE, INSERT, or UPDATE)
- A database definition (DDL) statement (CREATE, ALTER, or DROP)
- A database operation (SERVERERROR, LOGON, LOGOFF, STARTUP, or SHUTDOWN)

Triggers can be created on tables, views, and schemas. They can be used to enforce referential integrity, to audit data modifications, to maintain derived column values, and to maintain replication environments.

Here are some key points to remember when creating packages and triggers:

1. Packages allow you to encapsulate related types, variables, and subprograms into a single unit.
2. Triggers are fired in response to a specified event and can be used for a variety of purposes.
3. It is important to carefully plan and test your triggers to ensure that they function as intended.
4. Triggers can have unintended consequences if not used properly, so it is important to use them judiciously.