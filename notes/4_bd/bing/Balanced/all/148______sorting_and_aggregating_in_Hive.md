#### Sorting and Aggregating in Hive

- Sorting data in Hive can be achieved by using a standard `ORDER BY` clause, but there is a catch. `ORDER BY` produces a result that is totally sorted, as expected, but to do so it sets the number of reducers to one, making it very inefficient for large datasets.
- To sort data more efficiently, Hive provides two alternatives: `SORT BY` and `DISTRIBUTE BY`. `SORT BY` sorts the data within each reducer partition, but does not guarantee any global order. `DISTRIBUTE BY` partitions the data by a specified column or expression, and sends each partition to a different reducer. `DISTRIBUTE BY` can be combined with `SORT BY` to achieve a global order with parallel reducers.
- Aggregating data in Hive can be done by using built-in aggregate functions, such as `MAX`, `MIN`, `AVG`, `SUM`, `COUNT`, etc. These functions are usually used with the `GROUP BY` clause, which groups the data by one or more columns or expressions. If there is no `GROUP BY` clause specified, the aggregation is done over the whole table by default.
- Hive also supports advanced aggregation by using `GROUPING SETS`, `ROLLUP`, `CUBE`, analytic functions, and windowing. `GROUPING SETS` allows specifying multiple groupings in one query, which is equivalent to a `UNION ALL` of different `GROUP BY` queries. `ROLLUP` and `CUBE` are special cases of `GROUPING SETS` that generate subtotals and totals for hierarchical groupings. Analytic functions are similar to aggregate functions, but they operate on a window or a partition of rows, rather than the entire group. Windowing allows specifying the range or rows for each analytic function.
- To order the results of an aggregation by the aggregated values, such as `COUNT`, `SUM`, or `AVG`, the `ORDER BY` clause can be used. For example, to order the results by the count of each group in descending order, the query can be written as:

```sql
SELECT A, B, COUNT(*) AS cnt
FROM test_table
GROUP BY A, B
ORDER BY cnt DESC;
```

: https://hadooptechblog.wordpress.com/2015/12/30/hive-sorting-and-join/
: https://timepasstechies.com/hive-tutorial-5-hive-data-aggregation-group-case-coalesce-distinct-grouping-sets-rollup-cube/