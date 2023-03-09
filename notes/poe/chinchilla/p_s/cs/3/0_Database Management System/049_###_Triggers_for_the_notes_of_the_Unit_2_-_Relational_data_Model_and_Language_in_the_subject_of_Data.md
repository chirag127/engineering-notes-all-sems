### Triggers for the notes of the Unit 2 - Relational data Model and Language in the subject of Database Management System

Triggers are event-driven procedures that are executed automatically in response to certain events, such as an insert, update, or delete operation on a table. They are useful in maintaining data consistency and integrity in a relational database system. In this unit, we will discuss triggers in the context of the relational data model and language.

Here are some important points to remember about triggers:

- Triggers are defined using the CREATE TRIGGER statement.
- Triggers can be executed BEFORE or AFTER the triggering event.
- Triggers can be defined to execute once for each row affected by the triggering event, or once for each statement that affects one or more rows.
- Triggers can be defined to execute on one or more tables.
- Triggers can access the old and new values of the data being modified.
- Triggers can be used to enforce complex business rules that cannot be enforced using constraints.
- Triggers can be used to audit changes to data.

Here are some advantages and disadvantages of using triggers:

Advantages:

- Triggers can be used to enforce complex business rules that cannot be enforced using constraints.
- Triggers can be used to audit changes to data.
- Triggers can be used to maintain data consistency and integrity.

Disadvantages:

- Triggers can be difficult to debug and maintain.
- Triggers can slow down database performance if they are poorly written or executed frequently.
- Triggers can be a security risk if they are not properly secured.

Here is an example of a trigger:

```sql
CREATE TRIGGER update_salary
AFTER UPDATE ON employees
FOR EACH ROW
BEGIN
    IF NEW.salary > OLD.salary THEN
        INSERT INTO salary_changes (employee_id, old_salary, new_salary, change_date)
        VALUES (OLD.employee_id, OLD.salary, NEW.salary, NOW());
    END IF;
END;
```

This trigger is executed after an update operation on the employees table. It inserts a record into the salary_changes table if the new salary is greater than the old salary.

Triggers have many applications in database management systems, including:

- Enforcing complex business rules.
- Auditing changes to data.
- Maintaining data consistency and integrity.
- Implementing cascading updates and deletes.
- Implementing referential integrity constraints.
- Implementing security policies.

In summary, triggers are event-driven procedures that are useful in maintaining data consistency and integrity in a relational database system. They can be used to enforce complex business rules, audit changes to data, and implement cascading updates and deletes. However, they can also be difficult to debug and maintain, and can slow down database performance if they are poorly written or executed frequently.