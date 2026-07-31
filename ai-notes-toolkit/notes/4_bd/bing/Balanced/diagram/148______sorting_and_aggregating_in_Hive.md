#### Sorting and Aggregating in Hive

- Sorting data in Hive can be achieved by using a standard `ORDER BY` clause, but it has a drawback. `ORDER BY` produces a result that is totally sorted, as expected, but to do so it sets the number of reducers to one, making it very inefficient for large datasets.
- A better alternative for sorting data in Hive is to use the `SORT BY` clause, which sorts the data within each reducer. This produces a partially ordered result that is faster and more scalable than `ORDER BY`.
- Another option for sorting data in Hive is to use the `DISTRIBUTE BY` clause, which distributes the data among reducers based on a column or expression. This can be useful for performing joins or aggregations on large datasets.
- Aggregating data in Hive can be done by using built-in aggregate functions, such as `MAX`, `MIN`, `AVG`, `SUM`, `COUNT`, etc. These functions are usually used with the `GROUP BY` clause, which groups the data by one or more columns or expressions.
- If there is no `GROUP BY` clause specified, the aggregate functions operate on the whole table by default. Besides aggregate functions, all other columns that are selected must also be included in the `GROUP BY` clause.
- Hive also supports advanced aggregation by using `GROUPING SETS`, `ROLLUP`, `CUBE`, analytic functions, and windowing. These features allow for more complex and flexible aggregations, such as subtotals, totals, and moving averages.
- To order the aggregated results by a column or expression, the `ORDER BY` or `SORT BY` clause can be used after the `GROUP BY` clause. For example, to order the results by the count of each group in descending order, the following query can be used:

```sql
SELECT A, B, COUNT(*) AS cnt
FROM test_table
GROUP BY A, B
ORDER BY cnt DESC;
```

- To concatenate the values of a string column within each group, the `collect_list` or `collect_set` function can be used. These functions return an array of strings for each group. The difference between them is that `collect_list` preserves the order and duplicates of the values, while `collect_set` removes the duplicates and does not guarantee any order.
- For example, to aggregate the values of column C within each group of A and B, and order them by column D, the following query can be used:

```sql
SELECT A, B, collect_list(C) AS C_list
FROM test_table
GROUP BY A, B
ORDER BY D;
```