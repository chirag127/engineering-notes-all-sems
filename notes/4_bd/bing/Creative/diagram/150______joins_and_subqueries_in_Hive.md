#### Joins and subqueries in Hive

- Joins are used to combine data from two or more tables based on a common column or condition.
- Subqueries are used to create temporary tables that can be used in the main query or join.
- Hive supports different types of joins, such as inner join, left outer join, right outer join, full outer join, cross join, and semi join.
- Hive supports subqueries only in the FROM clause, and the subquery has to be given a name or alias.
- The columns in the subquery select list are available in the outer query just like columns of a table.
- The subquery can also be a query expression with UNION.
- Hive supports arbitrary levels of subqueries, but they may affect the performance of the query.

##### Examples of joins and subqueries in Hive

- Inner join: returns the records that match in both tables.

```sql
SELECT a.col1, b.col2 FROM table1 a JOIN table2 b ON a.id = b.id;
```

- Left outer join: returns all the records from the left table and the matching records from the right table.

```sql
SELECT a.col1, b.col2 FROM table1 a LEFT JOIN table2 b ON a.id = b.id;
```

- Right outer join: returns all the records from the right table and the matching records from the left table.

```sql
SELECT a.col1, b.col2 FROM table1 a RIGHT JOIN table2 b ON a.id = b.id;
```

- Full outer join: returns all the records from both tables, with null values for the non-matching records.

```sql
SELECT a.col1, b.col2 FROM table1 a FULL JOIN table2 b ON a.id = b.id;
```

- Cross join: returns the cartesian product of the two tables, i.e. every record from the first table is paired with every record from the second table.

```sql
SELECT a.col1, b.col2 FROM table1 a CROSS JOIN table2 b;
```

- Semi join: returns the records from the left table that have a matching record in the right table, but does not return any columns from the right table.

```sql
SELECT a.col1 FROM table1 a WHERE a.id IN (SELECT b.id FROM table2 b);
```

- Subquery in the FROM clause: creates a temporary table that can be used in the main query or join.

```sql
SELECT c.col1, c.col2 FROM (SELECT a.col1, b.col2 FROM table1 a JOIN table2 b ON a.id = b.id) c;
```