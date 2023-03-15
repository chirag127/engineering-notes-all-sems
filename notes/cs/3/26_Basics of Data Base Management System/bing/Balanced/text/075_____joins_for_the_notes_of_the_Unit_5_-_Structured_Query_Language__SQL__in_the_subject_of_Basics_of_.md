### Joins

- A join is a way of combining data from two or more tables based on a common column or condition.
- A join condition specifies how the tables are related, usually by comparing the values of a column in each table.
- A join can be classified into different types, depending on how the data is matched and retrieved from the tables.
- The most common types of joins are:

  - **Inner join**: This join returns only the rows that have matching values in both tables. It is the default type of join in SQL.
  - **Left outer join**: This join returns all the rows from the left table, and the matching rows from the right table. If there is no match, the right side will have NULL values.
  - **Right outer join**: This join returns all the rows from the right table, and the matching rows from the left table. If there is no match, the left side will have NULL values.
  - **Full outer join**: This join returns all the rows from both tables, and matches them if possible. If there is no match, both sides will have NULL values.
  - **Cross join**: This join returns the Cartesian product of the two tables, which means every row in the first table is paired with every row in the second table.
  - **Self join**: This join is used to join a table with itself, as if it were two separate tables. It is useful for comparing values within the same table.

- The syntax for a join in SQL is:

  ```sql
  SELECT column_list
  FROM table1
  JOIN table2
  ON join_condition;
  ```

- The join condition can be any logical expression that evaluates to true or false. It is usually based on the equality of a column in each table, but it can also use other operators or functions.
- The join type can be specified using the keywords INNER, LEFT OUTER, RIGHT OUTER, FULL OUTER, or CROSS before the word JOIN. If no join type is specified, it is assumed to be an inner join.
- The column list can include columns from both tables, or use aliases to rename them. It can also use aggregate functions or expressions to perform calculations on the data.
- The order of the tables in the join does not affect the result, unless the join type is left or right. In that case, the first table is considered the left table, and the second table is considered the right table.
- The join can be combined with other clauses, such as WHERE, GROUP BY, HAVING, ORDER BY, or LIMIT, to filter, group, or sort the data.