#### Tables in Hive

- Tables in Hive are similar to tables in a relational database management system. They store data in rows and columns and can be queried using HiveQL, a SQL-like language.
- Tables in Hive can be broadly classified into two types: internal and external .
- Internal tables are also known as managed tables. They are the default type of tables in Hive. They store data in the Hive data warehouse, which is located at `/hive/warehouse/` on the default storage for the cluster.
- External tables store data outside the Hive data warehouse. They can be stored on any storage accessible by the cluster, such as HDFS, Azure Blob Storage, or Amazon S3.
- The main difference between internal and external tables is how Hive handles the data when the table is dropped. When an internal table is dropped, Hive deletes both the table metadata and the data files. When an external table is dropped, Hive only deletes the table metadata, but the data files remain intact .
- Use internal tables when one of the following conditions applies:
  - The data is temporary and can be deleted when the table is dropped.
  - The data is only used by Hive and not by other applications.
  - The data is loaded from local files using the `LOAD DATA` command.
- Use external tables when one of the following conditions applies:
  - The data is permanent and should not be deleted when the table is dropped.
  - The data is shared by Hive and other applications.
  - The data is loaded from external sources using the `LOCATION` clause.
- The general syntax for creating a table in Hive is:

  ```sql
  CREATE [EXTERNAL] TABLE [IF NOT EXISTS] table_name
  (column_name data_type [COMMENT column_comment], ...)
  [COMMENT table_comment]
  [PARTITIONED BY (column_name data_type [COMMENT column_comment], ...)]
  [CLUSTERED BY (column_name, ...) [SORTED BY (column_name [ASC|DESC], ...)] INTO num_buckets BUCKETS]
  [SKEWED BY (column_name, ...) ON ((column_value, ...), ...) [STORED AS DIRECTORIES]]
  [ROW FORMAT row_format]
  [STORED AS file_format]
  [LOCATION hdfs_path]
  [TBLPROPERTIES (property_name=property_value, ...)];
  ```

- Here is an example of creating an internal table with four columns and loading data from a local file:

  ```sql
  CREATE TABLE IF NOT EXISTS employees
  (id INT, name STRING, dept STRING, salary FLOAT)
  COMMENT 'This is a table for storing employee data';
  
  LOAD DATA LOCAL INPATH '/home/hadoop/employees.txt' INTO TABLE employees;
  ```

- Here is an example of creating an external table with the same schema and loading data from an external location:

  ```sql
  CREATE EXTERNAL TABLE IF NOT EXISTS employees
  (id INT, name STRING, dept STRING, salary FLOAT)
  COMMENT 'This is a table for storing employee data'
  LOCATION 'hdfs://namenode:8020/user/hadoop/employees';
  ```

- Some advantages of using tables in Hive are:
  - They allow users to read and write data in various formats, such as text, JSON, Parquet, ORC, etc., using SerDes and Input/Output formats.
  - They support partitioning and bucketing to improve query performance and data organization.
  - They support data skew handling to avoid data imbalance and hotspots.
  - They can be accessed by other tools and frameworks, such as Spark, Pig, MapReduce, etc.