#### Tables in Hive

- Tables in Hive are similar to tables in a relational database management system. They store data in columns and rows and belong to a database. Each table has a schema that defines the column names, data types, and constraints.
- Tables in Hive can be created using the `CREATE TABLE` statement. The syntax is as follows:

```
CREATE [TEMPORARY] [EXTERNAL] TABLE [IF NOT EXISTS] [db_name.]table_name
[(col_name data_type [COMMENT col_comment], ...)]
[COMMENT table_comment]
[PARTITIONED BY (col_name data_type [COMMENT col_comment], ...)]
[CLUSTERED BY (col_name, col_name, ...) [SORTED BY (col_name [ASC|DESC], ...)] INTO num_buckets BUCKETS]
[STORED AS file_format]
[LOCATION hdfs_path]
[TBLPROPERTIES (property_name=property_value, ...)];
```

- Tables in Hive can be classified into two types: internal and external. The main difference between them is how the data is managed and deleted.

  - Internal tables: Data is stored in the Hive data warehouse, which is located at `/hive/warehouse/` on the default storage for the cluster. When an internal table is dropped, the data and the metadata are deleted. Use internal tables when the data is exclusive to Hive and not accessed by other applications.
  - External tables: Data is stored outside the data warehouse, on any storage accessible by the cluster. When an external table is dropped, only the metadata is deleted, but the data remains intact. Use external tables when the data is shared by other applications or needs to be preserved after dropping the table.

- Tables in Hive can also be partitioned and bucketed to improve query performance and data organization. Partitioning divides a table into multiple sub-tables based on one or more columns, such as date or country. Bucketing splits the data within a partition into multiple files based on a hash function of one or more columns, such as customer_id or product_id.