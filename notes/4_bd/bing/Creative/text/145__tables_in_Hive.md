#### Tables in Hive

- Tables in Hive are a way of storing and querying structured data in Apache Hadoop, a distributed data processing framework.
- Tables in Hive have a schema that defines the names and types of the columns, as well as other properties such as partitioning, bucketing, compression, etc.
- Tables in Hive can be created using the Hive Query Language (HiveQL), a SQL-like language that allows users to perform various operations on the data, such as creating, altering, dropping, inserting, selecting, joining, etc.
- Tables in Hive can be broadly classified into two types: internal tables and external tables.

##### Internal Tables

- Internal tables are also known as managed tables, as Hive manages their data and metadata.
- Internal tables store their data in the Hive warehouse directory, which is /user/hive/warehouse by default, unless specified otherwise.
- Internal tables are created using the syntax:

```
CREATE TABLE [IF NOT EXISTS] table_name (col_name data_type [COMMENT 'col_comment'], ...) [COMMENT 'table_comment'] [ROW FORMAT row_format] [STORED AS file_format];
```

- Internal tables are suitable for data that is temporary, transient, or exclusive to Hive.
- Internal tables are deleted along with their data and metadata when the DROP TABLE command is issued.

##### External Tables

- External tables are also known as unmanaged tables, as Hive does not manage their data, only their metadata.
- External tables store their data outside the Hive warehouse directory, in any location accessible by the cluster, such as HDFS, S3, etc.
- External tables are created using the syntax:

```
CREATE EXTERNAL TABLE [IF NOT EXISTS] table_name (col_name data_type [COMMENT 'col_comment'], ...) [COMMENT 'table_comment'] [ROW FORMAT row_format] [FIELDS TERMINATED BY char] [STORED AS file_format] LOCATION 'hdfs_path';
```

- External tables are suitable for data that is shared, permanent, or independent of Hive.
- External tables are not deleted along with their data when the DROP TABLE command is issued, only their metadata is removed. The data remains in the original location and can be accessed by other applications.

##### Managed vs External Tables

- The main difference between internal and external tables is how Hive handles their data and metadata.
- Internal tables are fully controlled by Hive, while external tables are only partially controlled by Hive.
- Internal tables store their data in the Hive warehouse directory, while external tables store their data in any location outside the Hive warehouse directory.
- Internal tables are deleted along with their data and metadata when the DROP TABLE command is issued, while external tables are not deleted along with their data when the DROP TABLE command is issued, only their metadata is removed.
- Internal tables are suitable for data that is temporary, transient, or exclusive to Hive, while external tables are suitable for data that is shared, permanent, or independent of Hive.

##### Identify the Type of Hive Table

- To identify the type of a Hive table, we can use the DESCRIBE FORMATTED command, which shows the detailed information about the table, such as its columns, properties, location, etc.
- For example, to identify the type of the table employees, we can run the command:

```
DESCRIBE FORMATTED employees;
```

- The output will show the table type as either MANAGED_TABLE or EXTERNAL_TABLE, depending on how the table was created. For example:

```
# col_name             data_type            comment             
id                     int                                         
name                   string                                      
country                string                                      
department             string                                      
salary                 int                                         
# Detailed Table Information             
Database:              company             
Owner:                 root             
CreateTime:            Tue Mar 14 18:36:00 GMT 2023             
LastAccessTime:        UNKNOWN             
Protect Mode:          None             
Retention:             0             
Location:              hdfs://localhost:9000/user/hive/warehouse/company.db/employees             
Table Type:            MANAGED_TABLE             
Table Parameters:             
        transient_lastDdlTime   1615737360             
# Storage Information             
SerDe Library:         org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe             
InputFormat:           org.apache.hadoop.mapred.TextInputFormat             
OutputFormat:          org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat             
Compressed:            No             
Num Buckets:           -1             
Bucket Columns:        []             
Sort Columns:          []             
Storage Desc Params:             
        field.delim             -             
        serialization.format    -             
```

- In this