### Database Triggers

- A database trigger is a special stored procedure that is run when specific actions occur within a database.
- Most triggers are defined to run when changes are made to a table’s data.
- Triggers can be defined to run instead of or after DML (Data Manipulation Language) actions such as INSERT, UPDATE, and DELETE.
- Triggers can also be defined to run in response to DDL (Data Definition Language) actions such as CREATE, ALTER, and DROP  .
- Triggers can be used to implement complex data interactions, maintain the integrity of the information on the database, enforce business rules, audit data changes, and perform other tasks  .
- Triggers are defined on a table, stored in the associated database, and executed as a result of an event on that table or view.
- Triggers can be recursive, meaning that they can invoke themselves or other triggers, and nested, meaning that they can be called by other triggers.
- Triggers can be disabled or enabled, and their order of execution can be specified.
- Triggers can return results to the calling application or user, but this feature will be removed in a future version of SQL Server.
- Triggers can be created in the master database and behave just like those created in user-designed databases.
- Triggers can be queried by using the sys.triggers catalog view.