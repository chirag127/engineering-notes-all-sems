 Here is the content in markdown format:

### Hadoop configuration for the notes of the Unit 5 - Hadoop Environment in the subject of Big Data

- Hadoop configuration refers to the settings/parameters that can be tuned in the Hadoop cluster for better performance and optimization.
- The main components that require configuration are:
** HDFS - Replication factor, block size, NameNode heap size, DataNode heap size, etc.
** YARN - Number of resource managers, node managers, application masters, container sizes, etc.
** MapReduce - Number of maps and reduces, heap sizes, etc.
- The configuration is done in `core-site.xml`, `hdfs-site.xml` and `yarn-site.xml` files of Hadoop.
- Some of the key configuration parameters to tune for optimization are:
** Increasing replication factor and block size for HDFS to increase throughput and fault tolerance.
** Increasing container sizes and number of nodes for YARN for better resource allocation.
** Tuning Map and Reduce parameters for MapReduce as per the job requirements.
- The configuration has to be done carefully by testing and benchmarking the Hadoop cluster for optimal performance based on the workload.

#### Hive metastore

- Hive metastore is a database that stores the metadata/schema information of the tables/partitions in Hive.
- The metadata includes table names, column names, data types, partition keys, locations of HDFS files, etc.
- By default, Hive uses a Derby database to store the metastore. But for production use, it is recommended to use MySQL or PostgreSQL which are more robust and scalable.
- The benefits of using an external metastore are:
** Better performance as the database is optimized for storing and querying metadata.
** Support for concurrent queries and ACID transactions.
** Persistence of metadata even after the Hive service is restarted.
** Scalability to handle metadata of huge tables and partitions.
- The metastore can be configured in the `hive-site.xml` file by specifying the JDBC connection parameters to the external database.
- The metastore is a critical component of Hive and its performance and reliability impacts the performance of Hive queries. Hence, it is important to use a robust external database for the metastore in production Hive deployments.