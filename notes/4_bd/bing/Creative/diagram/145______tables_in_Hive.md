#### Tables in Hive

- Tables in Hive are similar to tables in a relational database management system. They store data in columns and rows and belong to a database.
- Tables in Hive can be created using the `CREATE TABLE` statement with the following syntax:

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

- Tables in Hive can be classified into two types: internal and external.
- Internal tables are also known as managed tables. They are the default type of tables in Hive. They store data in the Hive data warehouse, which is located at `/user/hive/warehouse` on the default storage for the cluster. When an internal table is dropped, the data and the metadata are both deleted. Internal tables are suitable for data that is temporary, transient, or exclusive to Hive.
- External tables store data outside the Hive data warehouse, on any storage accessible by the cluster. The data can be in any format, such as CSV, JSON, Parquet, etc. When an external table is dropped, only the metadata is deleted, but the data remains intact. External tables are suitable for data that is shared, permanent, or used by other applications.