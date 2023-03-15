Hello, I am Sydney, your AI assistant. I can help you with your study material for the topic of Triggers in the Unit 2 - Relational data Model and Language in the subject of Database Management System. Here are some points to note:

- A trigger is a special kind of stored procedure that automatically executes when an event occurs in the database server.
- Triggers can be used to enforce business rules, validate input data, audit data changes, replicate data, or perform other actions.
- Triggers can be defined on tables or views, and can be activated by insert, update, or delete operations.
- Triggers can be classified into three types: row-level triggers, statement-level triggers, and instead-of triggers.
- Row-level triggers are executed for each row that is affected by the triggering event. They can access the old and new values of the row using the pseudo-records :old and :new.
- Statement-level triggers are executed once for the whole triggering statement. They cannot access the individual row values, but they can use the pseudo-functions SQL%ROWCOUNT, SQL%FOUND, SQL%NOTFOUND, and SQL%ISOPEN to get information about the statement execution.
- Instead-of triggers are defined on views, and are executed instead of the triggering event. They can be used to perform complex actions on the underlying tables that are not possible with direct view manipulation.
- Triggers can be created using the CREATE TRIGGER statement, which has the following syntax:

```sql
CREATE [OR REPLACE] TRIGGER trigger_name
{BEFORE | AFTER | INSTEAD OF} {INSERT | UPDATE | DELETE}
[OF column_list] ON table_or_view
[FOR EACH ROW]
[WHEN condition]
DECLARE
  -- variable declarations
BEGIN
  -- trigger body
EXCEPTION
  -- exception handling
END;
```

- Triggers can be dropped using the DROP TRIGGER statement, which has the following syntax:

```sql
DROP TRIGGER trigger_name;
```

- Triggers can be enabled or disabled using the ALTER TRIGGER statement, which has the following syntax:

```sql
ALTER TRIGGER trigger_name {ENABLE | DISABLE};
```

- Triggers can be queried using the data dictionary views USER_TRIGGERS, ALL_TRIGGERS, and DBA_TRIGGERS.