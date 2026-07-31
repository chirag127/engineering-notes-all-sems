#### Tables in Hive

- Tables in Hive are similar to tables in a relational database management system. They store data in columns and rows and belong to a database.   
- Tables in Hive can be created using the `CREATE TABLE` statement, which specifies the table name, column names, data types, and optionally, table properties and storage options.  
- Tables in Hive can be classified into two types: internal and external.   
  - Internal tables: Data is stored in the Hive data warehouse, which is located at `/hive/warehouse/` on the default storage for the cluster. Internal tables are managed by Hive and are deleted when the table is dropped. Use internal tables when the data is temporary and exclusive to Hive.   
  - External tables: Data is stored outside the Hive data warehouse, in any storage accessible by the cluster. External tables are not managed by Hive and are not deleted when the table is dropped. Use external tables when the data is permanent and shared by other applications.   
- Tables in Hive can also be partitioned and bucketed to improve query performance and data organization. Partitioning divides the table data into subdirectories based on column values. Bucketing splits the data into files based on a hash function of a column.