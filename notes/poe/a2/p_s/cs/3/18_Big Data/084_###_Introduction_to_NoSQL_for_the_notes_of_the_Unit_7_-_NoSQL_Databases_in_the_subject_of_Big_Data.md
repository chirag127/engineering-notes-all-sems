 Here is the content in markdown format:

#### Joins and Subqueries in Hive

- Joins in Hive can be performed on tables/partitions with matching schemas using `JOIN` keywords. The supported join types are:

**Equi-Joins:**

- `INNER JOIN`: Returns records that have matching values in both tables
- `LEFT OUTER JOIN`: Returns all records from the left table, and the matched records from the right table
- `RIGHT OUTER JOIN`: Returns all records from the right table, and the matched records from the left table
- `FULL OUTER JOIN`: Returns all records when there is a match in either left or right table

**Non-Equi Joins:** Joins can also be performed on ranges or intervals using operators like >, <, >=, <= on the join keys.

- Subqueries can be used in the `SELECT` or `FROM` clause of a query to derive a temporary table/view that can be used in the main query. This enables querying hierarchical/relational data or using results of one query in another.
- The subquery must be enclosed within parentheses and can use aliases to refer to the subquery in the main query.
- Subqueries are a powerful way to write complex queries in a structured way and can lead to more optimized execution plans in many cases.

**Examples:**

- `SELECT * FROM table1 JOIN table2 ON table1.key = table2.key`
- `SELECT * FROM table1 LEFT OUTER JOIN table2 ON table1.key = table2.key`
- `SELECT * FROM (SELECT col1, col2 FROM table3 WHERE cond) tmp JOIN table4 ON tmp.col1 = table4.col1`

**Advantages:**
- Joins and subqueries enable querying related data from multiple tables in a single query.
- They make queries more modular, reusable and optimized.
- They provide more powerful ways to filter and aggregate data.

**Disadvantages:**
- Joins and subqueries can make queries more complex to understand, debug and tune.
- They can lead to cartesian products and unintended results if not used correctly.
- Subqueries can be computationally expensive if not optimized properly.