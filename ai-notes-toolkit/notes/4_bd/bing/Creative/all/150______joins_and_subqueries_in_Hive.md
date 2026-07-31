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

- Left outer join: This join returns all the records from the left table and the matching records from the right table. If there is no match, the right table columns are filled with NULL.

```sql
SELECT a.col1, b.col2 FROM table1 a LEFT OUTER JOIN table2 b ON a.id = b.id;
```

- Right outer join: This join returns all the records from the right table and the matching records from the left table. If there is no match, the left table columns are filled with NULL.

```sql
SELECT a.col1, b.col2 FROM table1 a RIGHT OUTER JOIN table2 b ON a.id = b.id;
```

- Full outer join: This join returns all the records from both tables, and fills the missing values with NULL.

```sql
SELECT a.col1, b.col2 FROM table1 a FULL OUTER JOIN table2 b ON a.id = b.id;
```

- Cross join: This join returns the Cartesian product of the two tables, i.e., every row of the left table is joined with every row of the right table.

```sql
SELECT a.col1, b.col2 FROM table1 a CROSS JOIN table2 b;
```

- Semi join: This join returns the records from the left table that have a match in the right table, but does not return any columns from the right table.

```sql
SELECT a.col1 FROM table1 a WHERE a.id IN (SELECT b.id FROM table2 b);
```

- Subquery: This query creates a temporary table that can be used in the main query or another subquery. The subquery has to be given a name or alias.

```sql
SELECT col1, col2 FROM (SELECT * FROM table1 WHERE col3 > 10) sub;
```

- Subquery with UNION: This query creates a temporary table that combines the results of two or more queries using the UNION operator. The subquery has to be given a name or alias.

```sql
SELECT col1, col2 FROM (SELECT * FROM table1 UNION SELECT * FROM table2) sub;
```

- Join with subquery: This query joins a table with a subquery based on a common column or condition.

```sql
SELECT a.col1, b.col2 FROM table1 a JOIN (SELECT * FROM table2 WHERE col3 < 20) b ON a.id = b.id;
```