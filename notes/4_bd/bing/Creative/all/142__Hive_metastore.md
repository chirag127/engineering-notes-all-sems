#### Hive metastore

- Hive metastore (HMS) is a service that stores metadata related to Apache Hive and other services, such as Impala, Spark, and Presto, in a backend relational database, such as MySQL or PostgreSQL  .
- Metadata includes information about the tables, partitions, columns, data types, locations, statistics, and more.
- HMS provides a central repository of metadata that can easily be analyzed to make informed, data-driven decisions, and therefore it is a critical component of many data lake architectures.
- HMS provides clients access to this information using the metastore service API, which is a thrift interface that supports multiple concurrent connections and authentication .
- HMS also communicates with the NameNode that represents HDFS, where the physical data is stored, and with the security service, such as Ranger, for authorization and auditing .
- HMS can operate in different modes, such as embedded, local, or remote, depending on the deployment and configuration of the backend database and the Hive services.
- HMS can also support multiple metastores for different clusters or namespaces, using the catalog feature introduced in Hive 3.0.
- HMS can perform various operations on the metadata, such as creating, altering, dropping, and querying tables and partitions, as well as managing schemas, statistics, and privileges.
- HMS can also support advanced features, such as ACID transactions, data compaction, replication, and caching .
- HMS uses Apache Calcite's cost-based query optimizer (CBO) and query execution framework to optimize SQL queries.

: https://hive.apache.org/
: https://docs.cloudera.com/runtime/7.2.7/hive-hms-overview/topics/hive-hms-introduction.html
: https://docs.cloudera.com/runtime/7.2.8/hive-hms-overview/index.html