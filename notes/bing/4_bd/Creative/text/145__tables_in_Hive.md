#### Tables in Hive

- Tables in Hive are similar to tables in a relational database management system. They store data in columns and rows and belong to a database .
- There are two types of tables in Hive: internal and external   .
  - Internal tables: Data is stored in the Hive data warehouse, which is located at /hive/warehouse/ on the default storage for the cluster. Internal tables are also called managed tables because Hive manages their lifecycle and data . When an internal table is dropped, the data and the metadata are deleted  . Use internal tables when the data is temporary or exclusive to Hive  .
  - External tables: Data is stored outside the Hive data warehouse, on any storage accessible by the cluster. External tables are also called unmanaged tables because Hive does not manage their lifecycle and data . When an external table is dropped, only the metadata is deleted, but the data remains  . Use external tables when the data is shared by other applications or needs to be preserved after dropping the table  .
- The general syntax for creating a table in Hive is:

  ```
  CREATE [TEMPORARY] [EXTERNAL] TABLE [IF NOT EXISTS] [db_name.]table_name
  [(col_name data_type [COMMENT col_comment], ...)]
  [COMMENT table_comment]
  [PARTITIONED BY (col_name data_type [COMMENT col_comment], ...)]
  [CLUSTERED BY (col_name, col_name, ...) [SORTED BY (col_name [ASC|DESC], ...)] INTO num_buckets BUCKETS]
  [SKEWED BY (col_name, col_name, ...) ON ((col_value, col_value, ...), (col_value, col_value, ...), ...) [STORED AS DIRECTORIES]]
  [
   [ROW FORMAT row_format] 
   [STORED AS file_format]
     | STORED BY 'storage.handler.class.name' [WITH SERDEPROPERTIES (...)] 
  ]
  [LOCATION hdfs_path]
  [TBLPROPERTIES (property_name=property_value, ...)]
  [AS select_statement];
  ```

- An example of creating an internal table in Hive is:

  ```
  CREATE TABLE IF NOT EXISTS employees (
    id INT,
    name STRING,
    salary FLOAT,
    department STRING
  )
  COMMENT 'This is a table for storing employee data'
  ROW FORMAT DELIMITED
  FIELDS TERMINATED BY ','
  STORED AS TEXTFILE;
  ```

- An example of creating an external table in Hive is:

  ```
  CREATE EXTERNAL TABLE IF NOT EXISTS employees (
    id INT,
    name STRING,
    salary FLOAT,
    department STRING
  )
  COMMENT 'This is a table for storing employee data'
  ROW FORMAT DELIMITED
  FIELDS TERMINATED BY ','
  STORED AS TEXTFILE
  LOCATION '/hadoop/employees';
  ```