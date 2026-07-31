
#### Tables in Hive
- Hive is a data warehouse infrastructure built on top of Hadoop for providing data summarization, query, and analysis.
- Hive tables are similar to relational database tables in that they are organized into rows and columns.
- Hive tables can be created using two different approaches: the internal and the external table. 
- Internal tables are managed by Hive, meaning that the data and metadata associated with the table are stored in the Hive metastore. 
- External tables are used to access external data sources, such as HDFS, S3, or other data sources. 
- Hive allows users to create tables with partitioned columns. Partitioning is a way of dividing a table into related parts based on the values of particular columns like date, city, and department. 
- Hive also supports bucketing, which is a technique of dividing the table into more manageable parts based on the values of a particular column. 
- Hive supports a wide range of data types, including primitive types such as strings, integers, floats, and booleans, as well as complex types such as maps, structs, and arrays.