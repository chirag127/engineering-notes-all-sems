# Database Triggers

- A database trigger is a special stored procedure that is run when specific actions occur within a database.
- Most triggers are defined to run when changes are made to a table’s data.
- Triggers can be defined to run instead of or after DML (Data Manipulation Language) actions such as INSERT, UPDATE, and DELETE.
- Triggers can also be defined to run in response to DDL (Data Definition Language) actions such as CREATE, ALTER, and DROP.
- Triggers can be used for maintaining the integrity of the information on the database, implementing complex data interactions, auditing data changes, or enforcing business rules.
- Triggers are defined on a table, stored in the associated database, and executed as a result of an event on that table or view.
- Triggers can be created in the master database and behave just like those created in user-designed databases.
- Triggers can be recursive, meaning that they can fire themselves or other triggers, or nested, meaning that they can fire other triggers that fire them.
- Triggers can be disabled or enabled, modified or dropped, using SQL commands .
- Triggers can be queried using the sys.triggers catalog view.