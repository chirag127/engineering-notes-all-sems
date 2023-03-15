### Joins

- A join is a relational operation that combines data from two or more tables based on a common attribute or condition.
- Joins are used to retrieve related data from multiple tables in a single query.
- There are different types of joins, such as inner join, outer join, cross join, natural join, and theta join.
- Each type of join has a different syntax and semantics, and produces a different result set.

#### Inner join

- An inner join returns only the rows that match the join condition in both tables.
- An inner join can be specified using the keyword `JOIN` or the operator `⋈`.
- An inner join can be written as:

```sql
SELECT * FROM table1 JOIN table2 ON table1.attribute = table2.attribute;
```

- Or as:

```sql
SELECT * FROM table1 ⋈ table2 WHERE table1.attribute = table2.attribute;
```

- An example of an inner join is:

```sql
SELECT * FROM employee JOIN department ON employee.dept_id = department.dept_id;
```

- This query returns the details of all employees and their corresponding departments.

#### Outer join

- An outer join returns all the rows that match the join condition in either table, and also the rows that do not match in one or both tables.
- An outer join can be specified using the keywords `LEFT JOIN`, `RIGHT JOIN`, or `FULL JOIN`.
- A left outer join returns all the rows from the left table, and the matching rows from the right table. If there is no match, the right table columns are filled with null values.
- A right outer join returns all the rows from the right table, and the matching rows from the left table. If there is no match, the left table columns are filled with null values.
- A full outer join returns all the rows from both tables, regardless of whether they match or not. If there is no match, the corresponding table columns are filled with null values.
- An outer join can be written as:

```sql
SELECT * FROM table1 LEFT JOIN table2 ON table1.attribute = table2.attribute;
```

- Or as:

```sql
SELECT * FROM table1 RIGHT JOIN table2 ON table1.attribute = table2.attribute;
```

- Or as:

```sql
SELECT * FROM table1 FULL JOIN table2 ON table1.attribute = table2.attribute;
```

- An example of an outer join is:

```sql
SELECT * FROM employee LEFT JOIN department ON employee.dept_id = department.dept_id;
```

- This query returns the details of all employees, and the corresponding departments if they exist. If an employee does not belong to any department, the department columns are null.

#### Cross join

- A cross join returns the Cartesian product of two tables, that is, every possible combination of rows from both tables.
- A cross join can be specified using the keyword `CROSS JOIN` or the operator `×`.
- A cross join can be written as:

```sql
SELECT * FROM table1 CROSS JOIN table2;
```

- Or as:

```sql
SELECT * FROM table1 × table2;
```

- An example of a cross join is:

```sql
SELECT * FROM employee CROSS JOIN department;
```

- This query returns the details of every employee paired with every department, regardless of whether they are related or not.

#### Natural join

- A natural join is a special case of an inner join that automatically matches the columns with the same name and type in both tables.
- A natural join can be specified using the keyword `NATURAL JOIN` or the operator `⋈`.
- A natural join can be written as:

```sql
SELECT * FROM table1 NATURAL JOIN table2;
```

- Or as:

```sql
SELECT * FROM table1 ⋈ table2;
```

- An example of a natural join is:

```sql
SELECT * FROM employee NATURAL JOIN department;
```

- This query returns the details of all employees and their corresponding departments, based on the common column `dept_id`.

#### Theta join

- A theta join is a generalization of an inner join that allows any comparison operator in the join condition, not just equality.
- A theta join can be specified using the operator `⋈θ`, where θ is the comparison operator.
- A theta join can be written as:

```sql
SELECT * FROM table1 ⋈θ table2 WHERE table1.attribute θ table2.attribute;
```

- An example of a theta join is:

```sql
SELECT * FROM employee ⋈< department WHERE employee.salary < department.budget;
```

- This query returns the details of all employees whose salary is less than the