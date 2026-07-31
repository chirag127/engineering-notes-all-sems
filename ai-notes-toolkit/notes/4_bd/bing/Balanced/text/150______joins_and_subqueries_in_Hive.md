#### Joins and subqueries in Hive

- Joins are used to combine data from two or more tables based on a common column or condition.
- Subqueries are queries that are nested inside another query, usually in the FROM or WHERE clause.
- Hive supports different types of joins, such as inner join, left outer join, right outer join, full outer join, and cross join.
- Hive also supports subqueries only in the FROM clause, where the subquery is treated as a table and has to be given a name or alias.
- The columns in the subquery select list are available in the outer query just like columns of a table.
- The subquery can also be a query expression with UNION, which combines the results of two or more queries.
- Hive supports arbitrary levels of subqueries, meaning that a subquery can contain another subquery inside it, and so on.
- Joins and subqueries are useful for performing complex analysis on data stored in Hive tables.

Some examples of joins and subqueries in Hive are:

- Inner join: This join returns only the records that have matching values in both tables.

```sql
SELECT a.col1, b.col2 FROM table1 a JOIN table2 b ON a.key = b.key;
```

- Left outer join: This join returns all the records from the left table, and the matched records from the right table. If there is no match, the right side will be null.

```sql
SELECT a.col1, b.col2 FROM table1 a LEFT JOIN table2 b ON a.key = b.key;
```

- Right outer join: This join returns all the records from the right table, and the matched records from the left table. If there is no match, the left side will be null.

```sql
SELECT a.col1, b.col2 FROM table1 a RIGHT JOIN table2 b ON a.key = b.key;
```

- Full outer join: This join returns all the records from both tables, and fills the null values with the corresponding values from the other table if there is a match.

```sql
SELECT a.col1, b.col2 FROM table1 a FULL JOIN table2 b ON a.key = b.key;
```

- Cross join: This join returns the Cartesian product of the two tables, meaning that every row from the first table is paired with every row from the second table.

```sql
SELECT a.col1, b.col2 FROM table1 a CROSS JOIN table2 b;
```

- Subquery in the FROM clause: This subquery acts as a table and can be joined with other tables or subqueries.

```sql
SELECT a.col1, b.col2 FROM (SELECT * FROM table1 WHERE col3 > 10) a JOIN table2 b ON a.key = b.key;
```

- Subquery with UNION: This subquery combines the results of two or more queries and can be joined with other tables or subqueries.

```sql
SELECT a.col1, b.col2 FROM (SELECT * FROM table1 UNION SELECT * FROM table3) a JOIN table2 b ON a.key = b.key;
```

- Nested subquery: This subquery contains another subquery inside it, and can be joined with other tables or subqueries.

```sql
SELECT a.col1, b.col2 FROM (SELECT * FROM table1 WHERE col3 IN (SELECT col4 FROM table4)) a JOIN table2 b ON a.key = b.key;
```