### Update and Delete Operations for the notes of the Unit 2 - Relational data Model and Language in the subject of Database Management System

- Update and delete operations are used to modify or remove existing data from a relational database.
- Update operations can change the values of one or more attributes in one or more tuples of a relation, based on a specified condition.
- Delete operations can remove one or more tuples from a relation, based on a specified condition.
- Both update and delete operations can affect the integrity and consistency of the database, so they must be performed carefully and in accordance with the defined constraints and rules.
- The syntax for update and delete operations in SQL (Structured Query Language) is as follows:

```sql
-- Update operation
UPDATE <relation_name>
SET <attribute_name> = <new_value>, ...
WHERE <condition>;

-- Delete operation
DELETE FROM <relation_name>
WHERE <condition>;
```

- The `<relation_name>` is the name of the relation to be updated or deleted from.
- The `<attribute_name>` is the name of the attribute to be updated.
- The `<new_value>` is the new value to be assigned to the attribute.
- The `<condition>` is a logical expression that specifies which tuples to be updated or deleted.
- The `WHERE` clause is optional, but if omitted, all tuples in the relation will be updated or deleted.
- The `SET` clause can update multiple attributes at once, separated by commas.
- The update and delete operations can be combined with other SQL clauses, such as `ORDER BY`, `LIMIT`, `JOIN`, etc., to perform more complex operations.

- Some examples of update and delete operations in SQL are:

```sql
-- Update the salary of all employees who work in department 10 by 10%
UPDATE employee
SET salary = salary * 1.1
WHERE dept_no = 10;

-- Delete all employees who have not worked for more than a year
DELETE FROM employee
WHERE hire_date < CURRENT_DATE - INTERVAL '1 year';

-- Update the name and phone number of the supplier with id 123
UPDATE supplier
SET name = 'ABC Inc.', phone = '555-1234'
WHERE id = 123;

-- Delete all orders that have been shipped
DELETE FROM order
WHERE status = 'shipped';
```