### Database Triggers

- A database trigger is a special stored procedure that is run when specific actions occur within a database.
- Most triggers are defined to run when changes are made to a table’s data. Triggers can be defined to run instead of or after DML (Data Manipulation Language) actions such as INSERT, UPDATE, and DELETE.
- A database trigger is procedural code that is automatically executed in response to certain events on a particular table or view in a database.
- The trigger is mostly used for maintaining the integrity of the information on the database.
- Database triggers are defined on a table, stored in the associated database, and executed as a result of an INSERT, UPDATE, or DELETE statement being issued against a table, no matter which user or application issues the statement.
- Database triggers can be used to implement complex data interactions, such as auditing, logging, validation, or synchronization.
- SQL Server lets you create multiple triggers for each DML, DDL, or LOGON event. For example, if you have two DML triggers for a table, both will fire when an INSERT, UPDATE, or DELETE statement is issued against the table.
- DDL triggers are a special kind of trigger that fire in response to Data Definition Language (DDL) statements. They can be used to perform administrative tasks, such as auditing and regulating database operations.