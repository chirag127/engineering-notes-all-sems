# Update and Delete Operations

- Update and delete operations are used to modify or remove existing data from a relational database.
- Update operations can change the values of one or more attributes for a set of tuples that satisfy a given condition.
- Delete operations can remove one or more tuples that satisfy a given condition from a relation.
- Both update and delete operations can affect the integrity and consistency of the database, so they must be performed carefully and with proper authorization.
- The syntax for update and delete operations in SQL is as follows:

```sql
-- Update operation
UPDATE <table_name>
SET <attribute_name> = <new_value>, ...
WHERE <condition>;

-- Delete operation
DELETE FROM <table_name>
WHERE <condition>;
```

- The condition clause specifies which tuples are affected by the operation. It can use logical operators such as AND, OR, and NOT, as well as comparison operators such as =, <, >, etc.
- The update operation can also use arithmetic expressions, functions, or subqueries to compute the new values for the attributes.
- The delete operation can also use the keyword ALL to remove all the tuples from a relation, or the keyword CASCADE to remove the tuples that reference the deleted tuples in other relations (if foreign key constraints are defined).
- Some examples of update and delete operations in SQL are:

```sql
-- Update the salary of employee with ID 101 by 10%
UPDATE employee
SET salary = salary * 1.1
WHERE emp_id = 101;

-- Delete the employee with ID 102
DELETE FROM employee
WHERE emp_id = 102;

-- Delete all the employees who work in department 10
DELETE FROM employee
WHERE dept_id = 10;

-- Delete all the departments and cascade the deletion to the employees
DELETE FROM department
CASCADE;
```