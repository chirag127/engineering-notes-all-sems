 Here are the points on Database Triggers for the notes of Unit 6 - PL/SQL in the subject of Basics of Data Base Management System:

1. Triggers are special types of stored procedures that get executed automatically when an event (e.g. insert, update or delete) occurs on a table.
2. Triggers are used to maintain the integrity of the data in the database. They can be used to perform certain actions before or after a data modification.
3. Triggers can be row level or statement level. Row level triggers are executed once for each row that is affected by the event. Statement level triggers are executed only once for the triggering statement.
4. Triggers can be created for Insert, Update, Delete or all these events. They can be used to perform additional actions when data is inserted, updated or deleted from a table.
5. Example uses of triggers:
- Log changes made to a table
- Prevent invalid data from being inserted into a table
- Automate data modifications (e.g. calculate totals or audit trail)
- Cascade delete or update related data from child table

```
-- Example: Trigger to log all inserts into a table
CREATE TRIGGER log_inserts
AFTER INSERT ON products
FOR EACH ROW
BEGIN
    INSERT INTO product_log (product_id, event_date)
    VALUES (new.product_id, sysdate);
END;
```

Advantages:
- Maintain data integrity and consistency
- Automate tasks
- Enforce complex business rules

Disadvantages:
- May affect performance if many triggers are defined or if they are complex
- Difficult to understand, debug and maintain triggers
- May cause triggers to fire recursively if not written properly

[Diagrams and additional details can be added here if required]