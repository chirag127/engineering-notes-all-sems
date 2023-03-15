#### Tables in Hive

- A table in Hive is a set of data that uses a schema to sort the data by given identifiers.
- The table we create in any database will be stored in the sub-directory of that database.
- The default location where the database is stored on HDFS is `/user/hive/warehouse`.
- There are two types of tables that you can create with Hive: **internal** and **external**  .
- **Internal tables** are also known as **managed tables** .
- Data is stored in the Hive data warehouse.
- The data warehouse is located at `/hive/warehouse/` on the default storage for the cluster.
- Use internal tables when one of the following conditions applies:
  - The data is temporary and can be deleted when the table is dropped.
  - The data is not used by any other application outside Hive.
  - The data is loaded from a local file system or another Hive table.
- **External tables** are also known as **unmanaged tables** .
- Data is stored outside the data warehouse.
- The data can be stored on any storage accessible by the cluster.
- Use external tables when one of the following conditions apply:
  - The data is permanent and should not be deleted when the table is dropped.
  - The data is used by other applications outside Hive.
  - The data is loaded from a remote source or a non-default storage.
- The general syntax for creating a table in Hive is:

```sql
CREATE [TEMPORARY] [EXTERNAL] TABLE [IF NOT EXISTS] table_name
[(column_name data_type [COMMENT column_comment], ...)]
[COMMENT table_comment]
[PARTITIONED BY (column_name data_type [COMMENT column_comment], ...)]
[CLUSTERED BY (column_name, column_name, ...) [SORTED BY (column_name [ASC|DESC], ...)] INTO num_buckets BUCKETS]
[SKEWED BY (column_name, column_name, ...) ON ((column_value, column_value, ...), ...) [STORED AS DIRECTORIES]]
[ROW FORMAT row_format]
[STORED AS file_format]
[LOCATION hdfs_path]
[TBLPROPERTIES (property_name=property_value, ...)];
```