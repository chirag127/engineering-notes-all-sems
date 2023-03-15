### Database Triggers

- A database trigger is a special stored procedure that is run when specific actions occur within a database.
- Most triggers are defined to run when changes are made to a table’s data.
- Triggers can be defined to run instead of or after DML (Data Manipulation Language) actions such as INSERT, UPDATE, and DELETE.
- Triggers can also be defined to run in response to DDL (Data Definition Language) actions such as CREATE, ALTER, and DROP  .
- Triggers can be used to implement complex data interactions, maintain the integrity of the information on the database, enforce business rules, audit data changes, and perform custom actions   .
- Triggers are defined on a table, stored in the associated database, and executed as a result of an event on that table or view .
- Triggers can be written in SQL or PL/SQL, depending on the database system .
- Triggers can be classified into different types based on the timing and scope of their execution  :
  - Row-level triggers: These triggers are executed for each row that is affected by the triggering event.
  - Statement-level triggers: These triggers are executed once for the whole statement that causes the triggering event.
  - Before triggers: These triggers are executed before the triggering event occurs.
  - After triggers: These triggers are executed after the triggering event occurs.
  - Instead of triggers: These triggers are executed instead of the triggering event, and can be used to override the default behavior of the event.
  - DML triggers: These triggers are executed in response to DML actions such as INSERT, UPDATE, and DELETE.
  - DDL triggers: These triggers are executed in response to DDL actions such as CREATE, ALTER, and DROP.
  - Logon triggers: These triggers are executed when a user session is established with the database.