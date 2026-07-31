# Database Triggers

- A database trigger is a special stored procedure that is run when specific actions occur within a database.
- Most triggers are defined to run when changes are made to a table’s data.
- Triggers can be defined to run instead of or after DML (Data Manipulation Language) actions such as INSERT, UPDATE, and DELETE.
- Triggers can also be defined to run in response to DDL (Data Definition Language) actions such as CREATE, ALTER, and DROP  .
- Triggers can be used for maintaining the integrity of the information on the database, implementing complex data interactions, auditing data changes, enforcing business rules, and performing custom actions.
- Triggers are defined on a table, stored in the associated database, and executed as a result of an event on that table or view.
- Triggers can be created, modified, and dropped using SQL statements  .
- Triggers can be classified into different types based on the timing and scope of their execution  :
  - Row-level triggers: These triggers are executed for each row affected by the triggering event.
  - Statement-level triggers: These triggers are executed once for the whole statement that caused the triggering event.
  - Before triggers: These triggers are executed before the triggering event occurs.
  - After triggers: These triggers are executed after the triggering event occurs.
  - Instead of triggers: These triggers are executed instead of the triggering event, and can be used to override the default behavior of the event .
  - DML triggers: These triggers are executed in response to DML actions on a table or view.
  - DDL triggers: These triggers are executed in response to DDL actions on a database or server .
  - Logon triggers: These triggers are executed in response to logon events on a server.