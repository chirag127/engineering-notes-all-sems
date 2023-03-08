 Here is the content in markdown format for the topic ### Hive metastore for the notes of the Unit 11 - Hadoop Eco System Frameworks in the subject of Big Data:

#### Hive Metastore
- The Hive Metastore is a relational database that stores the metadata of Hive tables such as schema and partition information.
- It keeps information about the table names, column names, data types, partition keys, storage locations, etc.
- By default, Derby database is used as the metastore but for large clusters, MySQL or PostgreSQL can be used which provide better performance and high availability.
- The metastore service can be run in embedded mode, standalone mode or high availability mode.
- In embedded mode, the metastore service runs within the HiveServer2 process. In standalone mode, a separate metastore service process is started. In high availability mode, multiple metastore instances are run with automatic failover.
- The metastore contains the schema or structure of tables and partitions. Whenever Hive executes a query, it first consults the metastore to obtain the schema information to validate and process the query.
- The metastore helps decouple the schema information from the HDFS data and enables multiple Hive clients to share the same schema. It is a critical component of Hive and its availability and performance have significant impact on Hive queries.

Advantages:
- Central repository of table metadata
- Decouples schema from data
- Enables reuse of schema across sessions and users
- Supports large number of tables and partitions

Disadvantages:
- Single point of failure (ameliorated using HA configuration)
- Performance bottleneck for large clusters
- Requires additional maintenance

Examples:
- CREATE TABLE, ALTER TABLE, DROP TABLE statements update the metastore
- DESCRIBE <table> queries the metastore

Applications:
- Core component of Hive
- Used by other tools in Hadoop ecosystem that run on Hive such as Pig