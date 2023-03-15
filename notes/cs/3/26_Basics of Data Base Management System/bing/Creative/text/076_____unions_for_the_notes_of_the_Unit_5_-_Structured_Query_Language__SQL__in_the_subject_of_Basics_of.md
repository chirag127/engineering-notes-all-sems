### Unions

- A union is an SQL operator that combines the result sets of two or more SELECT queries into a single result set.
- A union can be used to merge data from different tables that have the same number and type of columns.
- A union can also be used to remove duplicate rows from the combined result set, or to include them by using the ALL keyword.
- The syntax of a union is:

```sql
SELECT column1, column2, ..., columnN FROM table1
UNION [ALL]
SELECT column1, column2, ..., columnN FROM table2
UNION [ALL]
...
SELECT column1, column2, ..., columnN FROM tableN;
```

- The columns in each SELECT statement must have the same name, data type, and order.
- The UNION operator applies a distinct operation to the combined result set, which means that it eliminates duplicate rows. To keep the duplicate rows, use the UNION ALL operator instead.
- The UNION operator can be combined with other SQL clauses, such as ORDER BY, LIMIT, OFFSET, etc. However, these clauses must be applied to the final result set, not to each individual SELECT statement.
- The UNION operator can be used to perform set operations, such as union, intersection, and difference, on two or more tables. For example, to find the intersection of two tables, use the following query:

```sql
SELECT column1, column2, ..., columnN FROM table1
INTERSECT
SELECT column1, column2, ..., columnN FROM table2;
```

- The INTERSECT operator is equivalent to the UNION operator with a WHERE clause that filters out the rows that are not in both tables. Similarly, to find the difference of two tables, use the following query:

```sql
SELECT column1, column2, ..., columnN FROM table1
EXCEPT
SELECT column1, column2, ..., columnN FROM table2;
```

- The EXCEPT operator is equivalent to the UNION operator with a WHERE clause that filters out the rows that are in both tables.