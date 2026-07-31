### Unit 7 - Creating Packages and Triggers in Database Management Systems Lab

- A **package** is a schema object that groups logically related PL/SQL types, variables, and subprograms.
- Packages usually have two parts: a specification and a body.
- The **specification** is the interface to the package. It declares the types, variables, constants, exceptions, cursors, and subprograms that can be referenced from outside the package.
- The **body** defines the queries for the cursors and the code for the subprograms.
- A **trigger** is a named PL/SQL block stored in the database and executed automatically when a triggering event occurs.
- Triggers can be used to enforce business rules, to maintain derived data, to maintain referential integrity, to audit data modifications, and to replicate data.
- Triggers can be created on tables or views.
- The triggering event can be an INSERT, UPDATE, or DELETE statement on a table or view.
- Triggers can be fired before or after the triggering event, and can be row-level or statement-level.
- Triggers can be created using the CREATE TRIGGER statement.
