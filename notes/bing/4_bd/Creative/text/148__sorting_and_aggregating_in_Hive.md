#### Sorting and aggregating in Hive

- Sorting data in Hive can be achieved by using a standard `ORDER BY` clause, but it has a drawback. `ORDER BY` produces a result that is totally sorted, as expected, but to do so it sets the number of reducers to one, making it very inefficient for large datasets.
- To sort data more efficiently, Hive supports two other clauses: `SORT BY` and `DISTRIBUTE BY`. `SORT BY` sorts the data within each reducer partition, but does not guarantee any global order. `DISTRIBUTE BY` partitions the data by a specified column or expression, but does not sort within each partition. These clauses can be combined to achieve a global order with multiple reducers.
- For example, the following query sorts the data by the `name` column using multiple reducers:

```sql
SELECT * FROM students
DISTRIBUTE BY name
SORT BY name;
```

- Aggregating data in Hive can be done by using built-in aggregate functions, such as `MAX`, `MIN`, `AVG`, `SUM`, `COUNT`, etc. These functions are usually used with the `GROUP BY` clause, which groups the data by one or more columns or expressions. If there is no `GROUP BY` clause specified, the aggregate functions apply to the whole table by default.
- For example, the following query calculates the average score of each student:

```sql
SELECT name, AVG(score) AS average_score
FROM students
GROUP BY name;
```

- Hive also supports advanced aggregation by using `GROUPING SETS`, `ROLLUP`, `CUBE`, analytic functions, and windowing. These features allow more complex and flexible grouping and aggregation operations.
- For example, the following query calculates the total score of each student, each subject, and the grand total using `GROUPING SETS`:

```sql
SELECT name, subject, SUM(score) AS total_score
FROM students
GROUP BY GROUPING SETS ((name, subject), (name), (subject), ());
```

- To aggregate strings in Hive, one can use the `collect_list` or `collect_set` functions, which return an array of strings for each group. The difference between them is that `collect_set` removes duplicates, while `collect_list` preserves them. To order the strings within each array, one can use the `sort_array` function.
- For example, the following query collects and sorts the subjects of each student:

```sql
SELECT name, sort_array(collect_list(subject)) AS subjects
FROM students
GROUP BY name;
```