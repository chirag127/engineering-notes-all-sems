#### Joins and subqueries in Hive

- Joins are used to combine data from two or more tables based on a common column or condition.
- Subqueries are used to create temporary tables that can be used in the main query or in another subquery.
- Hive supports different types of joins, such as inner join, left outer join, right outer join, full outer join, cross join, and semi join.
- Hive supports subqueries only in the FROM clause, and the subquery has to be given a name or alias.
- Hive supports arbitrary levels of subqueries, and the subquery can also be a query expression with UNION.
- Joins and subqueries can be used together to perform complex queries on Hive tables.

Some examples of joins and subqueries in Hive are:

- Inner join: This join returns the records that are common to both tables based on the join condition.

```sql
SELECT a.col1, b.col2 FROM table1 a JOIN table2 b ON a.id = b.id;
```

- Left outer join: This join returns all the records from the left table and the matching records from the right table. If there is no match, the right side will be null.

```sql
SELECT a.col1, b.col2 FROM table1 a LEFT OUTER JOIN table2 b ON a.id = b.id;
```

- Right outer join: This join returns all the records from the right table and the matching records from the left table. If there is no match, the left side will be null.

```sql
SELECT a.col1, b.col2 FROM table1 a RIGHT OUTER JOIN table2 b ON a.id = b.id;
```

- Full outer join: This join returns all the records from both tables, and fills the null values with the corresponding values from the other table if there is a match.

```sql
SELECT a.col1, b.col2 FROM table1 a FULL OUTER JOIN table2 b ON a.id = b.id;
```

- Cross join: This join returns the Cartesian product of the two tables, i.e., every row from the left table is paired with every row from the right table.

```sql
SELECT a.col1, b.col2 FROM table1 a CROSS JOIN table2 b;
```

- Semi join: This join returns the records from the left table that have a match in the right table, but does not return any columns from the right table.

```sql
SELECT a.col1 FROM table1 a WHERE a.id IN (SELECT b.id FROM table2 b);
```

- Subquery: This query creates a temporary table that can be used in the main query or in another subquery.

```sql
SELECT col1, col2 FROM (SELECT * FROM table1 WHERE col3 > 10) t;
```

- Subquery with UNION: This query combines the results of two or more subqueries using the UNION operator.

```sql
SELECT col1, col2 FROM (SELECT * FROM table1 WHERE col3 > 10 UNION SELECT * FROM table2 WHERE col4 < 20) t;
```

- Join with subquery: This query joins a table with a subquery using a common column or condition.

```sql
SELECT a.col1, b.col2 FROM table1 a JOIN (SELECT * FROM table2 WHERE col3 > 10) b ON a.id = b.id;
```