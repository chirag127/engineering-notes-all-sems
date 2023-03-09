 Here is the content in markdown format for the topic ### DML in PL/SQL for the notes of the Unit 6 - PL/SQL in the subject of Basics of Data Base Management System:

### DML in PL/SQL

PL/SQL supports Data Manipulation Language (DML) statements to manipulate data in tables. Following are the commonly used DML statements in PL/SQL:

- INSERT: Inserts a new row into a table. The INSERT statement must specify the column names and their values.
- UPDATE: Updates existing rows in a table. The UPDATE statement sets new values for one or more columns of existing rows.
- DELETE: Deletes rows from a table. The DELETE statement removes rows that match a particular condition.
- MERGE: Either inserts or updates rows in a table. The MERGE statement performs an insert or update operation on a table based on some condition.

Advantages of using DML in PL/SQL:

- Increased performance: DML statements in PL/SQL are compiled and executed together, thereby increasing performance as compared to executing them separately.
- Transaction management: PL/SQL provides blocks to group one or more DML statements. If any statement fails, the entire block is rolled back to maintain database consistency.
- Error handling: PL/SQL provides exception handling to deal with errors that occur during DML operations. This makes the application more robust and fault tolerant.

Examples of DML in PL/SQL:

```
-- Insert a row
INSERT INTO employees (employee_id, name)
VALUES (1001, 'John');

-- Update a row
UPDATE employees
SET salary = salary * 1.1
WHERE employee_id = 1001;

-- Delete a row
DELETE FROM employees
WHERE employee_id = 1001;

-- Merge example
MERGE INTO employees a
USING (SELECT 1001 employee_id, 'Mark' name FROM dual) b
ON (a.employee_id = b.employee_id)
WHEN MATCHED THEN
    UPDATE SET a.name = b.name
WHEN NOT MATCHED THEN
    INSERT (employee_id, name) VALUES (b.employee_id, b.name);
```

[Detailed diagrams, examples, applications, etc can be added here if required]