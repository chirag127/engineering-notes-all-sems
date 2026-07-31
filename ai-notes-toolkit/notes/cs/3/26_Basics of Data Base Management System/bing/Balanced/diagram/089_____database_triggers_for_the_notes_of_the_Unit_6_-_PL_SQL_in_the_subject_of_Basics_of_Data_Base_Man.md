### Database Triggers

- A database trigger is a special stored procedure that is run when specific actions occur within a database.
- Most triggers are defined to run when changes are made to a table’s data. Triggers can be defined to run instead of or after DML (Data Manipulation Language) actions such as INSERT, UPDATE, and DELETE.
- A database trigger is procedural code that is automatically executed in response to certain events on a particular table or view in a database.
- The trigger is mostly used for maintaining the integrity of the information on the database.
- Database triggers are defined on a table, stored in the associated database, and executed as a result of an INSERT, UPDATE, or DELETE statement being issued against a table, no matter which user or application issues the statement.
- Database triggers can be used to implement complex data interactions, such as auditing, logging, validation, or synchronization.
- Database triggers can be classified into two types: row-level triggers and statement-level triggers.
- Row-level triggers are executed for each row that is affected by the triggering event, while statement-level triggers are executed only once for the whole statement.
- Database triggers can also be classified into three types based on the timing of their execution: before triggers, after triggers, and instead of triggers.
- Before triggers are executed before the triggering event, after triggers are executed after the triggering event, and instead of triggers are executed in place of the triggering event.
- Database triggers can be created using the CREATE TRIGGER statement in SQL.
- The syntax of the CREATE TRIGGER statement is as follows:

```
CREATE TRIGGER [ schema_name . ]trigger_name   
ON { table | view }   
[ WITH <dml_trigger_option> [ ,...n ] ]  
{ FOR | AFTER | INSTEAD OF }   
{ [ INSERT ] [ , ] [ UPDATE ] [ , ] [ DELETE ] }   
[ WITH APPEND ]  
[ NOT FOR REPLICATION ]   
AS { sql_statement  [ ; ] [ ,...n ] | EXTERNAL NAME <method specifier [ ; ] > }  
```

- Database triggers can also be created for DDL (Data Definition Language) events, such as CREATE, ALTER, or DROP statements.
- DDL triggers can be used to perform administrative tasks, such as auditing, enforcing policies, or preventing unauthorized changes.
- DDL triggers can be created using the CREATE TRIGGER statement in SQL, with the ON clause specifying the DDL event or events to be handled.
- The syntax of the CREATE TRIGGER statement for DDL triggers is as follows:

```
CREATE TRIGGER [ schema_name . ]trigger_name   
ON { ALL SERVER | DATABASE | SCHEMA [ . ]object_name }   
[ WITH <ddl_trigger_option> [ ,...n ] ]  
{ FOR | AFTER } { event_type | event_group } [ ,...n ]   
AS { sql_statement  [ ; ] [ ,...n ] | EXTERNAL NAME <method specifier [ ; ] > }  
```

- Database triggers can be modified using the ALTER TRIGGER statement, and dropped using the DROP TRIGGER statement in SQL .
- Database triggers can be queried using the sys.triggers catalog view, which contains information such as the name, type, scope, and definition of the trigger.