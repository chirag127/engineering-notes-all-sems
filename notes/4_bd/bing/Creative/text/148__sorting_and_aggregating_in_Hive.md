#### Sorting and aggregating in Hive

- Sorting data in Hive can be achieved by using a standard `ORDER BY` clause, but it has a drawback. It produces a result that is totally sorted, as expected, but it sets the number of reducers to one, making it very inefficient for large datasets.
- When a globally sorted result is not required, then you can use Hive's nonstandard extension, `SORT BY` instead. It produces a sorted file per reducer.
- In some cases, you want to control which reducer a particular row goes to, typically so you can perform some subsequent aggregation. This is what Hive's `DISTRIBUTE BY` clause does.
- If the columns for `SORT BY` and `DISTRIBUTE BY` are the same, you can use `CLUSTER BY` as a shorthand for specifying both.
- Aggregating data in Hive can be done by using built-in aggregate functions, such as `MAX`, `MIN`, `AVG`, `COUNT`, etc. These functions are usually used with the `GROUP BY` clause. If there is no `GROUP BY` clause specified, it aggregates over the whole table by default.
- Hive also supports advanced aggregation by using `GROUPING SETS`, `ROLLUP`, `CUBE`, analytic functions, and windowing.
- `GROUPING SETS` allows you to specify multiple groupings in a single query, which is equivalent to a `UNION ALL` of different `GROUP BY` clauses.
- `ROLLUP` is a shorthand for a list of grouping sets that contain all the prefixes of the `GROUP BY` clause.
- `CUBE` is a shorthand for a list of grouping sets that contain all the combinations of the `GROUP BY` clause.
- Analytic functions are functions that compute an aggregate value based on a group of rows. They differ from aggregate functions in that they return multiple rows for each group.
- Windowing allows you to specify a window or frame of rows for each row, over which the analytic function operates.