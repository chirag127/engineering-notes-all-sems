### Update and Delete Operations

- Update and delete operations are used to modify or remove existing data from a relational database.
- Update operations can change the values of one or more attributes for a set of tuples that satisfy a given condition.
- Delete operations can remove one or more tuples that satisfy a given condition from a relation.
- Both update and delete operations can affect the integrity and consistency of the database, so they must be performed with care and respect the constraints and dependencies that exist among the relations.
- The syntax for update and delete operations in SQL is as follows:

```sql
-- Update operation
UPDATE <relation>
SET <attribute> = <expression>, ...
WHERE <condition>;

-- Delete operation
DELETE FROM <relation>
WHERE <condition>;
```

- The `<relation>` is the name of the relation to be modified or deleted from.
- The `<attribute>` is the name of the attribute to be updated, and the `<expression>` is the new value to be assigned to it. Multiple attributes can be updated by separating them with commas.
- The `<condition>` is a logical expression that specifies which tuples to be updated or deleted. It can use comparison operators, logical operators, and subqueries. If the condition is omitted, all tuples in the relation will be affected.
- Some examples of update and delete operations in SQL are:

```sql
-- Update the salary of all employees who work in department 10 by 10%
UPDATE EMPLOYEE
SET SALARY = SALARY * 1.1
WHERE DNO = 10;

-- Delete all employees who have not worked on any project
DELETE FROM EMPLOYEE
WHERE SSN NOT IN (SELECT ESSN FROM WORKS_ON);
```