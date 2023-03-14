#### Joins and Subqueries in Hive

Joins and subqueries are two ways of combining data from multiple tables in Hive. Joins allow you to relate data from two or more tables based on a common column or condition. Subqueries allow you to use the result of a query as a table in another query.

Some points to note about joins and subqueries in Hive are:

- Hive supports four types of joins: inner join, left outer join, right outer join, and full outer join.
- Hive only allows equality joins, meaning the join condition must use the equal sign (=).
- Hive does not support subqueries in the WHERE clause, but only in the FROM clause.
- Hive does not allow subqueries that return more than one row or column.
- Hive supports arbitrary levels of subqueries, meaning you can nest subqueries inside subqueries.

Here are some examples of how to use joins and subqueries in Hive:

- To perform an inner join between two tables, use the JOIN keyword and specify the join condition using the ON clause. For example, to join the tables sample_joins and sample_joins1 based on the Id column, you can write:

```sql
SELECT c.Id, c.Name, c.Age, o.Amount
FROM sample_joins c
JOIN sample_joins1 o
ON (c.Id=o.Id);
```

- To perform a left outer join between two tables, use the LEFT OUTER JOIN keyword and specify the join condition using the ON clause. For example, to join the tables sample_joins and sample_joins1 based on the Id column, and return all the rows from the left table even if there are no matches in the right table, you can write:

```sql
SELECT c.Id, c.Name, c.Age, o.Amount
FROM sample_joins c
LEFT OUTER JOIN sample_joins1 o
ON (c.Id=o.Id);
```

- To perform a right outer join between two tables, use the RIGHT OUTER JOIN keyword and specify the join condition using the ON clause. For example, to join the tables sample_joins and sample_joins1 based on the Id column, and return all the rows from the right table even if there are no matches in the left table, you can write:

```sql
SELECT c.Id, c.Name, c.Age, o.Amount
FROM sample_joins c
RIGHT OUTER JOIN sample_joins1 o
ON (c.Id=o.Id);
```

- To perform a full outer join between two tables, use the FULL OUTER JOIN keyword and specify the join condition using the ON clause. For example, to join the tables sample_joins and sample_joins1 based on the Id column, and return all the rows from both tables regardless of whether there are matches or not, you can write:

```sql
SELECT c.Id, c.Name, c.Age, o.Amount
FROM sample_joins c
FULL OUTER JOIN sample_joins1 o
ON (c.Id=o.Id);
```

- To use a subquery in the FROM clause, enclose the subquery in parentheses and give it a name using the AS keyword. For example, to use the result of a query that selects the Id and Name columns from the sample_joins table as a table named sub1, you can write:

```sql
SELECT sub1.Id, sub1.Name, o.Amount
FROM (SELECT Id, Name FROM sample_joins) AS sub1
JOIN sample_joins1 o
ON (sub1.Id=o.Id);
```

- To use a subquery that returns a single value in the SELECT clause, enclose the subquery in parentheses and use it as a column expression. For example, to use the result of a query that calculates the average amount from the sample_joins1 table as a column named avg_amount, you can write:

```sql
SELECT c.Id, c.Name, c.Age, (SELECT AVG(Amount) FROM sample_joins1) AS avg_amount
FROM sample_joins c;
```

- To use a subquery that returns a single column in the WHERE clause, enclose the subquery in parentheses and use it with the IN, NOT IN, EXISTS, or NOT EXISTS operators. For example, to use the result of a query that selects the Id column from the sample_joins1 table as a condition to filter the rows from the sample_joins table, you can write:

```sql
SELECT c.Id, c.Name, c.Age
FROM sample_joins c
WHERE c.Id IN (SELECT Id FROM sample_joins1);
```

- To use a subquery that returns a single row in the SELECT clause