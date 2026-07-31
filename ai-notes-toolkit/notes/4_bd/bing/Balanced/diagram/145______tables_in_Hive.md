#### Tables in Hive

- Tables in Hive are similar to tables in a relational database management system. They store data in columns and rows and belong to a database.   
- Tables in Hive can be created using the `CREATE TABLE` statement. The syntax is as follows:

```
CREATE [TEMPORARY] [EXTERNAL] TABLE [IF NOT EXISTS] [db_name.]table_name
[(col_name data_type [COMMENT col_comment], ... [constraint_specification])]
[COMMENT table_comment]
[PARTITIONED BY (col_name data_type [COMMENT col_comment], ...)]
[CLUSTERED BY (col_name, col_name, ...) [SORTED BY (col_name [ASC|DESC], ...)] INTO num_buckets BUCKETS]
[SKEWED BY (col_name, col_name, ...) ON ((col_value, col_value, ...), (col_value, col_value, ...), ...) [STORED AS DIRECTORIES]]
[ROW FORMAT row_format]
[STORED AS file_format]
[LOCATION hdfs_path]
[TBLPROPERTIES (property_name=property_value, ...)]
[AS select_statement];
```

- Tables in Hive can be classified into two types: internal and external.   
  - Internal tables: Data is stored in the Hive data warehouse, which is located at `/hive/warehouse/` on the default storage for the cluster. Internal tables are also called managed tables, as Hive manages their data and metadata. When an internal table is dropped, both the data and metadata are deleted. Use internal tables when the data is temporary or exclusive to Hive.   
  - External tables: Data is stored outside the Hive data warehouse, on any storage accessible by the cluster. External tables are also called unmanaged tables, as Hive only manages their metadata. When an external table is dropped, only the metadata is deleted, while the data remains intact. Use external tables when the data is shared by other applications or needs to be preserved after dropping the table.