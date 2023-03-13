 Here is the content in markdown format on the topic #### tables in Hive:

#### Tables in Hive

- Hive tables are classified into 4 types:
  - #### Managed tables:
    - Data is stored in HDFS.
    - Hive metastore contains the table metadata.
    - When dropped, only the metadata is deleted but the data remains in HDFS.
    - Used when you want to reuse the table data.
    - Example: CREATE TABLE tbl1(col1 int, col2 string) ROW FORMAT DELIMITED;
  - #### External tables:
    - Data is stored in HDFS.
    - Hive metastore contains the table metadata.
    - When dropped, only the metadata is deleted but the data remains in HDFS.
    - Used when the table data is not managed by Hive and you don't want Hive to delete it.
    - Example: CREATE EXTERNAL TABLE tbl2(col1 int, col2 string) ROW FORMAT DELIMITED LOCATION '/path/to/data';
  - #### Virtual tables:
    - No data is stored, view over data from other tables.
    - Queries on virtual table get translated to queries on underlying tables.
    - Used to reuse queries/views.
    - Example: CREATE VIRTUAL TABLE vtbl AS SELECT col1 + col2 FROM tbl1;
  - #### Temp tables:
    - Data is stored temporarily on the filesystem.
    - Exists only for the duration of the Hive session.
    - Used for intermediate/temporary storage.
    - No metastore involved.
    - Example: CREATE TEMPORARY TABLE temptbl(col1 int, col2 string);

- Some mnemonics/learning tricks:
  - Think of managed and external tables as similar to internal and external hard disks.
  - Virtual tables are like shortcuts/aliases to other tables.
  - Temp tables are like scratch pads which get erased once the session ends.
- Advantages: Flexibility to choose the right table type based on use case.
- Disadvantages: Need to keep track of the different types and their behaviors.
- Applications: Storing data, reusing queries, temporary storage, etc.