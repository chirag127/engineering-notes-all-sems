Tables in Hive are a way of storing and organizing data in a relational format. There are two types of tables in Hive: internal and external. Internal tables are managed by Hive and store data in the Hive warehouse directory. External tables are not managed by Hive and store data outside the Hive warehouse directory. The general syntax for creating a table in Hive is:

```
CREATE [EXTERNAL] TABLE [IF NOT EXISTS] [db_name.]table_name
(col_name data_type [COMMENT 'col_comment'], ...)
[COMMENT 'table_comment']
[ROW FORMAT row_format]
[FIELDS TERMINATED BY char]
[STORED AS file_format];
```

The following diagram illustrates the basic architecture of a table in Hive using ASCII characters:

```
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Column Name    |    |  Data Type      |    |  Column Comment |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  id             |    |  int            |    |  employee id    |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  name           |    |  string         |    |  employee name  |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  country        |    |  string         |    |  employee country |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  department     |    |  string         |    |  employee department |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  salary         |    |  int            |    |  employee salary |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
```

The table name is `employees` and it has five columns: `id`, `name`, `country`, `department`, and `salary`. Each column has a data type and an optional comment. The row format specifies how the data is stored and delimited in the table. The file format specifies the format of the files that store the data in the table. For example, the table can be stored as text files, sequence files, ORC files, etc.