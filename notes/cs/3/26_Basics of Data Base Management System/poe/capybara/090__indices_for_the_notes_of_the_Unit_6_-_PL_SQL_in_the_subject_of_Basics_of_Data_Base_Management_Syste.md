### Indices for the Notes of Unit 6 - PL/SQL

- An index in a database is a data structure that improves the speed of data retrieval operations on a database table.
- In PL/SQL, indices are created to improve the speed of queries on large data sets.
- There are two types of indices in PL/SQL: B-tree indices and bitmap indices.
- B-tree indices are most commonly used in PL/SQL. They are useful for range queries and equality queries. B-tree indices are also used to enforce unique constraints on columns.
- Bitmap indices are useful for queries that involve multiple columns. They are used to optimize queries that involve complex logical expressions.
- It is important to note that indices come with a cost. They require additional disk space and can slow down the insert and update operations on a table. Therefore, indices should be used judiciously and only when necessary.
- In PL/SQL, indices can be created using the CREATE INDEX statement. The syntax of the CREATE INDEX statement is as follows:

```sql
CREATE INDEX index_name
ON table_name (column1, column2, ...);
```

- In addition to the CREATE INDEX statement, there are other statements that can be used to manage indices in PL/SQL. These include ALTER INDEX, DROP INDEX, and ANALYZE INDEX.
- It is important to regularly analyze the indices in a database to ensure that they are being used effectively. The ANALYZE INDEX statement can be used to collect statistics on an index and to identify any performance issues.
- Finally, it is important to note that indices should be designed with the specific query requirements in mind. A poorly designed index can actually slow down queries rather than speed them up. Therefore, it is important to carefully consider the query patterns before creating an index.