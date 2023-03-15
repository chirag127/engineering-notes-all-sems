# Aggregating data using group function for the notes of the Unit 3 - Writing SQL statements Using ORACLE /MYSQL in the subject of Database Management Systems Lab

- Aggregate functions are functions that operate on a set of values and return a single value. They are commonly used to perform calculations or summaries on groups of rows in a table or view. 
- Some examples of aggregate functions are `SUM`, `MAX`, `MIN`, `COUNT`, `AVG`, `LISTAGG`, `JSON_ARRAYAGG`, etc.   
- Aggregate functions can appear in the select list and in the `ORDER BY` and `HAVING` clauses of a `SELECT` statement. 
- To use aggregate functions with a `GROUP BY` clause, the following syntax is used:

```sql
SELECT column1, column2, ..., aggregate_function(column)
FROM table
WHERE condition
GROUP BY column1, column2, ...
HAVING condition
ORDER BY column;
```

- The `GROUP BY` clause divides the rows of the queried table or view into groups based on the values of the specified columns. 
- The aggregate function is applied to each group of rows and returns a single result row for each group. 
- The `HAVING` clause is used to filter the groups based on a condition that involves an aggregate function. 
- The `ORDER BY` clause is used to sort the result rows based on the values of the specified columns or expressions. 
- If the `GROUP BY` clause is omitted, then the aggregate function is applied to all the rows in the queried table or view and returns a single result row. 
- The `GROUP BY` clause in SQL is not used to sort or keep the rows together, but to summarize or aggregate the data by the specified columns. 
- The order of the columns in the `GROUP BY` clause determines the level of grouping. The first column is the most general level of grouping, and the subsequent columns are more specific levels of grouping. 
- The columns in the `GROUP BY` clause must also appear in the select list, unless they are arguments to an aggregate function. 
- The columns in the select list that are not arguments to an aggregate function must also appear in the `GROUP BY` clause. 
- The `GROUP BY` clause can also use expressions or aliases as grouping criteria, as long as they are not ambiguous. 
- The `GROUP BY` clause can also use ordinal numbers to refer to the columns in the select list, starting from 1. For example, `GROUP BY 1, 2` means group by the first and second columns in the select list. 
- The `GROUP BY` clause can also use the `ROLLUP`, `CUBE`, `GROUPING SETS`, or `WITH ROLLUP` modifiers to generate subtotals and totals for the groups.  
- The `GROUP BY` clause can also use the `HAVING` clause to filter the groups based on a condition that involves an aggregate function. 
- The `HAVING` clause is similar to the `WHERE` clause, but it operates on groups rather than rows. 
- The `HAVING` clause can only use columns that appear in the `GROUP BY` clause or are arguments to an aggregate function. 
- The `HAVING` clause can also use expressions or aliases as filtering criteria, as long as they are not ambiguous. 
- The `HAVING` clause can also use ordinal numbers to refer to the columns in the select list, starting from 1. For example, `HAVING 3 > 100` means filter the groups where the third column in the select list is greater than 100. 
- The `HAVING` clause can also use logical operators such as `AND`, `OR`, and `NOT` to combine multiple conditions. 
- The `HAVING` clause can also use subqueries to compare the values of the groups with the values of another table or view. 
- The `HAVING` clause is evaluated after the `GROUP BY` clause and before the `ORDER BY` clause. [^1^