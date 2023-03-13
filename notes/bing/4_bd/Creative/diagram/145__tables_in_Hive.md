Tables in Hive are analogous to tables in a relational database management system. Each table belongs to a directory in HDFS. By default, it is /user/hive/warehouse directory. There are two types of tables that you can create with Hive: internal and external  .

Internal tables store data in the Hive data warehouse. The data is managed by Hive and deleted when the table is dropped. Internal tables are also called managed tables. External tables store data outside the data warehouse. The data is not managed by Hive and remains even when the table is dropped. External tables are also called unmanaged tables.

The following diagram illustrates the basic architecture of tables in Hive using ASCII characters:

```
+------------------+    +------------------+    +------------------+
|                  |    |                  |    |                  |
|  Internal Table  |    |  External Table  |    |  External Table  |
|                  |    |                  |    |                  |
+------------------+    +------------------+    +------------------+
|                  |    |                  |    |                  |
|  /user/hive/     |    |  /user/data/     |    |  /user/logs/     |
|  warehouse/      |    |                  |    |                  |
|  table1/         |    |  table2/         |    |  table3/         |
|                  |    |                  |    |                  |
+------------------+    +------------------+    +------------------+
|                  |    |                  |    |                  |
|  data1.txt       |    |  data2.txt       |    |  data3.txt       |
|                  |    |                  |    |                  |
+------------------+    +------------------+    +------------------+
```