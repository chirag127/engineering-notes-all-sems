#### Joins and Subqueries in Hive

- Joins are used to combine data from two or more tables based on a common column or condition.
- Subqueries are used to create temporary tables that can be used in the main query or join.
- Hive supports different types of joins, such as inner join, left outer join, right outer join, full outer join, and cross join.
- Hive supports subqueries only in the FROM clause (through Hive 0.12). The subquery has to be given a name because every table in a FROM clause must have a name. The columns in the subquery select list are available in the outer query just like columns of a table. The subquery can also be a query expression with UNION. Hive supports arbitrary levels of subqueries .
- An example of a join query in Hive is:

```sql
SELECT apps.acct_nbr, apps.date, c.ind, c.date
FROM applications apps
JOIN credits c
ON c.acct_nbr = apps.acct_nbr
WHERE c.ind in ('NP','0P')
AND c.date >= apps.date
ORDER BY c.date DESC;
```

- This query joins the applications and credits tables based on the acct_nbr column and filters the records based on the ind and date columns. The result is ordered by the date column in descending order.
- An example of a subquery in Hive is:

```sql
SELECT s.name, s.age, s.salary
FROM
(SELECT name, age, salary
FROM employee
WHERE age > 30) s
ORDER BY s.salary DESC;
```

- This query creates a temporary table s with the name, age, and salary columns from the employee table where the age is greater than 30. The main query selects the columns from s and orders them by the salary column in descending order .