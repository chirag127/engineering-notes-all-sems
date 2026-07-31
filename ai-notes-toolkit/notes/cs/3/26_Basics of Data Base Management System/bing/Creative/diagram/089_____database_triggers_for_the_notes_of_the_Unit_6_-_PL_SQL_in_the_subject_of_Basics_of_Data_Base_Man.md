### Database Triggers

- A database trigger is a special stored procedure that is run when specific actions occur within a database.
- Most triggers are defined to run when changes are made to a table’s data.
- Triggers can be defined to run instead of or after DML (Data Manipulation Language) actions such as INSERT, UPDATE, and DELETE.
- Triggers can also be defined to run in response to DDL (Data Definition Language) actions such as CREATE, ALTER, and DROP  .
- Triggers can be used to implement complex data interactions, maintain the integrity of the information on the database, enforce business rules, audit data changes, and perform custom actions   .
- Triggers are defined on a table, stored in the associated database, and executed as a result of a database event, no matter which user or application issues the statement.
- Triggers can be recursive, meaning that they can fire themselves or other triggers, and nested, meaning that they can fire in a cascading manner.
- Triggers can be disabled or enabled, and their order of execution can be specified .
- Triggers can be created using the CREATE TRIGGER statement, and modified or dropped using the ALTER TRIGGER or DROP TRIGGER statements .
- Triggers can be queried using the sys.triggers catalog view.