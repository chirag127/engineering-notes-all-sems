#### Joins and Subqueries in Hive

- Joins are used to combine data from two or more tables based on a common column or condition.
- Subqueries are queries that are nested inside another query, usually in the FROM or WHERE clause.
- Hive supports different types of joins, such as inner join, left outer join, right outer join, full outer join, and cross join.
- Hive also supports different types of subqueries, such as scalar subquery, IN subquery, EXISTS subquery, and correlated subquery.
- Joins and subqueries can be used together to perform complex queries on Hive tables.

Some examples of joins and subqueries in Hive are:

- Inner join: This join returns the records that are common to both tables based on the join condition.

```sql
SELECT a.col1, b.col2 FROM table1 a JOIN table2 b ON a.id = b.id;
```

- Left outer join: This join returns all the records from the left table and the matching records from the right table. If there is no match, the right table columns are filled with NULL values.

```sql
SELECT a.col1, b.col2 FROM table1 a LEFT JOIN table2 b ON a.id = b.id;
```

- Right outer join: This join returns all the records from the right table and the matching records from the left table. If there is no match, the left table columns are filled with NULL values.

```sql
SELECT a.col1, b.col2 FROM table1 a RIGHT JOIN table2 b ON a.id = b.id;
```

- Full outer join: This join returns all the records from both tables, regardless of the match. If there is no match, the corresponding table columns are filled with NULL values.

```sql
SELECT a.col1, b.col2 FROM table1 a FULL JOIN table2 b ON a.id = b.id;
```

- Cross join: This join returns the Cartesian product of the two tables, i.e., every row of the left table is joined with every row of the right table.

```sql
SELECT a.col1, b.col2 FROM table1 a CROSS JOIN table2 b;
```

- Scalar subquery: This subquery returns a single value that can be used in the SELECT, WHERE, or HAVING clause of the outer query.

```sql
SELECT col1, (SELECT MAX(col2) FROM table2) AS max_col2 FROM table1;
```

- IN subquery: This subquery returns a set of values that can be used with the IN operator in the WHERE or HAVING clause of the outer query.

```sql
SELECT col1, col2 FROM table1 WHERE col1 IN (SELECT col3 FROM table2);
```

- EXISTS subquery: This subquery returns a boolean value that can be used with the EXISTS operator in the WHERE or HAVING clause of the outer query. The subquery is usually correlated with the outer query, i.e., it references some columns from the outer query.

```sql
SELECT col1, col2 FROM table1 a WHERE EXISTS (SELECT 1 FROM table2 b WHERE a.id = b.id);
```

- Correlated subquery: This subquery is a type of subquery that depends on the outer query for its values. It cannot be executed independently and is usually used with comparison operators in the WHERE or HAVING clause of the outer query.

```sql
SELECT col1, col2 FROM table1 a WHERE col2 > (SELECT AVG(col2) FROM table2 b WHERE a.id = b.id);
```