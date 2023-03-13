#### Joins and subqueries in Hive

- Joins are used to combine data from two or more tables based on a common column or condition.
- Subqueries are used to write a query within another query, usually to filter or aggregate data based on some criteria.
- Hive supports four types of joins: inner join, left outer join, right outer join, and full outer join.
- Hive also supports subqueries in the WHERE and HAVING clauses, but not in the SELECT or FROM clauses.
- Here are some points to remember about joins and subqueries in Hive:

  - Hive does not support join conditions that are not equality conditions, such as `t1.col1 > t2.col2`.
  - Hive does not support self-joins, which are joins of a table with itself.
  - Hive does not support cross joins, which are joins without any condition that produce a Cartesian product of the tables.
  - Hive does not support nested joins, which are joins within another join.
  - Hive does not support correlated subqueries, which are subqueries that reference columns from the outer query.
  - Hive does not support EXISTS or IN operators with subqueries, but you can use LEFT SEMI JOIN instead.
  - Hive does not support scalar subqueries, which are subqueries that return a single value, but you can use a join instead.

- Here are some examples of how to write joins and subqueries in Hive:

  - To perform an inner join of two tables `t1` and `t2` on column `id`, you can write:

    ```sql
    SELECT t1.*, t2.*
    FROM t1
    JOIN t2
    ON t1.id = t2.id;
    ```

  - To perform a left outer join of two tables `t1` and `t2` on column `id`, you can write:

    ```sql
    SELECT t1.*, t2.*
    FROM t1
    LEFT OUTER JOIN t2
    ON t1.id = t2.id;
    ```

  - To perform a right outer join of two tables `t1` and `t2` on column `id`, you can write:

    ```sql
    SELECT t1.*, t2.*
    FROM t1
    RIGHT OUTER JOIN t2
    ON t1.id = t2.id;
    ```

  - To perform a full outer join of two tables `t1` and `t2` on column `id`, you can write:

    ```sql
    SELECT t1.*, t2.*
    FROM t1
    FULL OUTER JOIN t2
    ON t1.id = t2.id;
    ```

  - To perform a subquery in the WHERE clause to filter the rows from table `t1` based on the average value of column `col1` from table `t2`, you can write:

    ```sql
    SELECT *
    FROM t1
    WHERE t1.col1 > (SELECT AVG(col1) FROM t2);
    ```

  - To perform a subquery in the HAVING clause to filter the groups from table `t1` based on the maximum value of column `col2` from table `t2`, you can write:

    ```sql
    SELECT t1.col1, SUM(t1.col2) AS total
    FROM t1
    GROUP BY t1.col1
    HAVING total < (SELECT MAX(col2) FROM t2);
    ```

  - To perform a left semi join of two tables `t1` and `t2` on column `id`, which is equivalent to using an IN operator with a subquery, you can write:

    ```sql
    SELECT t1.*
    FROM t1
    LEFT SEMI JOIN t2
    ON t1.id = t2.id;
    ```

  - To perform a join of two tables `t1` and `t2` on column `id`, which is equivalent to using a scalar subquery, you can write:

    ```sql
    SELECT t1.*, (SELECT t2.col1 FROM t2 WHERE t2.id = t1.id) AS col1
    FROM t1;
    ```

- Here are some mnemonics and learning tricks for joins and subqueries in Hive:

  - To remember the four types of joins in Hive, you can use the acronym **FIRL** (Full, Inner, Right, Left).
  - To remember the syntax of joins in Hive, you can use the formula **SELECT FROM JOIN ON**.
  - To remember the syntax of subqueries in Hive, you can use the formula **SELECT FROM WHERE/HAVING (SELECT FROM)**.
  -