### Displaying data from multiple tables

- To display data from more than one table, you can use SQL statements that join the tables by a common column or condition .
- There are different types of joins, such as inner join, outer join, cross join, and self join, that determine how the rows from the tables are matched and combined.
- An inner join returns only the rows that satisfy the join condition, while an outer join returns all the rows from one table and the matching rows from another table.
- A cross join returns the Cartesian product of the rows from the tables, meaning every row from one table is paired with every row from another table.
- A self join is a join of a table to itself, using different aliases to distinguish the columns.
- To join tables in SQL, you can use the JOIN keyword in the FROM clause, followed by the names of the tables and the join condition in the ON clause .
- For example, to join the tables food and food_menu by the food_id column, you can write:

```sql
SELECT f.name, fm.price
FROM food f
JOIN food_menu fm
ON f.food_id = fm.food_id;
```

- To display data from multiple tables without joining them, you can use the UNION or UNION ALL operators, which combine the result sets of two or more SELECT statements.
- The UNION operator eliminates duplicate rows, while the UNION ALL operator preserves them.
- The SELECT statements must have the same number and type of columns, and the columns must be in the same order.
- For example, to display the name and price columns from the tables food and drink, you can write:

```sql
SELECT name, price
FROM food
UNION
SELECT name, price
FROM drink;
```

- To display data from multiple tables in a single column, you can use the CONCAT function, which concatenates two or more strings .
- The CONCAT function takes the strings as arguments and returns a single string as the result .
- For example, to display the name and price columns from the table food in a single column, you can write:

```sql
SELECT CONCAT(name, ' - ', price) AS food_info
FROM food;
```

- To display data from multiple tables using a subquery, you can use a SELECT statement inside another SELECT statement, where the inner query returns a value or a set of values that are used by the outer query .
- A subquery can be used in different clauses, such as WHERE, HAVING, FROM, or SELECT .
- For example, to display the name and price columns from the table food where the price is less than the average price of all foods, you can write:

```sql
SELECT name, price
FROM food
WHERE price < (SELECT AVG(price) FROM food);
```