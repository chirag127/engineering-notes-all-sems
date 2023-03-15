### Displaying data from multiple tables

- To display data from more than one table, you can use SQL statements that join the tables by a common column or condition.
- There are different types of joins, such as inner join, outer join, cross join, and self join, that determine how the rows from the tables are matched and displayed.
- You can also use subqueries to retrieve data from more than one table by nesting one SELECT statement inside another.
- You can also use UNION or UNION ALL operators to combine the results of two or more SELECT statements into a single result set.

#### Examples of displaying data from multiple tables using Oracle/MySQL

- To display the name and price of the food items from the food table and the food_menu table, you can use an inner join as follows:

```sql
SELECT f.name, f.price
FROM food f
INNER JOIN food_menu fm
ON f.food_id = fm.food_id;
```

- To display the name and price of the food items from the food table and the food_menu table, and also include the rows that do not have a matching food_id in both tables, you can use a full outer join as follows:

```sql
SELECT f.name, f.price
FROM food f
FULL OUTER JOIN food_menu fm
ON f.food_id = fm.food_id;
```

- To display the name and price of the food items from the food table and the food_menu table, and also include the rows that have a matching food_id in both tables, you can use a cross join as follows:

```sql
SELECT f.name, f.price
FROM food f
CROSS JOIN food_menu fm;
```

- To display the name and price of the food items from the food table and the food_menu table, and also include the rows that have the same name in both tables, you can use a self join as follows:

```sql
SELECT f.name, f.price
FROM food f
JOIN food_menu fm
ON f.name = fm.name;
```

- To display the name and price of the food items from the food table and the food_menu table, and also filter the results by a condition, you can use a subquery as follows:

```sql
SELECT f.name, f.price
FROM food f
WHERE f.food_id IN
(SELECT fm.food_id
FROM food_menu fm
WHERE fm.category = 'dessert');
```

- To display the name and price of the food items from the food table and the food_menu table, and also combine the results into one table, you can use a UNION operator as follows:

```sql
SELECT f.name, f.price
FROM food f
UNION
SELECT fm.name, fm.price
FROM food_menu fm;
```

- To display the name and price of the food items from the food table and the food_menu table, and also combine the results into one table, including the duplicate rows, you can use a UNION ALL operator as follows:

```sql
SELECT f.name, f.price
FROM food f
UNION ALL
SELECT fm.name, fm.price
FROM food_menu fm;
```