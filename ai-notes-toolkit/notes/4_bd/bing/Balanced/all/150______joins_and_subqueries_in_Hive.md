#### Joins and Subqueries in Hive

- Joins are used to combine data from two or more tables based on a common column or condition.
- Subqueries are used to create temporary tables from a query expression and use them in another query.
- Hive supports different types of joins, such as inner join, left outer join, right outer join, full outer join, cross join, and semi join.
- Hive supports subqueries only in the FROM clause (through Hive 0.12). The subquery has to be given a name because every table in a FROM clause must have a name. The columns in the subquery select list are available in the outer query just like columns of a table. The subquery can also be a query expression with UNION. Hive supports arbitrary levels of subqueries.
- Examples of joins and subqueries in Hive:

  - Inner join: returns the records that are common to both tables based on the join condition.

    ```sql
    SELECT a.col1, b.col2 FROM table1 a JOIN table2 b ON a.id = b.id;
    ```

  - Left outer join: returns all the records from the left table and the matching records from the right table. If there is no match, the right side will be null.

    ```sql
    SELECT a.col1, b.col2 FROM table1 a LEFT OUTER JOIN table2 b ON a.id = b.id;
    ```

  - Right outer join: returns all the records from the right table and the matching records from the left table. If there is no match, the left side will be null.

    ```sql
    SELECT a.col1, b.col2 FROM table1 a RIGHT OUTER JOIN table2 b ON a.id = b.id;
    ```

  - Full outer join: returns all the records from both tables, regardless of the match. If there is no match, the missing side will be null.

    ```sql
    SELECT a.col1, b.col2 FROM table1 a FULL OUTER JOIN table2 b ON a.id = b.id;
    ```

  - Cross join: returns the Cartesian product of the two tables, i.e. every row of the left table is paired with every row of the right table.

    ```sql
    SELECT a.col1, b.col2 FROM table1 a CROSS JOIN table2 b;
    ```

  - Semi join: returns the records from the left table that have a match in the right table. It is similar to an inner join, but it only returns the columns from the left table.

    ```sql
    SELECT a.col1 FROM table1 a WHERE a.id IN (SELECT b.id FROM table2 b);
    ```

  - Subquery: creates a temporary table from a query expression and uses it in another query. The subquery has to be given a name and can be nested inside another subquery.

    ```sql
    SELECT c.col1, d.col2 FROM (SELECT a.col1, b.col2 FROM table1 a JOIN table2 b ON a.id = b.id) c JOIN (SELECT e.col1, f.col2 FROM table3 e JOIN table4 f ON e.id = f.id) d ON c.col1 = d.col1;
    ```