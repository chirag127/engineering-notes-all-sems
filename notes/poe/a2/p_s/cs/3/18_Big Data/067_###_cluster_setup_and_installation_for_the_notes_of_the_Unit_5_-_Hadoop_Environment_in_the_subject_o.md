 Here is the content written in markdown format for the topic #### Hive services:

#### Hive services

- Hive SQL: Hive SQL is a query language similar to SQL which is used to query the data stored in HDFS. It provides a schema on read functionality and hides the complexities of MapReduce jobs.
- Metastore: The metastore is a database that stores the metadata about the Hive tables such as their schema and location. By default, Derby database is used as the metastore but MySQL or PostgreSQL can also be configured.
- Driver: The driver acts as an interface between the HiveQL and metastore. It accepts the HiveQL statements, converts them into an execution plan consisting of MapReduce or Tez jobs and executes them.
- CLI: Hive comes with a command-line interface which can be used to interact with Hive. The CLI accepts HiveQL statements and provides a shell-like experience.
- Web Interface: Hive also provides a web interface to interact with it. It is built using Java Server Pages and allows executing queries, browsing tables, and monitoring jobs via a web browser.
- Optimization: Hive performs multiple optimizations such as prunning, merging map-reduce jobs, etc to improve query performance. Some of the key optimization techniques are:
-- Prunning: Removal of unnecessary columns/partitions from queries
-- Merge map-reduce jobs: Merging multiple small jobs into a single job
-- Vectorization: Processing multiple rows at once instead of a single row
- Pluggable architectures: One of the key features of Hive is its pluggable architectures which allow extensions and customizations. Some pluggable components are:
-- File formats: Text, RCFile, ORC, Parquet, etc
-- Serde (Serializer-Deserializer): Converts data from Row format to desired format and vice-versa
-- UDF (User-Defined Functions): Custom functions and aggregations
-- Input-Output formats: Custom input and output formats

The above points cover the key Hive services and concepts to learn and understand Hive for exams and study purpose. Let me know if you would like me to elaborate on any of the points or add more details.