 Here are the notes in markdown format without any emojis or external links and in a formal tone:

### Triggers for the notes of the Unit 2 - Relational data Model and Language in the subject of Database Management System

1. Triggers are special types of stored procedures that get executed automatically when an INSERT, UPDATE or DELETE operation is performed on a table.
2. Triggers are useful to enforce business rules, auditing, data integrity, etc.
3. Syntax:
CREATE TRIGGER trigger_name
{BEFORE|AFTER} {INSERT|UPDATE|DELETE}
ON table_name
FOR EACH ROW
BEGIN
--sql_statement;
END;

4. Example:
CREATE TRIGGER tr_employee
AFTER INSERT ON employee
FOR EACH ROW
BEGIN
    INSERT INTO employee_audit
        (emp_name, action_time)
    VALUES
        (new.name, current_timestamp);
END;

5. The new keyword refers to the new data of the inserted/updated row and the old keyword refers to the original data of the updated/deleted row.
6. Triggers can be disabled using ALTER TRIGGER statement and can be dropped using DROP TRIGGER statement.

The content summarizes the key points about triggers in a formal tone with points and without any emojis or external links as requested. Please let me know if you would like me to modify or expand the content in any way.