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
[TBLPROPERTIES (property_name=property_value, ...)]
```

- Tables in Hive can be classified into two types: internal and external.    
  - Internal tables: Data is stored in the Hive data warehouse, which is located at `/hive/warehouse/` on the default storage for the cluster. Internal tables are also called managed tables, as Hive manages their data and metadata. When an internal table is dropped, both the data and metadata are deleted. Use internal tables when the data is temporary or exclusive to Hive.    
  - External tables: Data is stored outside the Hive data warehouse, on any storage accessible by the cluster. External tables are also called unmanaged tables, as Hive only manages their metadata. When an external table is dropped, only the metadata is deleted, while the data remains intact. Use external tables when the data is shared by other applications or needs to be preserved after dropping the table.    
- Tables in Hive can also be partitioned, clustered, and sorted to improve query performance and data organization.    
  - Partitioning: Partitioning divides a table into multiple sub-tables based on one or more columns. Each sub-table is stored in a separate directory on the file system. Partitioning allows Hive to scan only the relevant sub-tables for a query, reducing the amount of data to be processed.    
  - Clustering: Clustering distributes the data in a table or a partition into multiple files or buckets based on one or more columns. Each bucket is assigned a hash value and stored in a separate file. Clustering allows Hive to perform efficient joins and sampling on the table or partition.    
  - Sorting: Sorting orders the data in a table or a partition or a bucket based on one or more columns. Sorting can be done in ascending or descending order. Sorting allows Hive to perform faster queries with filters or range conditions on the sorted columns.