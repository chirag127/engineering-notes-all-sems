#### Introduction to Tables in Hive

- Tables in Hive are used to store structured data.
- Tables can be created from external data sources or from data already present in the Hive warehouse.
- Hive supports different file formats like CSV, JSON, ORC, and Parquet for tables.
- Tables in Hive can be partitioned for better performance.

#### Creating Tables in Hive

- Tables can be created in Hive using the `CREATE TABLE` statement.
- It is important to specify the columns and their data types while creating a table.
- The `LOCATION` keyword can be used to specify the directory where the table data will be stored.
- Example syntax: `CREATE TABLE table_name (column1_name column1_datatype, column2_name column2_datatype) LOCATION 'hdfs://user/hive/warehouse/table_name';`

#### Loading Data into Tables in Hive

- Data can be loaded into tables in Hive using the `LOAD DATA` statement.
- The `LOCAL` keyword can be used to specify the local file system path of the data to be loaded.
- The `INTO TABLE` keyword is used to specify the destination table.
- Example syntax: `LOAD DATA LOCAL INPATH '/path/to/data' INTO TABLE table_name;`

#### Querying Tables in Hive

- Tables in Hive can be queried using the `SELECT` statement.
- It is important to specify the columns to be selected while querying a table.
- Filters and sorting can be applied to the query results using the `WHERE` and `ORDER BY` clauses respectively.
- Example syntax: `SELECT column1_name, column2_name FROM table_name WHERE column1_name = 'value' ORDER BY column2_name;`

#### Partitioning Tables in Hive

- Partitioning tables in Hive can improve query performance by segregating data based on a specific column.
- The `PARTITIONED BY` keyword is used to specify the partition column while creating a table.
- Partitions can be added to a table using the `ALTER TABLE ADD PARTITION` statement.
- Example syntax: `CREATE TABLE table_name (column1_name column1_datatype, column2_name column2_datatype) PARTITIONED BY (partition_column_name partition_column_datatype);`