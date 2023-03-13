Querying data in Hive is done using Hive Query Language (HQL), which is a declarative language similar to SQL. HQL allows users to process and analyze structured and semi-structured data stored in Hadoop Distributed File System (HDFS) or other data sources. HQL converts the queries into MapReduce, Tez, or Spark jobs that run on the Hadoop cluster.

The following diagram illustrates the basic architecture of a Hive query:

```
+------------------+      +-----------------+      +-----------------+
|                  |      |                 |      |                 |
|   HQL Query      |----->|  Hive Compiler  |----->|  Execution Plan |
|                  |      |                 |      |                 |
+------------------+      +-----------------+      +-----------------+
                                                        |
                                                        |
                                                        V
+------------------+      +-----------------+      +-----------------+
|                  |      |                 |      |                 |
|  Hive Optimizer  |<-----|  Execution Plan |----->|  Driver/Task    |
|                  |      |                 |      |  Execution      |
+------------------+      +-----------------+      +-----------------+
                                                        |
                                                        |
                                                        V
+------------------+      +-----------------+      +-----------------+
|                  |      |                 |      |                 |
|  MapReduce/Tez/  |<-----|  Driver/Task    |----->|  HDFS/Local FS  |
|  Spark Jobs      |      |  Execution      |      |                 |
|                  |      |                 |      |                 |
+------------------+      +-----------------+      +-----------------+
```

The basic way to query data in Hive is using SELECT statement, which has the following syntax:

```
SELECT [ALL | DISTINCT] select_expr, select_expr, ...
FROM table_reference
[WHERE where_condition]
[GROUP BY col_list]
[HAVING having_condition]
[ORDER BY col_list]
[LIMIT number]
[CLUSTER BY col_list | [DISTRIBUTE BY col_list] [SORT BY col_list]]
```

Some examples of Hive queries are:

- Select all records from a table:

```
SELECT * FROM table_name;
```

- Select specific columns from a table:

```
SELECT col1, col2, col3 FROM table_name;
```

- Select records with a filter condition:

```
SELECT * FROM table_name WHERE col1 = 'value';
```

- Select records with aggregation and grouping:

```
SELECT col1, COUNT(*) AS count FROM table_name GROUP BY col1;
```

- Select records with sorting and limiting:

```
SELECT * FROM table_name ORDER BY col1 DESC LIMIT 10;
```

- Select records with join operation:

```
SELECT t1.col1, t2.col2 FROM table1 t1 JOIN table2 t2 ON t1.col3 = t2.col3;
```