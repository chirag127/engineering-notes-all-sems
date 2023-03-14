Joins and subqueries in Hive are used to combine data from different tables or sources based on some common criteria. Joins can be of four types: inner join, left outer join, right outer join, and full outer join. Subqueries are queries nested within another query, usually in the FROM clause. Subqueries can be used to filter, aggregate, or transform data before joining it with other tables.

The following diagram illustrates the basic syntax of joins and subqueries in Hive using ASCII characters:

```
+------------------+    +------------------+    +------------------+
| Table A          |    | Table B          |    | Subquery C       |
| +------+-------+ |    | +------+-------+ |    | +------+-------+ |
| | col1 | col2  | |    | | col3 | col4  | |    | | col5 | col6  | |
| +------+-------+ |    | +------+-------+ |    | +------+-------+ |
| | a1   | a2    | |    | | b1   | b2    | |    | | c1   | c2    | |
| | a3   | a4    | |    | | b3   | b4    | |    | | c3   | c4    | |
| | a5   | a6    | |    | | b5   | b6    | |    | | c5   | c6    | |
| +------+-------+ |    | +------+-------+ |    | +------+-------+ |
+------------------+    +------------------+    +------------------+

INNER JOIN: returns only the rows that match the join condition

SELECT A.col1, B.col4 FROM A JOIN B ON (A.col2 = B.col3);

+------+-------+
| col1 | col4  |
+------+-------+
| a1   | b2    |
| a3   | b4    |
| a5   | b6    |
+------+-------+

LEFT OUTER JOIN: returns all the rows from the left table and the matching rows from the right table, or NULL if no match

SELECT A.col1, B.col4 FROM A LEFT OUTER JOIN B ON (A.col2 = B.col3);

+------+-------+
| col1 | col4  |
+------+-------+
| a1   | b2    |
| a3   | b4    |
| a5   | b6    |
| a7   | NULL  |
| a9   | NULL  |
+------+-------+

RIGHT OUTER JOIN: returns all the rows from the right table and the matching rows from the left table, or NULL if no match

SELECT A.col1, B.col4 FROM A RIGHT OUTER JOIN B ON (A.col2 = B.col3);

+------+-------+
| col1 | col4  |
+------+-------+
| a1   | b2    |
| a3   | b4    |
| a5   | b6    |
| NULL | b8    |
| NULL | b10   |
+------+-------+

FULL OUTER JOIN: returns all the rows from both tables, and NULL for the columns that do not match the join condition

SELECT A.col1, B.col4 FROM A FULL OUTER JOIN B ON (A.col2 = B.col3);

+------+-------+
| col1 | col4  |
+------+-------+
| a1   | b2    |
| a3   | b4    |
| a5   | b6    |
| a7   | NULL  |
| a9   | NULL  |
| NULL | b8    |
| NULL | b10   |
+------+-------+

SUBQUERY: returns a table that can be used in the FROM clause of another query

SELECT A.col1, C.col6 FROM A JOIN (SELECT col5, col6 FROM B WHERE col4 > 5) C ON (A.col2 = C.col5);

+------+-------+
| col1 | col6  |
+------+-------+
| a5   | c6    |
| a7   | c8    |
| a9   | c10   |
+------+-------+
```