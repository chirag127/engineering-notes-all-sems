

### Joins and Subqueries in Hive

* Joins in Hive allow users to query data from multiple tables. Joins are performed on the basis of a common field between the two tables.
* Subqueries in Hive are used to query data from multiple tables. Subqueries are performed on the basis of a common field between the two tables.
* Hive supports the following types of joins:
  * Inner Join: An inner join is the most common type of join and returns only the records that match the given criteria.
  * Left Outer Join: A left outer join returns all the records from the left table, even if there are no matches in the right table.
  * Right Outer Join: A right outer join returns all the records from the right table, even if there are no matches in the left table.
  * Full Outer Join: A full outer join returns all the records from both the left and right tables, even if there are no matches in either table.
* Hive also supports the following types of subqueries:
  * Correlated Subqueries: A correlated subquery is a subquery that is evaluated for each row in the outer query.
  * Non-Correlated Subqueries: A non-correlated subquery is a subquery that is evaluated once for the entire outer query.
* Hive also supports the following types of aggregate functions:
  * COUNT: Counts the number of rows in a table.
  * SUM: Sums the values of a given column.
  * AVG: Calculates the average of a given column.
  * MIN: Finds the minimum value of a given column.
  * MAX: Finds the maximum value of a given column.
* Hive also supports the following types of window functions:
  * RANK: Ranks the rows in a table.
  * DENSE_RANK: Ranks the rows in a table, with no gaps in the ranking.
  * ROW_NUMBER: Assigns a unique number to each row in a table.
  * NTILE: Splits the rows in a table into a specified number of groups.