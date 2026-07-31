### Triggers

- A trigger is a special kind of stored procedure that is executed automatically when a certain event occurs on a table or view in a database.
- A trigger can be used to enforce integrity constraints, audit data changes, implement business rules, or perform other actions based on the data modification.
- A trigger has three main components: a triggering event, a trigger condition, and a trigger action.
- A triggering event is the type of operation that causes the trigger to fire, such as insert, update, or delete.
- A trigger condition is an optional Boolean expression that determines whether the trigger action should be executed or not, based on the data values before and after the triggering event.
- A trigger action is a sequence of SQL statements that are executed when the trigger fires and the trigger condition is true.
- A trigger can be defined as either row-level or statement-level, depending on whether it fires once for each affected row or once for the entire statement.
- A trigger can also be defined as either before or after, depending on whether it fires before or after the triggering event.
- A trigger can be created, altered, dropped, enabled, or disabled using the SQL commands CREATE TRIGGER, ALTER TRIGGER, DROP TRIGGER, ENABLE TRIGGER, or DISABLE TRIGGER, respectively.
- A trigger can be queried using the data dictionary views, such as USER_TRIGGERS, ALL_TRIGGERS, or DBA_TRIGGERS, depending on the level of access.