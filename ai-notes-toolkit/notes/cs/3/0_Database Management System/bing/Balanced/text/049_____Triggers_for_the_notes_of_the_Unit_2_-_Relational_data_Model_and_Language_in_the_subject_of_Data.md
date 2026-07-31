### Triggers for the notes of the Unit 2 - Relational data Model and Language in the subject of Database Management System

- A trigger is a stored procedure that is executed automatically when a specified event occurs on a table or view in a database.
- A trigger can be used to enforce business rules, data integrity, security policies, or perform other actions such as auditing, logging, or notification.
- A trigger has three main components: a triggering event, a trigger condition, and a trigger action.
- A triggering event is the type of operation that activates the trigger, such as INSERT, UPDATE, or DELETE.
- A trigger condition is an optional Boolean expression that determines whether the trigger action should be executed or not, based on the data values or state of the database.
- A trigger action is a sequence of SQL statements or commands that are executed when the trigger is activated and the condition is satisfied.
- A trigger can be classified into two types: row-level triggers and statement-level triggers.
- A row-level trigger is executed once for each row that is affected by the triggering event, and has access to the old and new values of the row.
- A statement-level trigger is executed once for the whole statement that causes the triggering event, and does not have access to the individual rows.
- A trigger can also be classified into two types based on the timing of execution: before triggers and after triggers.
- A before trigger is executed before the triggering event takes place, and can be used to validate or modify the data before it is inserted, updated, or deleted.
- An after trigger is executed after the triggering event takes place, and can be used to perform additional actions or check the results of the operation.
- A trigger can be created, altered, or dropped using the CREATE TRIGGER, ALTER TRIGGER, or DROP TRIGGER statements in SQL.
- A trigger can be enabled or disabled using the ENABLE TRIGGER or DISABLE TRIGGER statements in SQL.
- A trigger can be viewed using the SHOW TRIGGERS statement or the INFORMATION_SCHEMA.TRIGGERS table in SQL.